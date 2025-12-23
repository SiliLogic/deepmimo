# 基于 DeepMIMO 的无线信道处理与分析代码

## 📌 项目简介

本项目包含一系列 **基于 DeepMIMO 数据集的 Python 脚本**，用于无线信道数据的：

* 场景加载与预处理
* 信道生成与参数计算
* 多普勒效应与移动性分析
* 数据可视化与结果展示

该代码库主要面向 **科研实验与算法验证场景**，在设计上优先考虑：

* 数据访问的简洁性
* 实验过程的可复现性
* 快速迭代与分析效率

---

## 📁 目录结构说明

```
deepmimo/
├─ deepmimo_scenarios/      # DeepMIMO 场景数据（数据集，不纳入 Git 管理）
│
├─ download/                # 与数据下载、准备相关的脚本（逻辑分类）
├─ generate/                # 信道生成与预处理相关逻辑
├─ search/                  # 场景筛选与搜索相关工具
├─ visualize/               # 可视化与绘图相关脚本
│
├─ channel_gen.py
├─ dataset_core.py
├─ load_dataset.py
├─ doppler_dir.py
├─ doppler_v.py
├─ vis_scene_visual.py
├─ ...
│
├─ .gitignore
└─ README.md
```

---

## 📐 目录设计说明（Design Rationale）

### 为什么大部分 Python 文件位于项目根目录？

本项目中的大多数 Python 脚本 **需要直接访问 DeepMIMO 场景数据**，数据统一存放于：

```
deepmimo_scenarios/
```

为了实现以下目标：

* **数据集只保留一份，避免重复拷贝**
* 使用 **简单、稳定的相对路径** 加载数据
* 减少对运行路径（working directory）的依赖
* 方便快速实验与脚本调试

所有核心 Python 脚本被放置在与数据目录 **同一层级**。

> `download / generate / search / visualize` 等文件夹主要用于
> **功能上的逻辑分类与代码阅读提示**，而非 Python 模块或包结构。

该设计更适合 **科研实验阶段**，在后续工程化需求增强时可进一步重构。

---

## 📦 数据集说明

本项目基于 **DeepMIMO 数据集**。

* 数据集存放路径：

  ```
  deepmimo_scenarios/
  ```
  
* 所有数据文件（如 `.mat`）均通过 `.gitignore` 排除，不纳入版本管理
* 使用者需自行下载或生成 DeepMIMO 场景数据

📎 **DeepMIMO 官方网站**：
[TODO：填写 DeepMIMO 官方链接]

---

## ▶️ 使用方法

### 1️⃣ 准备数据集

将下载或生成的 DeepMIMO 场景文件放置于：

```
deepmimo_scenarios/
```

示例结构：

```
deepmimo_scenarios/
├─ scenario_1/
├─ scenario_2/
└─ ...
```

---

### 2️⃣ 运行脚本

在项目根目录下执行对应脚本，例如：

```bash
python channel_gen.py
```

或：

```bash
python vis_scene_visual.py
```

⚠️ 请确保 **当前工作目录为 `deepmimo/`**，以保证相对路径正确。

---

## 🧪 实验说明

* 本代码库主要用于 **研究与实验用途**
* 脚本接口可能会随着实验需求不断调整
* 实验中产生的中间数据与结果文件不纳入版本管理

---

## 🧰 运行环境与依赖

常用依赖包括：

* Python ≥ [TODO: 版本号]
* NumPy
* SciPy
* Matplotlib
* [TODO：其他依赖库]

如有需要，可通过以下方式安装依赖：

```bash
pip install -r requirements.txt
```

（如未提供，可自行配置环境）

---

## 🔁 可复现性说明

复现实验的一般流程如下：

1. 克隆本仓库
2. 准备 DeepMIMO 数据集至 `deepmimo_scenarios/`
3. 在项目根目录下运行对应脚本

---

## 📄 许可证（License）

[TODO：选择合适的许可证，例如 MIT License]

---

## ✍️ 作者与说明

* 作者：**SiliLogic**
* 本仓库主要用于 **个人科研学习与实验验证**
* 随着项目成熟，代码结构可能进行进一步工程化整理

---

## 🔮 后续计划（可选）

* 将代码重构为模块化 Python 包
* 引入统一的路径与配置管理
* 提供命令行接口（CLI）
* 构建自动化实验流程

---
