# 垃圾分类实验 - YOLO v11

使用YOLO v11进行垃圾图像分类

## 环境要求

- Python 3.8+
- PyTorch (已安装)
- CUDA (GPU支持)
- ultralytics

## 安装依赖

```bash
pip install ultralytics matplotlib pillow requests tqdm
```

## 数据集准备

### 方法1: 手动下载
1. 访问 https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification
2. 下载数据集并解压到当前目录
3. 确保文件夹结构为 `garbage-classification/`

### 方法2: 使用Kaggle API
```bash
pip install kaggle
kaggle datasets download -d asdasdasasdas/garbage-classification
unzip garbage-classification.zip
```

## 数据集结构

```
garbage-classification/
├── cardboard/  # 纸板
├── glass/      # 玻璃
├── metal/      # 金属
├── paper/      # 纸张
├── plastic/    # 塑料
└── trash/      # 垃圾
```

## 使用方法

### 1. 训练模型
```bash
python train.py
```

训练参数：
- 训练轮数: 10 epochs
- 图像大小: 128x128
- 批次大小: 16
- 设备: GPU (自动检测)

### 2. 预测分类
```bash
python predict.py
```

确保有测试图片 `test.jpg` 在当前目录

## 输出文件

- `runs/classify/garbage_exp/weights/best.pt` - 最佳模型
- `result.jpg` - 预测结果图片
- `runs/classify/garbage_exp/` - 训练日志和图表

## YOLO v11 vs MobileNetV2

| 特性 | YOLO v11 | MobileNetV2 |
|------|----------|-------------|
| 训练速度 | 更快 | 较慢 |
| 准确率 | 更高 | 较高 |
| 易用性 | 非常简单 | 需要更多代码 |
| 功能 | 分类+检测 | 仅分类 |
