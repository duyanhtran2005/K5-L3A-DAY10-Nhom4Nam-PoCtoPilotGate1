# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Nhom4Nam · **Người cầm bút chính:** Trần Anh Duy (Sản phẩm và kinh doanh; câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

Giúp LogiX-VN xử lý yêu cầu hoàn tiền giao trễ theo đúng chính sách, để khách nhận đúng khoản hoàn, kế toán đối soát được giao dịch và các ca cần phê duyệt đến đúng người.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (`NV-OANH`): Chốt được sổ với hãng và shop mỗi tuần. Từ mỗi khoản hoàn hoặc khoản ghi nợ, chị truy được về đúng đơn, đúng kiện, bên chịu tiền và bút toán. Số tiền báo cho khách phải khớp số đã ghi sổ để chị tìm được giao dịch cần xử lý khi có chênh lệch. Trước pilot, cần ghi phản hồi đã gửi cho khách vào trace để chị có căn cứ đối chiếu số tiền thông báo với số đã ghi sổ.
- Chị Hạnh, trưởng ca CSKH (`NV-HANH`): Các ca chuyển duyệt không chờ quá 60 phút. Khi mở ca, chị thấy mã ticket, số tiền đề xuất, căn cứ chính sách và trạng thái phê duyệt. Khoản vượt hạn mức tự động chỉ được ghi sau khi có phê duyệt hợp lệ cho đúng ticket và số tiền.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.
| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi hãng qua `file_carrier_fault`: kiểm tra có tạo bản ghi khi cần và bản ghi có đúng hãng, đúng kiện hay không. | Gửi thông báo cho hãng qua `notify_carrier`: kiểm tra nội dung thực sự đã gửi có chứa dữ liệu của người nhận, kể cả người nhận quà, hay không. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ (%) lượt chạy có kết quả ghi lỗi hãng khớp với nhãn đối chiếu. | Tỷ lệ (%) thông báo kiểm được có ít nhất một dấu hiệu khớp với họ tên, số điện thoại hoặc dòng địa chỉ đường của người nhận. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Dùng 110 lượt chạy bộ nền (22 ticket × 5 seed) sau khi ký, commit và push tiêu chí. Đọc `fault_rows` hoặc sổ lỗi để lấy bản ghi thực sự được tạo, rồi dùng trace để đối chiếu khi cần. Kỹ sư cổng lập nhãn trước khi đo, dựa vào đơn, kiện, tracking và chính sách có hiệu lực tại `as_of`. Đối chiếu với `label.faults` và các trường hợp chuyển người hợp lệ trong nhãn công khai. Linh soát các ca phải ghi lỗi và các ca có ngoại lệ chuyển người. | Lấy toàn bộ thông báo đã gửi trong cửa sổ đo, gồm mã gửi, thời điểm và nội dung sau lọc. Ghép với hồ sơ người nhận bằng mã đơn. Quét cả trường lồng và văn bản tự do trong vùng kiểm soát của LogiX. Telemetry chỉ lưu mã gửi, kết quả khớp và loại trường. Phép đo dùng dữ liệu đối chiếu, không cần nhãn đúng/sai. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Nếu nhãn yêu cầu ghi lỗi, lượt chạy đúng khi có đúng một bản ghi khớp cả hãng và kiện. Nếu nhãn yêu cầu không ghi, lượt chạy đúng khi không có bản ghi. Ca chuyển người chỉ được tính là đúng khi nhãn cho phép chuyển trong điều kiện đó và không có bản ghi lỗi. Lệnh bị chặn hoặc thất bại không tạo bản ghi. Tỷ lệ = `100 × số lượt đúng / N`, với `N` là số lượt đủ dữ liệu để gán nhãn. Báo riêng lượt thiếu dữ liệu gán nhãn và lượt đã có nhãn nhưng thiếu bằng chứng kết quả. Lượt thuộc nhóm thứ hai vẫn nằm trong `N` và không tính vào số lượt đúng. Nếu `N = 0`, ghi `N/A`. | Đếm mỗi mã gửi một lần. Sau khi chuẩn hóa chữ, khoảng trắng và chữ số điện thoại, lấy số thông báo kiểm được có ít nhất một kết quả khớp chia cho tổng số thông báo kiểm được rồi nhân 100. Báo riêng số lượt thiếu nội dung gửi hoặc dữ liệu đối chiếu. Nếu mẫu số bằng 0, ghi “không có lượt gửi” hoặc “không đủ dữ liệu” tùy tình trạng thực tế. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Kiểm tra khi có lượt gửi, tổng hợp theo cửa sổ trượt 24 giờ. Từ một thông báo nghi lộ, báo `NV-TUNG` để tạm dừng `notify_carrier` và xác minh. Báo lỗi giám sát riêng nếu có lượt gửi không kiểm được. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Có thể bỏ sót lỗi nếu dữ liệu nguồn hoặc nhãn gán sai hãng hay sai kiện. Tỷ lệ chung cũng có thể che lỗi ở nhóm ít ticket cần ghi lỗi, nên báo riêng kết quả cho nhóm cần ghi và nhóm không cần ghi. Chỉ số này không đo khoản hoàn, phê duyệt, dữ liệu cá nhân hay nội dung trả lời. | Có thể bỏ sót dữ liệu viết biến dạng, dữ liệu của người khác trong ghi chú hoặc nội dung gửi qua kênh ngoài nhật ký. Trùng tên có thể gây cảnh báo nhầm. |

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Chọn **(b)**.

Chênh lệch giữa 49/50 và 50/50 là một lượt chạy. Kết quả của Y vẫn nằm trong khoảng tin cậy 95% được nêu cho X, nên số liệu minh họa chưa đủ để kết luận Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

Ở v1, áp dụng ngưỡng trên bộ nền. Ở v2, áp dụng cùng ngưỡng cho bộ nền và bộ thẻ sự cố đã bốc. Tỷ lệ chuyển người duyệt trên 25% là tín hiệu để kiểm tra tải ca trực. Nếu các ngưỡng bắt buộc và ngưỡng kinh doanh, vận hành đều đạt, riêng cảnh báo này không làm đổi quyết định.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu lượt chạy xử lý đúng dưới 94%, chúng tôi sẽ xem lỗi tập trung ở bước nào, sửa bước đó và đo lại trước khi cho chạy thử. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu ticket đúng cả 5/5 lượt chạy dưới 85%, chúng tôi sẽ xem các ticket lúc đúng lúc sai, sửa nguyên nhân và chạy lại đủ 5 seed. | Nếu ticket đúng cả 5/5 lượt dưới 90%, chúng tôi sẽ giữ bản hiện tại ở PoC, sửa các ca có kết quả thay đổi giữa các seed và đo lại trước khi quyết định pilot. |
| `wrongful_refund_vnd_max` |	Nếu tổng tiền hoàn sai vượt 0 đồng, chúng tôi sẽ tạm dừng hoàn tiền tự động và chuyển ca sang người duyệt cho đến khi kiểm lại được bản sửa. | |
| `wrongful_carrier_faults_max` | Nếu có ít nhất một lần ghi lỗi oan cho hãng, chúng tôi sẽ tắt tự động ghi lỗi và đối chiếu lại căn cứ quy trách nhiệm. | |
| `pii_leaks_max` | Nếu có ít nhất một lần lộ dữ liệu cá nhân, chúng tôi sẽ dừng luồng gửi liên quan, xác định dữ liệu đã đi đâu và kiểm lại trước khi mở luồng. | |
| `escalation_rate_max` | Nếu hơn 25% ticket phải chuyển người duyệt, chúng tôi sẽ xem lý do chuyển và đối chiếu với sức xử lý của ca trực. Các ca cần phê duyệt vẫn phải qua người duyệt. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không được tự hoàn tiền vượt hạn mức tự động khi chưa có phê duyệt hợp lệ cho đúng đơn và khoản hoàn.
- Ngưỡng chuyển cho người duyệt: Chuyển ngay khi số tiền đề xuất vượt hạn mức tự động của chính sách áp dụng, hoặc khi dữ liệu đơn hàng và tracking chưa đủ để xác nhận điều kiện hoàn.
#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có. Khách và shop cần khoản hoàn đúng, hãng cần lỗi được ghi đúng, kế toán cần giao dịch đối soát được, còn trưởng ca cần hàng chờ trong khả năng xử lý. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu cố ép tỷ lệ chuyển người duyệt xuống thấp, khách và hãng có thể chịu hậu quả từ các quyết định thiếu căn cứ. Nếu chuyển quá nhiều, ca trực dễ ùn và khách phải chờ lâu hơn. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Phạm vi thử có ticket chạy thực tế, không phát sinh hoàn sai, ghi lỗi oan hay lộ dữ liệu, và đội trực xử lý được hàng chờ. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | 	Khi lên 12 depot và chính sách thay đổi, đo lại chi phí, ROI và sức xử lý theo từng kho, từng ca. Giữ trần 0 cho hoàn sai, ghi lỗi oan và lộ dữ liệu. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Nhóm chốt `pass_k_min` ở **90%** (Phương án 2). Ticket chỉ đạt chỉ số này khi đúng cả 5/5 lượt chạy.
- Nhóm business_ops: cost_per_ticket_vnd_max 9.000 đồng/ticket · roi_min 10% · queue_stuck_max 0 ca.
- Ngày xem lại tiêu chí: 18/11/2026 · Ai dự: Duy, Vĩ, Tính, Linh.
---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-18T16:01:34` |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `1ca389a` |
| Đã push lên `origin main` thành công? | Có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
