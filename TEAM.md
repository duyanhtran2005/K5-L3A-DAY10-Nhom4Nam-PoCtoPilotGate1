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
|   2 |           |      |     |             |
|   3 | Trần Dương Trung Tính | 2A202603488 | Kỹ sư cổng · trace, kiểm thử, monitor | |
|   4 |           |      |     |             |
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
