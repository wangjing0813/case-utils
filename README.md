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


---

### 关键点回顾

1. **`requirements.txt`** 必须包含 `pandas` 与 `aiofiles`（它们是 `utils.py` 里唯一的外部库）。  
2. **版本号**：使用 `>=` 可以保持向前兼容；如果项目对确定版本有严格要求，使用 `==` 并用 `pip freeze` 锁定。  
3. **开发依赖**（pytest、black、mypy 等）可以放在同一文件的下部或另建 `dev-requirements.txt`，根据团队工作流自行决定。  
4. **安装**：`pip install -r requirements.txt` 是最常用的方式，配合虚拟环境可以确保全局 Python 环境不受影响。

把这些内容复制进你的仓库根目录的 `requirements.txt`（或分别写到 `requirements.txt`、`dev-requirements.txt`），提交并推送即可。之后 **任何人** 只要 `git clone` 并运行上述 `pip install` 命令，就能得到完整、可运行的环境。  

如果还有 **依赖冲突**、**特定版本需求**（比如你必须使用 `pandas==2.1.3`），或者想了解 **如何在 CI 中使用这些文件**，随时告诉我！祝你项目顺利 🚀.


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



# .gitignore 里加入：
data/
*.pyc
__pycache__/
.venv/


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
