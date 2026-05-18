from ultralytics import YOLO
import torch

if __name__ == '__main__':
    # 检查GPU是否可用
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"使用设备: {device}")

    # 1. 加载预训练的YOLO v11模型
    model = YOLO('yolo11n-cls.pt')  # n=nano, 轻量级分类模型

    # 2. 训练模型
    results = model.train(
        data='garbage-classification',  # 数据集路径
        epochs=30,                       # 训练轮数（提升至30）
        imgsz=224,                       # 图像大小（提升至224，保留更多细节）
        batch=16,                        # 批次大小
        device=device,                   # 使用GPU/CPU
        project='runs/classify',         # 保存路径
        name='garbage_exp_v2',           # 新实验名称
        patience=10,                     # 早停耐心值
        save=True,                       # 保存最佳模型
        plots=True                       # 生成训练图表
    )

    print("\n训练完成！")
    print(f"最佳模型保存在: runs/classify/garbage_exp_v2/weights/best.pt")
