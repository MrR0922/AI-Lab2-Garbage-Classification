# SZU-Lab-Report-LaTeX-Template
深圳大学学生实验报告 LaTeX 模版 (电子与信息工程学院规范版)

## 📋 项目简介
本项目为深圳大学学生提供一套规范、美观且易于使用的实验报告 LaTeX 模版。针对电信学院实验报告的常见排版需求进行了像素级优化，解决了传统 Word 模版对齐难、公式排版丑等痛点。

## 🚀 使用指南
### 1. 环境准备
* 推荐使用 [Overleaf](https://www.overleaf.com/) 或本地安装 [TeX Live](https://www.tug.org/texlive/)。
* **重要**：请务必使用 **XeLaTeX** 编译器以支持中文字体。

### 2. 快速开始
1. 下载 `szu_lab_report.tex` 文件。
2. 在 `tabular` 环境中填写你的课程名称、学号、姓名等信息。
3. 若需在数据处理页添加一整页方框，请调用：
   ```latex
   \myfullpagebox