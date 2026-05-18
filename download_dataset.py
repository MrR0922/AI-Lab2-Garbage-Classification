import os
import zipfile
import requests
from tqdm import tqdm

def download_file(url, filename):
    """下载文件并显示进度条"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

def download_garbage_dataset():
    """下载垃圾分类数据集"""
    print("准备下载垃圾分类数据集...")

    # Kaggle数据集链接（需要先配置Kaggle API）
    dataset_url = "https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification"

    print("\n请按以下步骤下载数据集：")
    print("1. 访问: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification")
    print("2. 点击 'Download' 按钮下载数据集")
    print("3. 解压下载的zip文件到当前目录")
    print("4. 确保文件夹结构为:")
    print("   garbage-classification/")
    print("   ├── cardboard/")
    print("   ├── glass/")
    print("   ├── metal/")
    print("   ├── paper/")
    print("   ├── plastic/")
    print("   └── trash/")
    print("\n或者使用Kaggle API:")
    print("pip install kaggle")
    print("kaggle datasets download -d asdasdasasdas/garbage-classification")
    print("unzip garbage-classification.zip")

if __name__ == "__main__":
    download_garbage_dataset()
