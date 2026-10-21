"""
Explore and inspect Stanford Cars dataset via Hugging Face.

Features:
- Prints distribution summary (Makes, Body Types, Years) across all 196 classes.
- Displays curated 12-class subset for Vietnam market PoC.
- Streams real sample images for the selected classes and optionally saves a preview grid.

Usage:
    python src/data/explore_dataset.py --summary
    python src/data/explore_dataset.py --download-samples --max-per-class 1
"""

import os
import sys
import argparse
from typing import Dict, List
import pandas as pd

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from src.data.stanford_cars_classes import (
    STANFORD_CARS_CLASSES,
    SELECTED_VN_CLASSES,
    parse_class_name,
)

def print_dataset_summary() -> None:
    """Analyze and print structural distribution of Stanford Cars 196 classes."""
    parsed_items = [parse_class_name(name) for name in STANFORD_CARS_CLASSES]
    df = pd.DataFrame(parsed_items)
    
    print("=" * 70)
    print("STANFORD CARS DATASET - TỔNG QUAN 196 LỚP")
    print("=" * 70)
    print(f"Tổng số phân lớp (fine-grained classes): {len(STANFORD_CARS_CLASSES)}")
    print(f"Tổng số hãng xe (Makes): {df['make'].nunique()}")
    print("\nTop 10 hãng có nhiều dòng xe nhất trong bộ dữ liệu:")
    print(df['make'].value_counts().head(10).to_string())
    
    print("\nPhân bố theo kiểu dáng xe (Body Type):")
    print(df['body_type'].value_counts().to_string())
    
    print("\nPhân bố theo năm sản xuất (Year):")
    print(f"Năm sớm nhất: {df['year'].min()} - Năm muộn nhất: {df['year'].max()}")
    print(df['year'].value_counts().sort_index(ascending=False).head(5).to_string())
    
    print("\n" + "=" * 70)
    print("12 NHÓM XE ĐƯỢC CHỌN CHO PHẠM VI VIỆT NAM (POC GIAI ĐOẠN 1):")
    print("=" * 70)
    for idx, info in SELECTED_VN_CLASSES.items():
        print(f"[{idx:3d}] {info['raw_name']}")
        print(f"      Phân khúc: {info['segment']} | Đời/bản: {', '.join(info['vn_generations'])}")
        print(f"      Thực tế VN: {info['vn_popularity']}")
    print("=" * 70)

def download_and_save_samples(output_dir: str = "results/sample_previews", max_per_class: int = 1) -> None:
    """
    Streams a few images for the 12 selected classes using Hugging Face datasets streaming
    without downloading the entire 16,000+ images.
    """
    from datasets import load_dataset
    from PIL import Image, ImageDraw, ImageFont

    os.makedirs(output_dir, exist_ok=True)
    print(f"\n[+] Đang kết nối Hugging Face 'tanganke/stanford_cars' ở chế độ Streaming...")
    
    dataset = load_dataset("tanganke/stanford_cars", split="train", streaming=True)
    
    counts: Dict[int, int] = {idx: 0 for idx in SELECTED_VN_CLASSES.keys()}
    saved_samples: List[Dict] = []
    
    print(f"[+] Đang lọc và lấy mẫu {max_per_class} ảnh cho mỗi nhóm xe...")
    
    for row in dataset:
        lbl = row["label"]
        if lbl in counts and counts[lbl] < max_per_class:
            img = row["image"]
            class_info = SELECTED_VN_CLASSES[lbl]
            
            # Format filename
            safe_name = class_info["raw_name"].replace(" ", "_").replace("/", "-")
            save_path = os.path.join(output_dir, f"class_{lbl}_{safe_name}.jpg")
            
            # Save raw image
            img.convert("RGB").save(save_path, quality=90)
            counts[lbl] += 1
            saved_samples.append({
                "label": lbl,
                "name": class_info["raw_name"],
                "path": save_path,
                "image": img
            })
            print(f"  -> Đã lưu ảnh mẫu lớp [{lbl}] {class_info['raw_name']} -> {save_path}")
            
            # Stop early if we have all needed classes
            if all(c >= max_per_class for c in counts.values()):
                break
                
    print(f"\n[✓] Hoàn tất! Đã lưu {len(saved_samples)} ảnh mẫu vào thư mục '{output_dir}'.")

def main():
    parser = argparse.ArgumentParser(description="Khảo sát dữ liệu Stanford Cars cho CarVision AI")
    parser.add_argument("--summary", action="store_true", default=True, help="Hiển thị thống kê phân bố 196 lớp")
    parser.add_argument("--download-samples", action="store_true", help="Lấy ảnh mẫu các lớp chọn lọc qua HF streaming")
    parser.add_argument("--max-per-class", type=int, default=1, help="Số lượng ảnh mẫu cần lấy cho mỗi lớp")
    
    args = parser.parse_args()
    
    print_dataset_summary()
    
    if args.download_samples:
        download_and_save_samples(max_per_class=args.max_per_class)

if __name__ == "__main__":
    main()
