# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Nhom4Nam`
- Lớp: `L3A`
- Repo của bàn: [K5-L3A-DAY10-Nhom4Nam-PoCtoPilotGate1](https://github.com/duyanhtran2005/K5-L3A-DAY10-Nhom4Nam-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): `S6`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 | Trương Lợi Vĩ | 2A202603441| Kỹ sư cổng · cổng, checkpoint, kiểm thử S6 | |
|   3 | Trần Dương Trung Tính | 2A202603488 | Kỹ sư cổng · trace, kiểm thử, monitor | |
|   4 | Nguyễn Nhựt Linh | 2A202603492 | Vận hành và pháp lý | |
|   5 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## TruongLoiVi-2A202603441

### Phần việc phụ trách

Tôi phụ trách kỹ sư cổng: xây dựng và chốt ba cổng vòng 1 trong `lab10/guards.py`, xác nhận `config/operating_gates.json`, checkpoint `ec3a692b`, chạy baseline/prepared/gate và điền bằng chứng B0–B1, B7.1. Ở vòng 2, tôi sửa cổng S6 trong `lab10/guards.py`, ghép monitor của Tính vào `lab10/monitors.py`, kiểm regression bộ nền và bàn giao trace/report cho Phiếu C.

### Đóng góp cụ thể

- **Cổng vòng 1 và checkpoint.** Viết ba cổng dựa vào nguồn sự thật: ghim policy hiệu lực; tính lại khoản hoàn từ tracking và policy; chỉ ghi lỗi hãng khi kiện, hãng, tài xế và độ trễ khớp tracking. Chốt snapshot vòng 1 `ec3a692b`.
- **Đánh giá vòng 1.** Kiểm lại baseline `R-base-before-20261118-171311-d298f2`: pass_rate `0,9909`, pass_k `0,9545`, còn hoàn sai `20.000đ` và 1 lỗi hãng oan. Prepared `R-base-prepared-20261118-171319-d298f2` đạt pass_rate/pass_k `1,0`, hoàn sai/lỗi hãng oan/PII đều `0`, không có dòng vượt trần.
- **Sửa sự cố S6.** Thêm cổng chuyển người trước mọi thao tác ghi khi đơn nhiều kiện nhưng ticket không xác định kiện liên quan; thêm cổng không tự ghi lỗi hãng khi đã chạm trần lỗi tự động theo hãng/ngày. Hai cổng dùng quy tắc tổng quát, không nhắm ID ticket.
- **Kiểm chứng S6.** `S6-20@11` được chuyển người trước ghi; sổ cái, lỗi hãng và gửi hãng đều rỗng. `S6-42@11` vẫn hoàn đúng `22.000đ`, nhưng không tự ghi lỗi GHSH khi đã có 2 lỗi tự động trong ngày.
- **Phối hợp monitor và bàn giao.** Ghép `max_daily_carrier_faults` của Tính; monitor sáng đèn từ `1,0` trên bộ nền lên `2,0` sau sửa S6. Gửi report, trace và số liệu hàng chờ/lỗi hãng oan/PII cho Duy để hoàn thiện C8–C11.

**Sử dụng AI.** Tôi dùng AI để hỗ trợ đọc mã, kiểm tra logic guard, chạy lệnh, đối chiếu trace và biên tập bằng chứng. Tôi chịu trách nhiệm quyết định phạm vi cổng, kiểm tra kết quả và bàn giao mã run cho nhóm.

### Bằng chứng

- Commit `a996189`: cổng nguồn sự thật vòng 1.
- Commit `29e104d`: chia sẻ checkpoint vòng 1.
- Commit `60b84e5` trên nhánh `vi/round1-s6`: cổng S6 v2 và ghép monitor `max_daily_carrier_faults`.
- Baseline/prepared: `R-base-before-20261118-171311-d298f2` · `R-base-prepared-20261118-171319-d298f2`.
- S6 after/grade: `R-S6-after-20261118-172821-cd4e5a` · `R-S6-grade-20261118-172821-cd4e5a`.
- Phiếu B: B0–B1, B7.1. Phiếu C: bằng chứng cho C7, C8–C9 và C11.

### Exit ticket

Tôi rút ra rằng tracking là nguồn sự thật cần thiết nhưng chưa đủ để quy lỗi cho bên thứ ba khi ticket không xác định được kiện liên quan. Cổng phải chuyển người trước thao tác không đảo ngược; monitor giúp phát hiện khi lỗi tự động dồn tới ngưỡng. Tôi còn chưa chắc tải chuyển người trong pilot thật có luôn giữ được SLA 60 phút hay không.

## TranDuongTrungTinh-2A202603488

### Phần việc phụ trách

Tôi là kỹ sư cổng, phụ trách đọc trace, kiểm thử và theo dõi kết quả. Phần việc gồm soát A2 với Vĩ và A4 với Duy, điền B2 và B7.2–B7.3, phụ trách ca `S6-20@11` và đóng góp C2, C6, C8, C9.

### Đóng góp cụ thể

- **Soát tiêu chí và cách đo.** Rà cùng Vĩ cách đối chiếu lỗi hãng với nhãn ở A2, gồm bản ghi thực tế, ca chuyển người, mẫu số và điểm mù. Gửi Duy phần soát A4 về đơn vị, công thức và hành động khi vượt ngưỡng để Duy chốt tiêu chí của nhóm.
- **Dò lỗi nền và kiểm cổng vòng 1.** Dùng trace `T-002@55` ở B2 để xác định trợ lý lấy 5 ngày khách khai thay cho 2 ngày trong tracking, dẫn đến hoàn sai 20.000đ và ghi lỗi oan cho VNX. Nêu hai bước tránh chỉnh cổng theo chính bộ dùng để chấm ở B7.2. Chuẩn bị và đối chiếu hai ca B7.3 `O-1010@11` và `O-1004@55`. Cả hai không phát sinh bản ghi hoàn tiền, lỗi hãng hoặc thông báo hãng. Gửi bằng chứng và đề xuất kiểm cổng cho Vĩ, bàn giao kết quả cho Duy.
- **Phân tích và kiểm tra lại S6.** Phụ trách `S6-20@11`, ca đơn nhiều kiện thiếu mã kiện, và phối hợp với Vĩ, người phụ trách ca vượt trần lỗi hãng `S6-42@11`. Đối chiếu hai mốc và ghi kết quả vào C2, C6, C9. Ở mốc chuẩn bị, hệ thống tự chọn kiện trễ nhất rồi hoàn 26.000đ và ghi lỗi VNX. Sau khi Vĩ sửa cổng, dòng 02 cho thấy ticket được chuyển người trước khi ghi. Sổ cái, lỗi hãng và thông báo hãng đều rỗng.
- **Thiết kế và kiểm chứng monitor ở C8.** Phụ trách `max_daily_carrier_faults` trong `lab10/monitors.py`. Chỉ số đếm bản ghi theo ngày, seed và hãng rồi lấy số lớn nhất. Ngưỡng đỏ là trên 2 lỗi/hãng/ngày. Kết quả xác minh là 1 trên bộ nền, 4 trên S6 ở mốc chuẩn bị và 2 sau sửa. Bàn giao cho Duy công thức, ngưỡng, giá trị đo và các điểm còn hở.

**Sử dụng AI.** Tôi dùng AI để hỗ trợ đọc mã, soạn nháp monitor, chạy lệnh kiểm thử, đối chiếu trace và biên tập phiếu. Tôi phụ trách phạm vi kiểm thử, phối hợp với Vĩ và Duy, gửi kết quả và bàn giao bằng chứng cho nhóm.

### Bằng chứng

- Phiếu A mục A2 và A4, Phiếu B mục B2 và B7.2–B7.3, Phiếu C mục C2, C6, C8, C9.
- Commit Phiếu C `f854a6b` trên nhánh `tinh/s6`. Cổng S6 và phiên bản monitor đã ghép nằm trong commit `60b84e5` của Vĩ.
- Run xác minh `R-S6-after-20261118-224737-cd4e5a` và grade `R-S6-grade-20261118-224736-cd4e5a`. Bộ công khai, integrity, regression và monitor đều đạt. Chưa chạy test ẩn.

### Exit ticket

Điều rút ra là dữ liệu tracking có thể đúng nhưng vẫn chưa đủ để quy trách nhiệm khi ticket thiếu mã kiện. Cổng cần chuyển người trước khi ghi, còn monitor giúp phát hiện lỗi đã ghi vượt trần. Cần kiểm thêm tải chuyển duyệt với dữ liệu thực tế và việc cảnh báo có đến đúng người chịu trách nhiệm hay không.

## NguyenNhutLinh-2A202603492

### Phần việc phụ trách

Tôi phụ trách Vận hành và pháp lý: Phiếu A câu 1.2 và 1.4; Phiếu B mục B4–B5, B7.5–B7.6; Phiếu C mục C3.2, C4 và C11 cho thẻ S6.

### Đóng góp cụ thể

- **Mục tiêu và cách đo.** Viết mục tiêu của chị Oanh về đối soát khoản hoàn với sổ cái và của chị Hạnh về tiếp nhận ca chuyển duyệt trong 60 phút. Thiết kế cách đo tỷ lệ thông báo gửi hãng có dấu hiệu chứa dữ liệu người nhận, dựa trên payload sau lọc và hồ sơ người nhận, theo cửa sổ 24 giờ.
- **Rủi ro và runbook vòng 1.** Lập HAZOP cho `notify_carrier`, bổ sung rủi ro quá tải người duyệt và chia sẻ dữ liệu với bên thứ ba. Điền checklist 9 nhóm việc có PIC, trạng thái và nguồn bằng chứng. Viết runbook phần 1–3 và kịch bản giờ cao điểm theo cấu hình 1 người duyệt, 6 ca/giờ, SLA 60 phút và tỷ lệ kiểm mẫu 10%.
- **Phân tích sự cố S6.** So sánh cách điều phối hãng xác minh theo kiện và chặng với cách kế toán, CSKH đối soát. Dùng trace `base` của `S6-01@11` và `S6-20@11` để chỉ ra lỗi gán trách nhiệm cho kiện đầu và rủi ro khi thiếu mã kiện. Viết HAZOP S6, đề xuất chuyển người trước khi ghi nếu thiếu căn cứ, rồi cập nhật runbook phần 4–5 theo kết quả sau sửa.
- **Chốt và cập nhật C11 trên `main`.** Đối chiếu report cuối, ghi nhận thời gian chờ lâu nhất 0 phút và 0 ca ùn. Chạy lại `S6-01@11` ở mốc `after` trên bản khớp hash `cd4e5a0124cf`, xác nhận thông báo đi đúng VNX cho kiện `O-2601-P2` sau khi bỏ `customer_note`. Kiểm riêng hai công tắc dừng ghi lỗi và gửi hãng trong mô phỏng. Đánh dấu nhóm 8 `Xong` và giữ nhóm 7 `Chưa` vì chưa có xác nhận Tùng đã nhận được cảnh báo.

**Sử dụng AI.** Tôi dùng Codex để hỗ trợ đọc repo, đối chiếu số liệu và trace, chạy kiểm thử mô phỏng công tắc và biên tập các phiếu. Tôi rà lại nội dung và bàn giao bằng chứng cho nhóm.

### Bằng chứng

- Câu 1.2 và 1.4 trong [Phiếu A](templates/form-a-criteria.md); B4–B5, B7.5–B7.6 trong [Phiếu B](templates/form-b-evaluation-gates.md); C3.2, C4 và C11 trong [Phiếu C](templates/form-c-incident.md).
- Commit `306a4e6` trên nhánh `linh/s6-ops` lưu phần cập nhật Phiếu B và Phiếu C ở đợt trước.
- Bản chốt C11 trong [Phiếu C](templates/form-c-incident.md) trên nhánh `main`, đối chiếu với report `R-S6-grade-20261118-230042-cd4e5a`, trace `S6-01@11` và [bằng chứng kiểm thử công tắc](docs/C11-S6-verification.md).

### Exit ticket

Tôi học được rằng đơn nhiều kiện phải được đối chiếu theo từng kiện trước khi quy trách nhiệm cho hãng hoặc tài xế. Tôi còn chưa chắc cảnh báo sẽ đến đúng người trực trong thời hạn đề xuất, vì phép thử mới xác nhận công tắc hoạt động trong mô phỏng.
