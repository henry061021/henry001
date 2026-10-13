# 实验01：Python 基础与数据处理入门

- **学号**：2024408029
- **姓名**：何启恒
- **作业编号**：01（hw01）
- **实验名称**：实验01 Python 基础与数据处理入门

> 提交文件：`2024408029_何启恒_hw01.ipynb`

## 目录结构

```
.
├── 2024408029_何启恒_hw01.ipynb     # 作业 Notebook（已运行，含全部输出）
├── student_utils.py                 # parse_student() 模块（实验4-3 由 Notebook 生成）
├── README.md
└── exp01_data/                      # 实验数据与输出
    ├── students.txt                 # 原始数据文件
    ├── report.txt                   # 统计报告（w / a 模式演示结果）
    └── students.pkl                 # pickle 序列化数据
```

## 运行环境（conda 虚拟环境，不使用 base）

```bash
conda create -n exp01 python=3.11 -y
conda activate exp01
pip install jupyter
jupyter notebook
```

打开 Notebook 后，将内核切换为 `exp01`，执行 **Restart Kernel → Run All**，即可复现全部结果。

## 实验内容

| 实验 | 主题 | 主要知识点 |
| --- | --- | --- |
| 实验1 | 基本运算、数据类型与字符串 | `/ // % **`、`type()`、类型转换与 `ValueError`、字符串处理、字符串不可变性 |
| 实验2 | 函数、条件、循环与递归 | 参数校验、`for`/`while`、递归与迭代、元组返回与解包、`*args` |
| 实验3 | 列表、字典、元组与基础统计 | `zip`/`dict`/`items`、`enumerate`、列表推导式、格式化、别名与 `copy()` |
| 实验4 | 文件读写、异常处理与模块 | `os` 路径、文件读写、`w`/`a` 模式、异常捕获、`pickle`、自定义模块 |
| 实验5 | 类、继承与对象复制 | 类与 `__init__`、`__str__`、继承与 `super()`、`copy` 与 `deepcopy` |

全部单元格已按顺序运行通过，未出现报错。
