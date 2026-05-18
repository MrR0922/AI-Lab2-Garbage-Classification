from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

# 1. 加载训练好的模型
model = YOLO('runs/classify/runs/classify/garbage_exp/weights/best.pt')

# 2. 对测试图片进行预测
img_path = 'test.jpg'  # 测试图片路径
results = model.predict(img_path, device='cuda')

# 3. 获取预测结果
result = results[0]
top1_class = result.names[result.probs.top1]
top1_conf = result.probs.top1conf.item()

print(f"预测类别: {top1_class}")
print(f"置信度: {top1_conf:.2%}")

# 4. 显示结果
img = Image.open(img_path)
plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.axis('off')
plt.title(f"预测类别: {top1_class}\n置信度: {top1_conf:.2%}", fontsize=14)
plt.tight_layout()
plt.savefig('result.jpg')
plt.show()

print("\n预测结果已保存到 result.jpg")
