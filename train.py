from ultralytics import YOLO

MODEL_PATH = "yolo11n.pt"
DATA_YAML = "data_3class.yaml"

EPOCHS = 100
IMG_SIZE = 640
BATCH_SIZE = -1
DEVICE = 0
WORKERS = 4
PATIENCE = 0

PROJECT_NAME = "kitchen_fire_3class_v5"

def main():
    print("=== 智能厨房安全助手 - YOLOv11 训练脚本（从头训练） ===")
    print(f"使用基础模型     : {MODEL_PATH}")
    print(f"数据集配置文件   : {DATA_YAML}")
    print(f"训练轮数 (Epochs) : {EPOCHS}")
    print(f"图像大小 (ImgSize): {IMG_SIZE}")
    print(f"Batch Size        : {BATCH_SIZE} (自动优化)")
    print(f"项目名称          : {PROJECT_NAME}")
    print("-" * 70)

    print("正在加载预训练模型...")
    model = YOLO(MODEL_PATH)

    print("开始训练，请耐心等待...\n")
    
    results = model.train(
        data=DATA_YAML,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        device=DEVICE,
        workers=WORKERS,
        patience=PATIENCE,
        name=PROJECT_NAME,
        amp=True,
        cache=True,
        project="runs/detect",
        exist_ok=True,
        seed=42,
        val=True
    )

    print("\n🎉 训练完成！")
    print(f"最佳模型路径: runs/detect/{PROJECT_NAME}/weights/best.pt")
    print(f"最后模型路径: runs/detect/{PROJECT_NAME}/weights/last.pt")
    print(f"详细结果可查看: runs/detect/{PROJECT_NAME}/results.csv")

if __name__ == "__main__":
    main()