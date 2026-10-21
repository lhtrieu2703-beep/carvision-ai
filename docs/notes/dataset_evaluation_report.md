# Báo Cáo Đánh Giá Bộ Dữ Liệu: Stanford Cars vs. CompCars
**Dự án:** CarVision AI  
**Người lập:** Lê Hoàng Triều (`trieu/dataset-exploration`)  
**Ngày:** 22/10/2026 (Tuần 1)  

---

## 1. Đặt vấn đề
Hệ thống CarVision AI có mục tiêu nhận diện hãng/dòng xe từ hình ảnh, sau đó cho phép người dùng xác nhận và chọn phiên bản để tra cứu thông số kỹ thuật (specs) kèm đường dẫn chứng minh nguồn gốc.

Để bắt đầu giai đoạn huấn luyện và thử nghiệm trong tuần 1–2, nhóm cần một tập dữ liệu ảnh xe có gán nhãn chi tiết. Hai ứng viên tiêu biểu được đưa ra xem xét là:
1. **Stanford Cars** (Hugging Face / TFDS `cars196`)
2. **CompCars** (The Comprehensive Cars Dataset - MMLab CUHK)

---

## 2. Bảng so sánh chi tiết

| Tiêu chí | Stanford Cars (`tanganke/stanford_cars`) | CompCars (MMLab CUHK) |
| :--- | :--- | :--- |
| **Số lượng ảnh** | 16.185 ảnh (8.144 train / 8.041 test) | 136.726 ảnh web + 50.000 ảnh camera giám sát |
| **Số phân lớp** | 196 lớp (fine-grained: hãng + dòng + dáng + năm) | 163 hãng, 1.716 dòng xe |
| **Độ chi tiết nhãn** | `[Hãng] [Dòng] [Kiểu dáng] [Năm]`<br>Ví dụ: `Toyota Camry Sedan 2012` | Hãng $\rightarrow$ Dòng $\rightarrow$ Đời $\rightarrow$ Góc chụp $\rightarrow$ Bounding box |
| **Thuộc tính kỹ thuật (Specs)** | Không có sẵn (chỉ có nhãn tên xe) | **Có sẵn 5 thuộc tính**: Tốc độ tối đa, Dung tích xi-lanh, Số cửa, Số ghế, Kiểu dáng xe |
| **Quy trình tải & tích hợp** | **Cực nhanh & nhẹ**: Hỗ trợ streaming trực tiếp qua Hugging Face `datasets`, không tốn dung lượng ổ cứng | **Phức tạp & nặng**: Phải tải 23 file nén (`data.zip`, `data.z01`–`z22`) từ GDrive/Dropbox, giải nén bằng mật khẩu |
| **Bản quyền & Sử dụng web** | Dùng cho mục đích học thuật / nghiên cứu | Chỉ dùng cho nghiên cứu phi thương mại, **nghiêm cấm phân phối lại ảnh lên website công khai** |

---

## 3. Đánh giá về độ phủ xe tại thị trường Việt Nam

| Bộ dữ liệu | Ưu điểm tại VN | Hạn chế lớn |
| :--- | :--- | :--- |
| **Stanford Cars** | Chứa nhiều dòng xe toàn cầu quen thuộc: Camry, Corolla Altis, Accord, Sonata, Accent, Tucson, Santa Fe, Ranger, C-Class, 3-Series. | Dữ liệu dừng ở năm 2012. **Hoàn toàn không có VinFast**, thiếu các xe đặc trưng Đông Nam Á (Mitsubishi Xpander, Toyota Vios, Hyundai Grand i10). |
| **CompCars** | Độ phủ các hãng châu Á (Toyota, Honda, Hyundai, Kia, Mazda, Ford) dày đặc và đa dạng đời xe hơn. | Vẫn là dữ liệu Trung Quốc/quốc tế, không có VinFast. Dung lượng quá lớn để bắt đầu ở tuần 1. |

---

## 4. Quyết định & Đề xuất hành động cho nhóm

### Giai đoạn 1 (Tuần 1 - 2): Dùng Stanford Cars làm tập PoC (12 nhóm xe)
Không cần tải toàn bộ 16.185 ảnh. Nhóm tập trung vào **12 nhóm xe tiêu biểu** đại diện cho các phân khúc phổ biến tại Việt Nam:

1. **Toyota Camry Sedan 2012** (Label 186) - Sedan hạng D
2. **Toyota Corolla Sedan 2012** (Label 187) - Sedan hạng C (Corolla Altis)
3. **Honda Accord Sedan 2012** (Label 128) - Sedan hạng D
4. **Hyundai Accent Sedan 2012** (Label 135) - Sedan hạng B
5. **Hyundai Sonata Sedan 2012** (Label 137) - Sedan hạng D
6. **Hyundai Santa Fe SUV 2012** (Label 130) - SUV 7 chỗ
7. **Hyundai Tucson SUV 2012** (Label 131) - Crossover 5 chỗ
8. **Ford Ranger SuperCab 2011** (Label 110) - Bán tải (Pickup)
9. **Ford Fiesta Sedan 2012** (Label 116) - Sedan/Hatchback cỡ nhỏ
10. **BMW 3 Series Sedan 2012** (Label 28) - Sedan hạng sang
11. **Mercedes-Benz C-Class Sedan 2012** (Label 161) - Sedan hạng sang
12. **Volkswagen Golf Hatchback 2012** (Label 189) - Hatchback

### Giai đoạn 2: Tận dụng CompCars cho Module Thông số kỹ thuật (Specs)
- Tham khảo schema thuộc tính xe của CompCars để thiết kế file `app/specs/car_specs.json` chuẩn hóa (Công suất, động cơ, kích thước, tiêu hao nhiên liệu, URL dẫn chứng chính hãng).

### Giai đoạn 3 (Nâng cao): Bộ Test dữ liệu xe Việt Nam
- Tự thu thập tập ảnh nhỏ (khoảng 30–50 ảnh/loại) chụp thực tế tại Việt Nam:
  - **VinFast VF8 / VF5** (Xe điện thế hệ mới)
  - **Toyota Vios** (Sedan quốc dân)
  - **Mitsubishi Xpander** (MPV 7 chỗ bán chạy nhất)
- Đánh giá khả năng chuyển giao (transferability) của mô hình sang các dòng xe thực tế tại VN.

---

## 5. Hướng dẫn sử dụng công cụ đã xây dựng

1. **Xem thống kê phân bố 196 lớp:**
   ```bash
   python src/data/explore_dataset.py --summary
   ```
2. **Tải/lấy mẫu ảnh của 12 lớp chọn lọc qua stream:**
   ```bash
   python src/data/explore_dataset.py --download-samples --max-per-class 1
   ```
3. **Mở Jupyter Notebook khảo sát:**
   Mở file [`notebooks/01_stanford_cars_exploration.ipynb`](file:///d:/carvision-ai/notebooks/01_stanford_cars_exploration.ipynb).
