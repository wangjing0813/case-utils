我来给你详细的操作步骤，按照周五到周日的学习计划：

---

## **周五：周总结**

### 1. 创建思维导图（XMind）

```bash
# 如果没有XMind，安装
# Ubuntu/Debian:
sudo snap install xmind

# 或者下载：https://www.xmind.cn/

# 创建思维导图文件
xmind case_utils_weekly_summary.xmind
```

**思维导图结构：**
```
本周学习
├── Git基础
│   ├── add/commit/push - 基本操作
│   ├── 分支操作 - git branch, checkout, merge
│   ├── 子模块 - git submodule
│   └── 冲突解决 - git merge, rebase
├── Python项目
│   ├── setup.py - 项目配置
│   ├── 包管理 - pip, requirements.txt
│   ├── 虚拟环境 - venv, conda
│   └── 项目结构 - __init__.py, 模块组织
└── 协作工具
    ├── GitHub - 仓库管理, PR, Issue
    ├── PlantUML - 代码绘图
    ├── Mermaid - GitHub原生图表
    └── README编写 - 文档规范
```

### 2. 写周小结（500字）

```bash
# 创建周总结文档
mkdir -p docs/weekly
cat > docs/weekly/week1_summary.md << 'EOF'
# 第一周学习总结

## 本周我学会了：

### 1. Git的基本操作
- **解决了代码版本管理问题**
- 学会了 `git add/commit/push` 工作流
- 掌握了分支操作：`git branch`, `git checkout`, `git merge`
- 理解了子模块：`git submodule add` 用于数据管理

### 2. Python包结构
- **知道了如何组织代码**
- 创建了标准的包结构：`case_utils/`
- 编写了 `setup.py` 和 `requirements.txt`
- 学会了虚拟环境管理依赖

### 3. 团队协作工具
- **学会了用GitHub协作**
- 创建和维护README文档
- 使用Mermaid绘制工作流图
- 理解了Pull Request流程

## 遇到的问题：

### Git冲突不知道怎么解决
**问题**：多人协作时出现合并冲突
**解决**：学习使用 `git merge` 和 `git status` 查看冲突
**收获**：现在能独立解决大部分Git冲突

### Python包安装失败
**问题**：依赖包冲突，环境混乱
**解决**：学会了使用虚拟环境 `python -m venv .venv`
**收获**：项目隔离，依赖管理更清晰

### README格式混乱
**问题**：Markdown语法错误，图表不显示
**解决**：学习Mermaid语法，GitHub原生支持
**收获**：文档更专业，协作更顺畅

## 下周计划：

### 技术目标
- **学习机器数据处理**：pandas高级操作，数据清洗
- **完成一个小项目**：基于case_utils的数据分析工具
- **掌握测试框架**：pytest，单元测试

### 能力提升
- 提高代码质量：添加类型注解，文档字符串
- 学习CI/CD：GitHub Actions自动化测试
- 数据可视化：matplotlib，seaborn

## 本周收获总结：

通过一周的学习，我从零基础掌握了：
1. **版本控制**：能独立管理代码版本
2. **项目组织**：规范的Python包结构
3. **协作能力**：GitHub工作流程
4. **文档编写**：专业的README和图表

最重要的是建立了**持续学习**的习惯，遇到问题先查文档，再寻求帮助。每完成一个功能就提交代码，保持代码库的整洁和可追溯性。
EOF
```

### 3. 版本标记

```bash
# 查看当前状态
git status
git log --oneline -5

# 创建版本标签
git tag v0.1.0 -m "第一周完成 - Git基础和项目结构"

# 推送标签到GitHub
git push origin v0.1.0

# 查看所有标签
git tag -l

# 验证标签
git show v0.1.0
```

---

## **周六：Python 进阶**

### 1. 创建命令行入口

```bash
# 创建命令行入口文件
cat > case_utils/cli.py << 'EOF'
#!/usr/bin/env python3
"""
case-utils 命令行入口
"""

import argparse
import sys
from .monitor import Monitor
from .utils import process_data


def create_parser():
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        description="case-utils - 实用工具包",
        prog="case-utils"
    )
    
    # 添加子命令
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # monitor 命令
    monitor_parser = subparsers.add_parser('monitor', help='启动监控')
    monitor_parser.add_argument('--interval', type=int, default=5, 
                               help='监控间隔（秒）')
    
    # process 命令
    process_parser = subparsers.add_parser('process', help='处理数据')
    process_parser.add_argument('--input', required=True, help='输入文件')
    process_parser.add_argument('--output', help='输出文件')
    
    # demo 命令
    demo_parser = subparsers.add_parser('demo', help='运行演示')
    
    return parser


def main():
    """主函数"""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command == 'monitor':
        print("🚀 启动监控工具...")
        monitor = Monitor()
        monitor.start(interval=args.interval)
        
    elif args.command == 'process':
        print(f"📊 处理数据: {args.input}")
        result = process_data(args.input)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(str(result))
            print(f"✅ 结果已保存到: {args.output}")
        else:
            print(f"📈 处理结果: {result}")
            
    elif args.command == 'demo':
        print("🎯 运行演示...")
        from .demo import run_demo
        run_demo()
        
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
EOF
```

### 2. 更新 setup.py

```bash
# 创建或更新 setup.py
cat > setup.py << 'EOF'
from setuptools import setup, find_packages
import os

# 读取 README 文件
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# 读取依赖
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="case-utils",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="一个实用的Python工具包",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/case-utils",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "case-utils=case_utils.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
EOF
```

### 3. 测试命令行工具

```bash
# 安装项目（开发模式）
pip install -e .

# 测试命令行工具
case-utils --help
case-utils demo
case-utils monitor --interval 3

# 或者使用python -m方式
python -m case_utils.cli --help
python -m case_utils.cli demo
```

---

## **周日：数据准备**

### 1. 下载机器学习数据

```bash
# 创建数据目录结构
mkdir -p data/{raw,processed,external}
mkdir -p data/raw/breast_cancer

# 下载乳腺癌数据集
cd data/raw/breast_cancer

# 下载主数据文件
wget https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data

# 下载特征名称文件
wget https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.names

# 下载其他相关文件
wget https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
wget https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.names

# 回到项目根目录
cd ../../..
```

### 2. 创建数据说明文档

```bash
# 创建数据README
cat > data/README.md << 'EOF'
# 数据集说明

## 目录结构

```
data/
├── raw/                 # 原始数据
│   └── breast_cancer/   # 乳腺癌数据集
├── processed/           # 处理后的数据
└── external/           # 外部数据源
```

## 乳腺癌数据集 (Breast Cancer Wisconsin)

### 来源
- **数据源**: UCI Machine Learning Repository
- **链接**: https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(diagnostic)
- **下载日期**: $(date +%Y-%m-%d)

### 数据描述
- **样本数量**: 569个实例
- **特征数量**: 30个特征
- **类别数量**: 2类（恶性/良性）
- **缺失值**: 无

### 字段说明

| 列名 | 说明 | 类型 |
|------|------|------|
| ID | 病人编号 | 整数 |
| Diagnosis | 诊断结果 (M=恶性, B=良性) | 字符 |
| radius_mean | 半径均值 | 数值 |
| texture_mean | 纹理均值 | 数值 |
| perimeter_mean | 周长均值 | 数值 |
| area_mean | 面积均值 | 数值 |
| smoothness_mean | 光滑度均值 | 数值 |
| compactness_mean | 紧密度均值 | 数值 |
| concavity_mean | 凹度均值 | 数值 |
| concave points_mean | 凹点均值 | 数值 |
| symmetry_mean | 对称性均值 | 数值 |
| fractal_dimension_mean | 分形维度均值 | 数值 |
| ... | 其他特征（标准差和最大值） | 数值 |

### 用途
- **主要用途**: 机器学习分类任务
- **目标变量**: Diagnosis（恶性/良性分类）
- **应用场景**: 医学诊断辅助、模式识别研究

### 数据质量
- ✅ 无缺失值
- ✅ 特征已标准化
- ✅ 标签平衡
- ⚠️ 需要特征缩放

## 使用示例

```python
import pandas as pd
from case_utils.data import load_breast_cancer

# 加载数据
df = load_breast_cancer()

# 查看数据信息
print(df.head())
print(df.info())
print(df['Diagnosis'].value_counts())
```

## 处理步骤

1. **数据清洗**: 检查缺失值和异常值
2. **特征工程**: 标准化、特征选择
3. **数据划分**: 训练集/测试集分离
4. **可视化**: 探索性数据分析

## 相关文件

- `wdbc.data`: 主要数据文件
- `wdbc.names`: 特征详细说明
- `breast-cancer-wisconsin.data`: 备用格式
- `breast-cancer-wisconsin.names`: 详细文档
EOF
```

### 3. 创建GitHub Issue

```bash
# 使用GitHub CLI创建Issue（如果安装了gh）
gh issue create \
  --title "Week2 - 机器学习数据准备" \
  --body "## 任务清单

### 数据准备
- [x] 下载乳腺癌数据集
- [ ] 清理缺失值和异常值
- [ ] 特征标准化处理
- [ ] 划分训练/测试集

### 代码实现
- [ ] 创建数据加载模块
- [ ] 实现数据预处理函数
- [ ] 添加数据验证
- [ ] 编写单元测试

### 文档完善
- [ ] 完善数据说明文档
- [ ] 添加使用示例
- [ ] 更新API文档

### 截止日期
下周五 $(date -d 'next Friday' +%Y-%m-%d)

### 注意事项
1. 确保数据隐私和安全
2. 遵循数据使用协议
3. 保持代码可重现性

### 相关链接
- [UCI数据集页面](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(diagnostic))
- [项目文档](https://github.com/yourusername/case-utils)" \
  --label "enhancement" \
  --label "data-prep" \
  --label "week2"
```

### 4. 创建数据处理模块

```bash
# 创建数据处理模块
cat > case_utils/data_loader.py << 'EOF'
"""
数据加载和预处理模块
"""

import pandas as pd
import numpy as np
from typing import Tuple, Optional
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def load_breast_cancer(data_path: str = "data/raw/breast_cancer/wdbc.data") -> pd.DataFrame:
    """
    加载乳腺癌数据集
    
    Args:
        data_path: 数据文件路径
        
    Returns:
        包含特征和标签的DataFrame
    """
    # 定义列名
    column_names = [
        'ID', 'Diagnosis',
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
        'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
        'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
        'smoothness_worst', 'compactness_worst', 'concavity_worst',
        'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]
    
    # 加载数据
    df = pd.read_csv(data_path, header=None, names=column_names)
    
    # 数据验证
    logger.info(f"数据形状: {df.shape}")
    logger.info(f"缺失值: {df.isnull().sum().sum()}")
    logger.info(f"标签分布:\n{df['Diagnosis'].value_counts()}")
    
    return df


def preprocess_data(df: pd.DataFrame, 
                   test_size: float = 0.2,
                   random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    数据预处理和划分
    
    Args:
        df: 原始数据
        test_size: 测试集比例
        random_state: 随机种子
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    
    # 复制数据避免修改原数据
    data = df.copy()
    
    # 移除ID列
    data = data.drop('ID', axis=1)
    
    # 分离特征和标签
    X = data.drop('Diagnosis', axis=1)
    y = data['Diagnosis']
    
    # 标签编码
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # 特征标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    
    # 划分训练测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_encoded, test_size=test_size, random_state=random_state, stratify=y_encoded
    )
    
    logger.info(f"训练集形状: {X_train.shape}")
    logger.info(f"测试集形状: {X_test.shape}")
    
    return X_train, X_test, y_train, y_test


def save_processed_data(X_train: pd.DataFrame, X_test: pd.DataFrame,
                       y_train: pd.Series, y_test: pd.Series,
                       output_dir: str = "data/processed") -> None:
    """
    保存处理后的数据
    
    Args:
        X_train, X_test, y_train, y_test: 处理后的数据
        output_dir: 输出目录
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 保存数据
    X_train.to_csv(output_path / "X_train.csv", index=False)
    X_test.to_csv(output_path / "X_test.csv", index=False)
    pd.Series(y_train).to_csv(output_path / "y_train.csv", index=False)
    pd.Series(y_test).to_csv(output_path / "y_test.csv", index=False)
    
    logger.info(f"数据已保存到: {output_path}")


if __name__ == "__main__":
    # 示例用法
    logging.basicConfig(level=logging.INFO)
    
    # 加载数据
    df = load_breast_cancer()
    
    # 预处理
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # 保存数据
    save_processed_data(X_train, X_test, y_train, y_test)
    
    print("✅ 数据处理完成!")
EOF
```

### 5. 提交所有更改

```bash
# 添加所有新文件
git add .

# 提交周末工作
git commit -m "feat: 第二周数据准备

- 添加命令行入口和CLI工具
- 完善setup.py配置
- 下载乳腺癌数据集
- 创建数据处理模块
- 添加详细的文档说明
- 创建GitHub Issue跟踪进度"

# 推送到GitHub
git push

# 创建新的版本标签
git tag v0.2.0 -m "第二周完成 - 数据准备和CLI工具"
git push origin v0.2.0
```

---

## **学习小贴士总结**

### 快速理解技巧
- **子模块** = 嵌套的仓库，独立管理数据
- **PlantUML** = 代码画图，团队协作可视化
- **思维导图** = 知识树状图，系统化学习
- **setup.py** = 项目安装说明书，标准化部署
- **命令行入口** = 终端启动程序，提升用户体验

### 学习顺序建议
1. **先动手做** - 实践出真知
2. **再理解原理** - 知其然知其所以然
3. **遇到问题先查官方文档** - 培养自学能力
4. **每完成一个任务就提交代码** - 保持版本整洁
5. **用Issue记录问题和进度** - 项目化管理学习

### 持续改进
- 每周写总结，巩固知识
- 定期打标签，标记重要节点
- 用工具提升效率，而不是增加复杂度
- 保持好奇心，探索新技术

按照这些步骤，你就能系统地完成第二周的学习任务！
