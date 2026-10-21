# Cấu trúc GitHub và luồng ứng dụng (Lê Hoàng Triều)

## Cấu trúc repo
Gồm các thư mục: data, notebooks, src, app, docs, results. Chi tiết xem README.md.

## Quy ước làm việc nhóm
- main được bảo vệ, mỗi người làm trên nhánh riêng
  (nam/..., vuong/..., nguyen/..., trieu/...).
- Gộp vào main bằng Pull Request, có ít nhất 1 người duyệt.
- Không đẩy ảnh dataset hay file trọng số lên Git.

## Luồng ứng dụng (dự kiến)
1. Người dùng tải ảnh xe lên.
2. Mô hình đưa ra vài dự đoán hãng/dòng xe kèm độ tin cậy.
3. Người dùng xác nhận kết quả đúng, hoặc báo không có kết quả nào đúng.
4. Người dùng chọn đời xe, động cơ, phiên bản.
5. Hệ thống hiển thị thông số kèm nguồn dẫn chứng.
6. Trường hợp lỗi: ảnh không phải xe, độ tin cậy thấp, hoặc xe ngoài phạm vi
   thì thông báo rõ thay vì đoán bừa.

## Cần thống nhất với nhóm
- Framework: TensorFlow hay PyTorch
- Công cụ giao diện: Streamlit hay Gradio
- Định dạng lưu thông số kèm nguồn (JSON/CSV)

## Lưu ý
Nhóm chưa huấn luyện mô hình và chưa có kết quả thực nghiệm.
Phần mô hình và giao diện là hướng dự kiến.