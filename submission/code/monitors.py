"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def max_daily_carrier_faults(trials):
    """Largest count of recorded carrier faults in one day/seed/carrier group.

    Uses the unlabeled monitor view only. Missing grouping data on a fault is
    an error, rather than a zero that could silently suppress an alert.
    """
    counts = {}
    for trial in trials:
        faults = trial.get("faults", [])
        if not faults:
            continue
        day, seed = trial.get("day"), trial.get("seed")
        if day is None or seed is None:
            raise ValueError("carrier faults require day and seed")
        for fault in faults:
            carrier = fault.get("carrier_id")
            if not carrier:
                raise ValueError("carrier fault requires carrier_id")
            key = (day, seed, carrier)
            counts[key] = counts.get(key, 0) + 1
    return max(counts.values(), default=0)


MONITORS = {
    "max_daily_carrier_faults": max_daily_carrier_faults,
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
}
STARTER_MONITORS = ("escalation_rate",)
