# CarVision AI

Dự án nhận diện hãng/dòng xe từ ảnh, sau đó tra cứu thông số kỹ thuật có dẫn nguồn.

## Ý tưởng
- Người dùng tải ảnh xe, hệ thống đưa ra các dự đoán hãng/dòng xe phù hợp.
- Người dùng xác nhận dự đoán và chọn phiên bản xe trước khi xem thông số
  (vì chỉ nhìn ảnh khó xác định chính xác đời xe hay động cơ).
- Thông số hiển thị kèm nguồn dẫn chứng.

## Trạng thái (tuần 1)
Đang ở giai đoạn lập kế hoạch. Chưa huấn luyện mô hình, chưa có kết quả thực nghiệm.
Mọi nội dung về mô hình và giao diện là hướng dự kiến.

## Dự kiến
- 10–15 nhóm xe (số cuối cùng phụ thuộc dữ liệu thực tế)
- Nguồn dữ liệu ứng viên: Stanford Cars
- So sánh CNN tự xây với MobileNetV2, sau đó đánh giá tác động của tăng cường dữ liệu

## Thành viên
- Phan Lê Phương Nam
- Trần Võ Bá Vương
- Lê Văn Công Nguyên
- Lê Hoàng Triều

## Quy ước làm việc
- `main` luôn ổn định, mỗi người làm trên nhánh riêng
  (`nam/...`, `vuong/...`, `nguyen/...`, `trieu/...`).
- Gộp vào `main` bằng Pull Request, có ít nhất 1 người xem.
- Không đẩy ảnh dataset hay file trọng số lên Git.