# case-utils
Utilities for async CSV handling and data filtering

## 安装依赖

```bash
# 创建并激活虚拟环境（推荐）
python3 -m venv .venv
source .venv/bin/activate

# 安装运行时依赖
pip install -r requirements.txt

#（可选）安装开发工具
pip install -r dev-requirements.txt   # 或者直接使用本文件的 dev 部分


# ==================== Runtime ====================
pandas>=2.0.0
aiofiles>=23.2.0

# ==================== Development ====================
# testing
pytest>=8.0.0
pytest-asyncio>=0.23.0

# formatting & linting
black>=24.1.0
isort>=5.13.0
flake8>=7.0.0

# type checking
mypy>=1.8.0





'''
case-utils/
│
├─ .git/                 ← Git 元数据（已存在）
├─ .gitignore            ← 忽略不需要提交的文件/目录
├─ .venv/                ← 本地虚拟环境（不提交）
├─ data/                 ← 示例 CSV（如果不想公开，可加入 .gitignore）
│   └─ sample.csv
├─ utils.py              ← 核心实现（read_csv_async、filter_invalid）
├─ utils_wrapper.py      ← 同步包装函数（load_and_clean）
├─ demo.py               ← 演示脚本（可在 README 中引用）
├─ requirements.txt      ← 运行时依赖（已锁定 pandas、aiofiles）
├─ README.md             ← 项目说明（已写好，可再补充示例）
├─ LICENSE               ← 开源许可证（MIT）
└─ 1                     ← 误生成的空文件（建议删除）
'''
 
## 开发工作流
 
```mermaid
sequenceDiagram
    title case-utils 开发工作流
    
    participant 开发者
    participant 本地Git
    participant GitHub
    participant data子模块
    
    开发者->>本地Git: 修改代码
    开发者->>data子模块: git pull
    开发者->>本地Git: git add .
    开发者->>本地Git: git commit
    本地Git->>GitHub: git push
    GitHub->>其他开发者: git clone
    其他开发者->>子模块: git submodule update --init
'''