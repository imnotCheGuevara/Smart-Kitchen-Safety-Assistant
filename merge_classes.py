
import os
import shutil
from pathlib import Path
from collections import defaultdict

# ================== 修改这里 ==================
project_root = Path(r"C:\Users\杨4\Desktop\Smart Kitchen Safety Assistant")
original_dataset = project_root / "fire_detection"          

# 【重要】请把下面这行改成你 Roboflow 解压后的真实路径
roboflow_nonfire_path = Path(r"C:\Users\杨4\Desktop\Smart Kitchen Safety Assistant\nonfiredataset")   # ←←← 这里一定要改成正确的路径！
# =============================================

dataset_root = project_root / "fire_detection"
dataset_root.mkdir(exist_ok=True)
def merge_original_labels(label_path: Path):
    """把原始4类合并为3类：fire=0, non_fire=1, smoke=2"""
    if not label_path.exists():
        return []
    
    new_lines = []
    with open(label_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 5:
                continue
            class_id = int(parts[0])
            
            if class_id == 0:        # fire
                new_class = 0
            elif class_id == 3:      # smoke
                new_class = 2
            elif class_id in [1, 2]: # light + nonfire → non_fire
                new_class = 1
            else:
                continue
            
            new_line = f"{new_class} {' '.join(parts[1:])}"
            new_lines.append(new_line)
    return new_lines

print("=== 开始合并数据集为 3 类（fire, non_fire, smoke）===")

# 创建标准文件夹结构
for split in ['train', 'valid', 'test']:
    (dataset_root / split / 'images').mkdir(parents=True, exist_ok=True)
    (dataset_root / split / 'labels').mkdir(parents=True, exist_ok=True)

class_count = defaultdict(int)

# 第一步：处理原始 Iron Wolf 数据集
for split in ['train', 'valid', 'test']:
    src_images = original_dataset / split / 'images'
    src_labels = original_dataset / split / 'labels'
    
    if not src_images.exists():
        print(f"警告：未找到 {split} 文件夹")
        continue
    
    print(f"正在处理原始数据集 {split} ...")
    for img_file in src_images.glob("*.jpg"):
        label_file = src_labels / (img_file.stem + ".txt")
        
        dst_img = dataset_root / split / 'images' / img_file.name
        dst_label = dataset_root / split / 'labels' / (img_file.stem + ".txt")
        
        shutil.copy2(img_file, dst_img)
        
        new_lines = merge_original_labels(label_file)
        if new_lines:
            with open(dst_label, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines) + '\n')
            
            for line in new_lines:
                cls = int(line.split()[0])
                class_count[f"original_{split}_{cls}"] += 1

print("原始数据集处理完成！")

# 第二步：添加 Roboflow 的 non_fire 数据（全部放到 train）
print(f"正在添加 Roboflow non_fire 数据（538 张）...")

rf_images_dir = roboflow_nonfire_path / "train" / "images"   # Roboflow 导出通常是 train 结构
rf_labels_dir = roboflow_nonfire_path / "train" / "labels"

if not rf_images_dir.exists():
    rf_images_dir = roboflow_nonfire_path / "images"   # 兼容不同导出结构
    rf_labels_dir = roboflow_nonfire_path / "labels"

added_count = 0
for img_file in rf_images_dir.glob("*.jpg"):
    label_file = rf_labels_dir / (img_file.stem + ".txt")
    
    dst_img = dataset_root / "train" / "images" / f"rf_nonfire_{img_file.name}"
    dst_label = dataset_root / "train" / "labels" / f"rf_nonfire_{img_file.stem}.txt"
    
    shutil.copy2(img_file, dst_img)
    
    # Roboflow 的 non_fire 类通常是 class 0，我们改为我们的 non_fire=1
    if label_file.exists():
        with open(label_file, 'r') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:
                new_lines.append(f"1 {' '.join(parts[1:])}")  # 改为 non_fire class 1
        with open(dst_label, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines) + '\n')
    
    class_count["added_non_fire"] += 1
    added_count += 1

print(f"已添加 {added_count} 张 Roboflow non_fire 图片到 train 集")

# 生成 data_3class.yaml
yaml_path = dataset_root / "data_3class.yaml"
with open(yaml_path, 'w', encoding='utf-8') as f:
    f.write(f"""path: {dataset_root.as_posix()}

train: train/images
val: valid/images
test: test/images

nc: 3
names: ['fire', 'non_fire', 'smoke']
""")

print("\n=== 合并完成！===")
print(f"最终数据集位置：{dataset_root}")
print(f"生成的配置文件：{yaml_path}")

print("\n各类样本统计：")
for k, v in class_count.items():
    print(f"  {k}: {v}")

print("\n现在你可以开始训练了！推荐命令：")
print(f'yolo detect train model=yolo11n.pt data="{yaml_path}" epochs=50 imgsz=640 batch=8 device=0 name=kitchen_fire_3class patience=0 task=detect workers=0')