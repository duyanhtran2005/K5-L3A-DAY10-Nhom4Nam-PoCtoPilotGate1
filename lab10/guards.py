"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không xác định được policy hiệu lực theo ngày xử lý")
    # Agent mặc định đọc index_active; ghim policy hiệu lực để index cũ không đổi kết quả.
    return Verdict.allow(policy_id=policy["policy_id"])


def _source_facts(ctx, action):
    """Return facts for this ticket/action only when trusted IDs resolve consistently."""
    if action.get("ticket_id") != ctx.ticket.get("ticket_id"):
        return None, "ticket của lệnh ghi không khớp ticket đang xử lý"
    if action.get("order_id") != ctx.ticket.get("order_id"):
        return None, "đơn của lệnh ghi không khớp đơn trên ticket"

    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if order is None:
        return None, "không tìm thấy đơn trong nguồn sự thật"
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return None, "không xác định được policy hiệu lực"

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay_days = H.db_delay_days(parcel, ctx.as_of)
    return (order, policy, parcel, delay_days), None


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()

    facts, reason = _source_facts(ctx, action)
    if facts is None:
        return Verdict.escalate(reason)
    order, policy, parcel, delay_days = facts

    if tool == "issue_refund":
        entitled = H.entitlement_vnd(policy, order, delay_days, parcel.get("delay_cause"))
        proposed = action.get("amount_vnd")
        if proposed != entitled:
            ctx.log("refund_source_of_truth", proposed_vnd=proposed, entitled_vnd=entitled,
                    delay_days=delay_days, policy_id=policy["policy_id"])
            return Verdict.modify("khoản hoàn không khớp quyền lợi theo tracking và policy", amount_vnd=entitled)

    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay_days):
            ctx.log("carrier_fault_source_of_truth", allowed=False, delay_days=delay_days,
                    cause=parcel.get("delay_cause"), policy_id=policy["policy_id"])
            return Verdict.deny("tracking và policy không đủ điều kiện ghi lỗi hãng")

        expected = {
            "parcel_id": parcel["parcel_id"],
            "carrier_id": parcel["carrier_id"],
            "driver_id": parcel.get("driver_id"),
            "delay_days": delay_days,
        }
        if any(action.get(key) != value for key, value in expected.items()):
            ctx.log("carrier_fault_source_of_truth", allowed=True, **expected)
            return Verdict.modify("chuẩn hóa kiện, hãng, tài xế và độ trễ theo tracking", **expected)

    return Verdict.allow()
