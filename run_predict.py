from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

model = YOLO('runs/classify/runs/classify/garbage_exp/weights/best.pt')

test_dir = 'test'
output_dir = 'SZU-Lab-Report-LaTeX-2.0/SZU-Lab-Report-LaTeX'

img_files = [f for f in os.listdir(test_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
print(f"找到 {len(img_files)} 张测试图片: {img_files}")

for i, fname in enumerate(img_files, 1):
    img_path = os.path.join(test_dir, fname)
    results = model.predict(img_path, device='cpu', verbose=False)
    result = results[0]

    top5_classes = [result.names[idx] for idx in result.probs.top5]
    top5_confs = result.probs.top5conf.tolist()

    print(f"\n图片 {i}: {fname}")
    for cls, conf in zip(top5_classes, top5_confs):
        print(f"  {cls}: {conf:.2%}")

    img = Image.open(img_path)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].imshow(img)
    axes[0].axis('off')
    axes[0].set_title('原始图片', fontsize=13)

    bars = axes[1].barh(top5_classes[::-1], [c * 100 for c in top5_confs[::-1]],
                        color=['#e74c3c' if j == 4 else '#3498db' for j in range(5)])
    axes[1].set_xlabel('置信度 (%)', fontsize=11)
    axes[1].set_title(f'Top-5 预测结果\n最高: {top5_classes[0]} ({top5_confs[0]:.1%})', fontsize=12)
    axes[1].set_xlim(0, 100)
    for bar, conf in zip(bars, [c * 100 for c in top5_confs[::-1]]):
        axes[1].text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                     f'{conf:.1f}%', va='center', fontsize=10)

    plt.tight_layout()
    out_name = f'result_{i}.png'
    plt.savefig(os.path.join(output_dir, out_name), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  已保存: {out_name}")

print("\n所有预测结果已保存。")
