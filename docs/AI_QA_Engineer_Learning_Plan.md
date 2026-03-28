# AI/Deep Learning QA 工程师 — 完整学习计划

> **背景假设：** 有 Java / C / Python 经验但不够熟练，零 AI 基础
> **总周期：** 18 周（含编程强化）| 每天 3-4 小时（工作日）| 周末可选加练
> **总学时：** ~330 小时

---

## 目录

- [前置阶段：编程与工具强化（第 0-1 周）](#前置阶段编程与工具强化第-0-1-周)
- [第一阶段：AI/深度学习基础（第 2-4 周）](#第一阶段ai深度学习基础第-2-4-周)
- [第二阶段：大语言模型原理（第 5-7 周）](#第二阶段大语言模型原理第-5-7-周)
- [第三阶段：GPU 与 CUDA（第 8-10 周）](#第三阶段gpu-与-cuda第-8-10-周)
- [第四阶段：推理引擎实战（第 11-13 周）](#第四阶段推理引擎实战第-11-13-周)
- [第五阶段：软件测试与 QA（第 14-16 周）](#第五阶段软件测试与-qa第-14-16-周)
- [第六阶段：综合实战（第 17-18 周）](#第六阶段综合实战第-17-18-周)
- [附录：推荐资源汇总](#附录推荐资源汇总)

---

# 前置阶段：编程与工具强化（第 0-1 周）

> 你已有 Java/C/Python 经验，这个阶段的目的是把 **Python 提到熟练**、**C/C++ 补齐关键知识**、**Linux 命令行达到日常使用水平**。

## 第 0 周：Python 强化 + Linux（每天 3 小时）

### Day 1 — Python 数据结构与语法进阶（3h）

**学习内容：**
- 列表推导式、生成器表达式、字典推导式
- `*args` / `**kwargs`、装饰器（decorator）、上下文管理器（with 语句）
- 类型提示（Type Hints）：`def func(x: int) -> str`

**学习资源：**
- 书籍：《Python Crash Course》第 7-9 章（函数、类）
- 在线：https://docs.python.org/3/tutorial/ （官方教程，重点看 4-9 章）
- 视频：Corey Schafer YouTube — "Python OOP Tutorial"（6 集，每集 15 分钟）

**动手实践：**
```python
# 练习 1：用装饰器实现函数计时
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(1)

# 练习 2：实现一个简单的上下文管理器
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# 练习 3：列表推导式 — 生成 1-100 中所有能被3整除的数的平方
squares = [x**2 for x in range(1, 101) if x % 3 == 0]
```

**必须搞清楚的知识点：**
- [ ] 什么是可迭代对象（Iterable）vs 迭代器（Iterator）vs 生成器（Generator）？
- [ ] 装饰器本质上是什么？（高阶函数，接受函数返回函数）
- [ ] Python 的 GIL 是什么？为什么多线程在 CPU 密集任务中无法加速？
- [ ] `list` vs `tuple` vs `set` vs `dict` 的时间复杂度差异

---

### Day 2 — NumPy 基础（3h）

**学习内容：**
- ndarray 创建、shape/dtype/reshape
- 索引、切片、布尔索引
- 广播机制（Broadcasting）
- 矩阵运算：dot、matmul、转置

**学习资源：**
- 官方文档：https://numpy.org/doc/stable/user/quickstart.html
- 视频：freeCodeCamp — "NumPy Full Course"（YouTube，1 小时）
- 交互练习：https://github.com/rougier/numpy-100 （100 道 NumPy 练习题）

**动手实践：**
```python
import numpy as np

# 练习 1：创建并操作数组
a = np.random.randn(3, 4)       # 3x4 随机矩阵
print(a.shape, a.dtype)          # 查看形状和数据类型
b = a.reshape(4, 3)              # 重塑
c = a.T                          # 转置

# 练习 2：广播机制
matrix = np.ones((3, 4))         # 3x4 全 1 矩阵
row_vector = np.array([1, 2, 3, 4])  # 形状 (4,)
result = matrix + row_vector     # 广播：(3,4) + (4,) → (3,4)

# 练习 3：矩阵乘法
A = np.random.randn(3, 4)
B = np.random.randn(4, 5)
C = A @ B                       # 等价于 np.matmul(A, B)，结果形状 (3,5)

# 练习 4：用 NumPy 实现 Softmax 函数
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # 减去最大值防溢出
    return exp_x / exp_x.sum()

print(softmax(np.array([1.0, 2.0, 3.0])))
```

**必须搞清楚的知识点：**
- [ ] Broadcasting 规则是什么？给定两个形状如何判断能否广播？
- [ ] `np.dot` vs `np.matmul` vs `@` 的区别
- [ ] 为什么 NumPy 比纯 Python 循环快？（底层 C 实现 + 向量化操作）
- [ ] 什么是 stride？reshape 和 transpose 是否会复制数据？

---

### Day 3 — Python 包管理与虚拟环境（2h）+ Linux 基础（1h）

**学习内容（Python 部分）：**
- pip / conda / uv 包管理工具
- 虚拟环境：venv / conda env
- requirements.txt / pyproject.toml

**学习内容（Linux 部分）：**
- 文件操作：`ls -la`, `cp`, `mv`, `rm`, `find`, `chmod`, `chown`
- 文本处理：`cat`, `grep`, `awk`, `sed`, `head`, `tail`, `wc`
- 进程管理：`ps aux`, `top/htop`, `kill`, `nohup`, `&`
- 网络：`curl`, `wget`, `ssh`, `scp`

**学习资源：**
- Linux：https://linuxcommand.org/tlcl.php（《The Linux Command Line》免费在线书）
- Linux：https://github.com/jlevy/the-art-of-command-line （命令行的艺术，有中文版）
- Python 环境：https://docs.python.org/3/library/venv.html

**动手实践：**
```bash
# Linux 练习
# 1. 查找当前目录下所有 .py 文件
find . -name "*.py" -type f

# 2. 在所有 Python 文件中搜索 "import torch"
grep -r "import torch" --include="*.py" .

# 3. 查看 GPU 信息（如果有）
nvidia-smi

# 4. 用 awk 统计文件行数
find . -name "*.py" | xargs wc -l | sort -n

# 5. 进程管理：后台运行并查看
nohup python train.py > train.log 2>&1 &
tail -f train.log

# Python 环境练习
python3 -m venv myenv
source myenv/bin/activate
pip install numpy torch
pip freeze > requirements.txt
```

**必须搞清楚的知识点：**
- [ ] Linux 文件权限 `rwxr-xr-x` 如何解读？数字表示法 755 是什么意思？
- [ ] `|`（管道）和 `>`（重定向）和 `>>`（追加重定向）的区别
- [ ] 什么是环境变量？`PATH`, `LD_LIBRARY_PATH`, `CUDA_HOME` 各有什么用？
- [ ] `conda` 和 `pip` 混用的坑是什么？为什么推荐先 conda 再 pip？

---

### Day 4 — C/C++ 关键知识补齐（3h）

**学习内容：**
- C 指针复习：指针运算、数组与指针、函数指针
- C++ 基础：引用、类、构造/析构、RAII
- C++ 现代特性（C++11/14/17）：auto、智能指针、lambda、range-based for
- 内存管理：栈 vs 堆、malloc/free vs new/delete、内存泄漏

**学习资源：**
- C 指针：《C Primer Plus》第 10-12 章（指针与数组）
- C++ 快速入门：https://www.learncpp.com/（在线免费教程，选读重点章节）
- 视频：The Cherno YouTube — "C++ Tutorial"（选看指针、引用、智能指针几集）

**动手实践：**
```cpp
// 练习 1：理解指针与数组
#include <stdio.h>
int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr;
    printf("arr[2] = %d\n", *(p + 2));  // 指针运算

    // 练习 2：动态内存分配
    int *dynamic_arr = (int*)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) dynamic_arr[i] = i * 10;
    free(dynamic_arr);  // 必须释放!

    return 0;
}

// 练习 3：C++ 智能指针（编译：g++ -std=c++17 main.cpp）
#include <memory>
#include <iostream>
int main() {
    auto ptr = std::make_unique<int>(42);    // unique_ptr：独占所有权
    auto shared = std::make_shared<int>(99); // shared_ptr：共享所有权
    std::cout << *ptr << ", " << *shared << std::endl;
    // 不需要手动 delete，离开作用域自动释放
    return 0;
}
```

**必须搞清楚的知识点：**
- [ ] 指针和引用的区别是什么？
- [ ] `unique_ptr` vs `shared_ptr` vs `weak_ptr` 各自的使用场景
- [ ] 什么是 RAII？为什么它在 C++ 中很重要？
- [ ] 栈内存和堆内存的区别？为什么栈更快？
- [ ] 编译链接过程：预处理 → 编译 → 汇编 → 链接

---

### Day 5 — Git + 开发工具链（3h）

**学习内容：**
- Git 核心操作：clone, add, commit, push, pull, branch, merge, rebase
- Git 高级：stash, cherry-pick, reset vs revert, .gitignore
- 开发工具：VS Code 配置、SSH Remote 开发、tmux 终端复用

**学习资源：**
- Git：https://learngitbranching.js.org/（交互式 Git 学习）
- Git：《Pro Git》在线免费书 https://git-scm.com/book/zh/v2
- tmux：https://github.com/tmux/tmux/wiki/Getting-Started

**动手实践：**
```bash
# Git 练习
git init my-learning-repo && cd my-learning-repo
git checkout -b feature/week0
echo "# AI QA Learning" > README.md
git add . && git commit -m "Initial commit"
git log --oneline --graph

# tmux 基础
tmux new -s dev          # 新建 session
# Ctrl+b % 竖分屏 | Ctrl+b " 横分屏 | Ctrl+b d detach
tmux attach -t dev       # 重新连接
```

**必须搞清楚的知识点：**
- [ ] `git merge` vs `git rebase` 什么区别？什么时候用哪个？
- [ ] `git reset --soft/--mixed/--hard` 三者的区别
- [ ] 如何解决 merge conflict？

---

## 第 1 周：Python 科学计算与数据处理（每天 3 小时）

### Day 1 — Pandas 基础（3h）

**学习资源：**
- https://pandas.pydata.org/docs/getting_started/10min.html（10 分钟入门）
- 书籍：《Python for Data Analysis》第 5-7 章

**动手实践：**
```python
import pandas as pd

# 读取 CSV、基本操作
df = pd.read_csv("data.csv")
df.head(), df.describe(), df.info()
df.groupby("category").mean()
df[df["score"] > 90].sort_values("score", ascending=False)
```

### Day 2 — Matplotlib 可视化（3h）

**学习资源：**
- https://matplotlib.org/stable/tutorials/index.html
- 视频：Corey Schafer — "Matplotlib Tutorial"（YouTube）

**动手实践：**
```python
import matplotlib.pyplot as plt
import numpy as np

# 画损失曲线（后续深度学习会频繁用到）
epochs = range(1, 51)
train_loss = [1.0 / (1 + 0.1 * e) + np.random.normal(0, 0.02) for e in epochs]
val_loss = [1.0 / (1 + 0.08 * e) + np.random.normal(0, 0.03) for e in epochs]

plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss, label="Train Loss")
plt.plot(epochs, val_loss, label="Val Loss")
plt.xlabel("Epoch"); plt.ylabel("Loss")
plt.legend(); plt.title("Training Curve")
plt.savefig("loss_curve.png", dpi=150)
```

### Day 3 — Python 并发与多进程（3h）

**学习内容：**
- threading vs multiprocessing vs asyncio
- concurrent.futures: ThreadPoolExecutor / ProcessPoolExecutor
- subprocess 模块：调用外部命令

**学习资源：**
- 官方文档：https://docs.python.org/3/library/concurrent.futures.html
- Real Python：https://realpython.com/python-concurrency/

**动手实践：**
```python
# 多进程并行处理（AI测试中常用于批量处理数据）
from concurrent.futures import ProcessPoolExecutor
import time

def heavy_task(n):
    total = sum(i * i for i in range(n))
    return total

start = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(heavy_task, [10**7] * 8))
print(f"Parallel: {time.time() - start:.2f}s")

# subprocess：调用系统命令（测试中常用）
import subprocess
result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
print(result.stdout)
```

**必须搞清楚的知识点：**
- [ ] GIL 导致 Python 多线程无法利用多核做 CPU 密集任务，所以要用多进程
- [ ] `asyncio` 适合 IO 密集场景（网络请求、文件读写），非 CPU 密集

### Day 4 — Python 测试框架 pytest（3h）

**学习资源：**
- 官方文档：https://docs.pytest.org/en/stable/
- 书籍：《Python Testing with pytest》（Brian Okken）

**动手实践：**
```python
# test_example.py
import pytest

def add(a, b):
    return a + b

# 基本测试
def test_add():
    assert add(1, 2) == 3

# 参数化测试
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# fixture
@pytest.fixture
def sample_data():
    return {"model": "llama", "tokens": 1024}

def test_model_name(sample_data):
    assert sample_data["model"] == "llama"

# 运行：pytest test_example.py -v
```

**必须搞清楚的知识点：**
- [ ] fixture 的 scope（function/class/module/session）有什么区别？
- [ ] conftest.py 的作用是什么？
- [ ] 如何用 pytest-xdist 并行运行测试？

### Day 5 — HTTP 请求与 API 测试（3h）

**学习资源：**
- requests 库：https://docs.python-requests.org/
- httpx（支持异步）：https://www.python-httpx.org/

**动手实践：**
```python
import requests
import json

# REST API 测试（这是后续测试推理引擎 API 的基础）
# OpenAI 兼容 API 格式（vLLM/TensorRT-LLM 都支持）
def test_chat_completion():
    url = "http://localhost:8000/v1/chat/completions"
    payload = {
        "model": "meta-llama/Llama-2-7b-chat-hf",
        "messages": [{"role": "user", "content": "Hello"}],
        "temperature": 0.7,
        "max_tokens": 100
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "choices" in data
    assert len(data["choices"]) > 0
    assert "message" in data["choices"][0]

# 流式响应测试（SSE: Server-Sent Events）
def test_streaming():
    url = "http://localhost:8000/v1/chat/completions"
    payload = {
        "model": "meta-llama/Llama-2-7b-chat-hf",
        "messages": [{"role": "user", "content": "Count 1 to 5"}],
        "stream": True
    }
    response = requests.post(url, json=payload, stream=True)
    for line in response.iter_lines():
        if line:
            text = line.decode("utf-8")
            if text.startswith("data: ") and text != "data: [DONE]":
                chunk = json.loads(text[6:])
                print(chunk["choices"][0]["delta"])
```

**必须搞清楚的知识点：**
- [ ] HTTP 方法（GET/POST/PUT/DELETE）的语义区别
- [ ] 什么是 SSE（Server-Sent Events）？和 WebSocket 有什么区别？
- [ ] RESTful API 设计规范基础

---

# 第一阶段：AI/深度学习基础（第 2-4 周）

## 第 2 周：机器学习核心概念（每天 3 小时）

### Day 1 — 什么是机器学习（3h）

**学习内容：**
- 机器学习定义：从数据中学习模式，做出预测或决策
- 三大类型：监督学习、无监督学习、强化学习
- 核心概念：特征（Feature）、标签（Label）、模型（Model）、训练（Training）、推理（Inference）
- 损失函数（Loss Function）：MSE（均方误差）、Cross-Entropy（交叉熵）

**学习资源：**
- 视频：吴恩达《Machine Learning Specialization》（Coursera）第 1 周
  - 地址：https://www.coursera.org/specializations/machine-learning-introduction
  - 重点看：什么是机器学习、监督学习、损失函数
- 视频（中文）：李宏毅机器学习 2023 — 第 1 讲
  - 地址：https://www.youtube.com/c/HungyiLee （搜 "ML 2023"）
- 文章：https://developers.google.com/machine-learning/crash-course （Google ML Crash Course）

**动手实践：**
```python
import numpy as np
import matplotlib.pyplot as plt

# 手写线性回归 — 梯度下降
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# 梯度下降
learning_rate = 0.1
n_iterations = 1000
m = len(X)
theta = np.random.randn(2, 1)  # [bias, weight]

X_b = np.c_[np.ones((100, 1)), X]  # 加 bias 列

losses = []
for i in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta -= learning_rate * gradients
    loss = np.mean((X_b.dot(theta) - y) ** 2)
    losses.append(loss)

print(f"学到的参数: bias={theta[0][0]:.2f}, weight={theta[1][0]:.2f}")
# 应该接近 bias=4, weight=3

plt.plot(losses)
plt.xlabel("Iteration"); plt.ylabel("MSE Loss")
plt.title("Gradient Descent Convergence")
plt.savefig("gradient_descent.png")
```

**必须搞清楚的知识点：**
- [ ] 梯度下降的直觉理解：想象在山谷中找最低点，每一步沿着最陡的方向走
- [ ] 学习率（Learning Rate）太大会怎样？太小会怎样？
- [ ] 什么是收敛（Convergence）？如何判断模型已经收敛？
- [ ] 训练（Training）和推理（Inference）的区别？（训练=学习参数，推理=用参数做预测）

---

### Day 2 — 过拟合与模型评估（3h）

**学习内容：**
- 训练集 / 验证集 / 测试集 的划分与作用
- 过拟合（Overfitting）vs 欠拟合（Underfitting）
- 正则化（L1/L2 Regularization）
- 评估指标：Accuracy、Precision、Recall、F1-Score

**学习资源：**
- 吴恩达 ML 课程第 2-3 周
- 可视化理解：https://playground.tensorflow.org （TensorFlow Playground — 直接在浏览器中观察过拟合）

**动手实践：**
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error
import numpy as np

# 生成数据
X = np.random.randn(200, 10)
y = X[:, 0] * 3 + X[:, 1] * 2 + np.random.randn(200) * 0.5

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 对比普通线性回归 vs 正则化
models = {
    "Linear": LinearRegression(),
    "Ridge(L2)": Ridge(alpha=1.0),
    "Lasso(L1)": Lasso(alpha=0.1),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    train_mse = mean_squared_error(y_train, model.predict(X_train))
    test_mse = mean_squared_error(y_test, model.predict(X_test))
    print(f"{name}: Train MSE={train_mse:.4f}, Test MSE={test_mse:.4f}")
```

**必须搞清楚的知识点：**
- [ ] 如果训练集上效果好但测试集上差，是什么问题？（过拟合）
- [ ] 如果训练集和测试集上效果都差呢？（欠拟合）
- [ ] L1 正则化（Lasso）为什么能产生稀疏解（部分权重变为 0）？
- [ ] 为什么需要验证集？（用于调超参数，避免在测试集上"作弊"）

---

### Day 3 — 神经网络基础（3h）

**学习内容：**
- 感知机（Perceptron）→ 多层感知机（MLP）
- 激活函数：Sigmoid、ReLU、Tanh、Softmax
- 前向传播（Forward Propagation）的数学过程
- 为什么需要激活函数？（没有非线性变换，多层等价于单层）

**学习资源：**
- 3Blue1Brown：《Neural Networks》4 集动画（YouTube 搜索 "3Blue1Brown neural network"）
  - 第 1 集：什么是神经网络
  - 第 2 集：梯度下降
  - 第 3 集：反向传播
  - 第 4 集：反向传播的数学
- 交互可视化：https://playground.tensorflow.org

**动手实践：**
```python
import numpy as np

# 用纯 NumPy 实现两层神经网络（不用任何框架）
class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        # 随机初始化权重
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_deriv(self, x):
        return (x > 0).astype(float)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / exp_x.sum(axis=1, keepdims=True)

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1      # 线性变换
        self.a1 = self.relu(self.z1)          # 激活
        self.z2 = self.a1 @ self.W2 + self.b2 # 线性变换
        self.a2 = self.softmax(self.z2)        # 输出概率
        return self.a2

    def backward(self, X, y, lr=0.01):
        m = X.shape[0]
        # 反向传播
        dz2 = self.a2 - y                       # 输出层梯度
        dW2 = self.a1.T @ dz2 / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        dz1 = (dz2 @ self.W2.T) * self.relu_deriv(self.z1)
        dW1 = X.T @ dz1 / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        # 更新参数
        self.W2 -= lr * dW2; self.b2 -= lr * db2
        self.W1 -= lr * dW1; self.b1 -= lr * db1

# 测试：XOR 问题（线性不可分，需要非线性）
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[1,0],[0,1],[0,1],[1,0]])  # one-hot

nn = SimpleNN(2, 8, 2)
for epoch in range(5000):
    out = nn.forward(X)
    nn.backward(X, y, lr=0.5)

predictions = np.argmax(nn.forward(X), axis=1)
print(f"XOR predictions: {predictions}")  # 应该是 [0, 1, 1, 0]
```

**必须搞清楚的知识点：**
- [ ] 为什么 Sigmoid 在深层网络中会出现梯度消失？ReLU 如何解决？
- [ ] Softmax 的输出是什么？（概率分布，所有值加起来=1）
- [ ] 前向传播的公式：z = Wx + b, a = activation(z)
- [ ] 神经网络本质上在做什么？（学习一个复杂的非线性函数映射）

---

### Day 4 — 反向传播算法（3h）

**学习内容：**
- 链式法则（Chain Rule）
- 计算图（Computational Graph）
- 反向传播的完整数学推导（两层网络）
- 梯度检验（Gradient Checking）

**学习资源：**
- 3Blue1Brown 第 3-4 集（反向传播动画）
- CS231n 笔记：https://cs231n.github.io/optimization-2/ （Backpropagation）
- 文章：https://colah.github.io/posts/2015-08-Backprop/ （Chris Olah 的计算图解释）

**动手实践：**
```python
# 梯度检验：用数值方法验证反向传播是否正确
def gradient_check(nn, X, y, epsilon=1e-7):
    """数值梯度 vs 解析梯度对比"""
    # 计算解析梯度
    nn.forward(X)
    nn.backward(X, y)
    analytical_grad = nn.W1.copy()

    # 数值梯度
    numerical_grad = np.zeros_like(nn.W1)
    for i in range(nn.W1.shape[0]):
        for j in range(nn.W1.shape[1]):
            nn.W1[i, j] += epsilon
            loss_plus = -np.sum(y * np.log(nn.forward(X) + 1e-8))
            nn.W1[i, j] -= 2 * epsilon
            loss_minus = -np.sum(y * np.log(nn.forward(X) + 1e-8))
            nn.W1[i, j] += epsilon  # 恢复
            numerical_grad[i, j] = (loss_plus - loss_minus) / (2 * epsilon)

    diff = np.linalg.norm(analytical_grad - numerical_grad)
    diff /= np.linalg.norm(analytical_grad) + np.linalg.norm(numerical_grad)
    print(f"Gradient difference: {diff}")  # 应该 < 1e-5
```

**必须搞清楚的知识点：**
- [ ] 链式法则：dL/dW = dL/da * da/dz * dz/dW，每一步是什么意思？
- [ ] 计算图中"前向"和"反向"分别在做什么？
- [ ] 为什么反向传播比逐个参数数值求梯度快得多？

---

### Day 5 — 优化器与训练技巧（3h）

**学习内容：**
- SGD、Momentum、Adam 优化器的区别
- Batch Size 的选择与影响
- 学习率调度（Learning Rate Schedule）
- Batch Normalization、Dropout

**学习资源：**
- 动画对比优化器：https://ruder.io/optimizing-gradient-descent/ （经典博客）
- CS231n 笔记：https://cs231n.github.io/neural-networks-3/

**必须搞清楚的知识点：**
- [ ] Adam 为什么是最常用的优化器？它结合了什么？（Momentum + RMSProp）
- [ ] Batch Size 越大越好吗？（不是，太大泛化性差，太小梯度噪声大）
- [ ] Dropout 在训练和推理时的行为有什么不同？

---

## 第 3 周：深度学习框架 PyTorch（每天 3 小时）

### Day 1 — PyTorch 基础：Tensor（3h）

**学习资源：**
- PyTorch 官方教程：https://pytorch.org/tutorials/beginner/basics/intro.html
- 视频：freeCodeCamp — "PyTorch for Deep Learning"（YouTube，26 小时，选看前 5 小时）

**动手实践：**
```python
import torch

# Tensor 基本操作
a = torch.randn(3, 4)
b = torch.zeros(3, 4)
c = torch.ones_like(a)

# GPU 操作（如果有 GPU）
if torch.cuda.is_available():
    device = torch.device("cuda")
    a_gpu = a.to(device)
    print(f"Tensor on: {a_gpu.device}")

# 自动求导
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2 + 3 * x + 1
y.backward()
print(f"dy/dx at x=2: {x.grad}")  # 应该是 7.0 (2*2+3)

# Tensor vs NumPy 互转
np_arr = a.numpy()
tensor_from_np = torch.from_numpy(np_arr)
```

**必须搞清楚的知识点：**
- [ ] `requires_grad=True` 做了什么？（告诉 PyTorch 跟踪这个 Tensor 的计算历史）
- [ ] `.backward()` 做了什么？（自动计算梯度并存到 `.grad` 属性中）
- [ ] `.detach()` 和 `with torch.no_grad()` 有什么区别？分别何时使用？
- [ ] CPU Tensor 和 GPU Tensor 的区别？`.to(device)` 做了什么？

---

### Day 2 — 用 PyTorch 训练 MNIST（3h）

**动手实践（完整代码）：**
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. 数据加载
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('./data', train=False, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=1000)

# 2. 定义模型
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28*28, 256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.flatten(x)     # (batch, 1, 28, 28) → (batch, 784)
        x = self.relu(self.fc1(x))
        return self.fc2(x)      # 输出 logits（未经 softmax）

model = MLP()
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()  # 内部包含 softmax

# 3. 训练循环
for epoch in range(5):
    model.train()
    total_loss = 0
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()       # 清零梯度
        output = model(batch_X)     # 前向传播
        loss = criterion(output, batch_y)  # 计算损失
        loss.backward()             # 反向传播
        optimizer.step()            # 更新参数
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss/len(train_loader):.4f}")

# 4. 测试评估
model.eval()
correct = 0
with torch.no_grad():
    for batch_X, batch_y in test_loader:
        pred = model(batch_X).argmax(dim=1)
        correct += (pred == batch_y).sum().item()
print(f"Test Accuracy: {correct/len(test_data)*100:.2f}%")

# 5. 保存/加载模型
torch.save(model.state_dict(), "mnist_model.pth")
# 加载: model.load_state_dict(torch.load("mnist_model.pth"))
```

**必须搞清楚的知识点：**
- [ ] `model.train()` vs `model.eval()` 有什么区别？（影响 Dropout 和 BatchNorm 的行为）
- [ ] 为什么要 `optimizer.zero_grad()`？（否则梯度会累加）
- [ ] `nn.CrossEntropyLoss` 内部做了什么？（LogSoftmax + NLLLoss）
- [ ] `torch.no_grad()` 的作用？（推理时不需要计算梯度，节省内存和计算）
- [ ] DataLoader 的 `shuffle=True` 为什么只在训练时用？

---

### Day 3 — CNN 卷积神经网络（3h）

**学习内容：**
- 卷积操作的直觉：用一个小窗口（kernel）扫描图片，提取局部特征
- 池化（Pooling）：缩小特征图尺寸
- 经典架构：LeNet → AlexNet → VGG → ResNet（了解演进即可）

**学习资源：**
- CS231n 笔记：https://cs231n.github.io/convolutional-networks/
- 可视化：https://poloclub.github.io/cnn-explainer/ （CNN Explainer — 浏览器中交互式理解）

**动手实践：**
```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)   # 输入1通道，输出32通道
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)          # 2x2 池化，尺寸减半
        self.fc1 = nn.Linear(64 * 7 * 7, 128)   # 28→14→7
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))  # (batch,1,28,28)→(batch,32,14,14)
        x = self.pool(self.relu(self.conv2(x)))  # (batch,32,14,14)→(batch,64,7,7)
        x = x.view(x.size(0), -1)               # 展平
        x = self.relu(self.fc1(x))
        return self.fc2(x)

# 用同样的 MNIST 数据训练，对比 MLP 和 CNN 的准确率
```

**必须搞清楚的知识点：**
- [ ] 卷积核（Kernel）的参数量怎么算？（in_channels * out_channels * kernel_h * kernel_w）
- [ ] 输出特征图尺寸怎么算？`(input_size - kernel_size + 2*padding) / stride + 1`
- [ ] 为什么 CNN 比全连接网络更适合图像？（参数共享 + 局部连接 → 参数量更少）
- [ ] ResNet 的 Skip Connection（残差连接）解决了什么问题？（深层网络的退化问题）

---

### Day 4 — RNN/LSTM（了解即可）（3h）

**学习内容：**
- RNN 的结构：隐藏状态在时间步之间传递
- 长期依赖问题与梯度消失
- LSTM 的门控机制（遗忘门、输入门、输出门）
- **重点理解为什么 Transformer 取代了 RNN**

**学习资源：**
- 经典博客：https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- 李宏毅 RNN 课程（YouTube）

**必须搞清楚的知识点：**
- [ ] RNN 的隐藏状态（Hidden State）是什么？
- [ ] 为什么 RNN 在长序列上表现不好？（梯度消失/爆炸）
- [ ] LSTM 如何通过"门"来控制信息流？
- [ ] Transformer 相比 RNN 的优势是什么？（并行化、长距离依赖）

---

### Day 5 — 模型保存、ONNX 导出（3h）

**动手实践：**
```python
import torch
import torch.onnx

# 保存与加载
model = SimpleCNN()
# 方式1：保存权重（推荐）
torch.save(model.state_dict(), "model_weights.pth")
loaded = SimpleCNN()
loaded.load_state_dict(torch.load("model_weights.pth"))

# 方式2：保存整个模型
torch.save(model, "full_model.pth")

# 导出 ONNX（跨框架通用格式）
dummy_input = torch.randn(1, 1, 28, 28)
torch.onnx.export(model, dummy_input, "model.onnx",
                   input_names=["image"],
                   output_names=["prediction"],
                   dynamic_axes={"image": {0: "batch_size"}})

# 模型参数量统计
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Total: {total_params:,}, Trainable: {trainable_params:,}")
```

**必须搞清楚的知识点：**
- [ ] `state_dict()` 保存的是什么？（模型参数的字典）
- [ ] ONNX 是什么？为什么要导出为 ONNX？（跨框架、方便部署到 TensorRT 等推理引擎）
- [ ] `dynamic_axes` 为什么重要？（允许推理时使用不同的 batch size）

---

## 第 4 周：NLP 与 Transformer 架构（每天 3.5 小时）⭐ 最关键的一周

### Day 1 — NLP 基础与 Tokenization（3.5h）

**学习内容：**
- NLP 任务：分类、翻译、摘要、问答、文本生成
- 分词（Tokenization）的演进：
  - 字符级 → 词级 → 子词级（BPE、WordPiece、SentencePiece）
- 词嵌入（Word Embedding）：Word2Vec、GloVe

**学习资源：**
- HuggingFace NLP Course 第 1-2 章：https://huggingface.co/learn/nlp-course/
- BPE 原理：https://huggingface.co/learn/nlp-course/chapter6/5

**动手实践：**
```python
# 使用 HuggingFace tokenizer
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
text = "Hello, how are you doing today?"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print(f"原文: {text}")
print(f"Token: {tokens}")
print(f"Token IDs: {token_ids}")
print(f"词表大小: {tokenizer.vocab_size}")

# 观察中文分词
text_cn = "大语言模型是人工智能的重要方向"
tokens_cn = tokenizer.tokenize(text_cn)
print(f"中文 Token: {tokens_cn}")
# 注意观察中文可能被拆成很多小片段（因为训练数据以英文为主）
```

**必须搞清楚的知识点：**
- [ ] 为什么不用字符级分词？（序列太长，丢失语义信息）
- [ ] 为什么不用词级分词？（OOV 问题——遇到没见过的词怎么办？）
- [ ] BPE 的核心思想是什么？（从字符开始，不断合并最频繁的相邻对）
- [ ] 词表大小对模型有什么影响？（词表越大 → 嵌入层越大 → 更多参数）

---

### Day 2 — Attention 注意力机制（3.5h）⭐⭐⭐

**学习内容：**
- 为什么需要 Attention？（让模型"注意"输入中最相关的部分）
- Self-Attention 公式：Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
- Query、Key、Value 的直觉理解

**学习资源：**
- 必读博客：Jay Alammar — "The Illustrated Transformer"
  - https://jalammar.github.io/illustrated-transformer/
- 可视化：https://github.com/jessevig/bertviz （Attention 权重可视化工具）
- 视频：StatQuest — "Attention for Neural Networks"（YouTube）

**动手实践：**
```python
import torch
import torch.nn.functional as F
import math

def self_attention(Q, K, V):
    """
    手写 Self-Attention
    Q, K, V: (batch_size, seq_len, d_model)
    """
    d_k = Q.size(-1)

    # Step 1: 计算注意力分数
    scores = torch.matmul(Q, K.transpose(-2, -1))  # (batch, seq, seq)

    # Step 2: 缩放（防止 softmax 梯度消失）
    scores = scores / math.sqrt(d_k)

    # Step 3: Softmax 归一化 → 注意力权重
    attention_weights = F.softmax(scores, dim=-1)   # 每一行加起来=1

    # Step 4: 加权求和
    output = torch.matmul(attention_weights, V)     # (batch, seq, d_model)

    return output, attention_weights

# 测试
batch_size, seq_len, d_model = 2, 5, 64
Q = torch.randn(batch_size, seq_len, d_model)
K = torch.randn(batch_size, seq_len, d_model)
V = torch.randn(batch_size, seq_len, d_model)

output, weights = self_attention(Q, K, V)
print(f"Output shape: {output.shape}")        # (2, 5, 64)
print(f"Attention weights shape: {weights.shape}")  # (2, 5, 5)
print(f"权重每行之和: {weights[0].sum(dim=-1)}")      # 应该都是 1.0
```

**必须搞清楚的知识点（面试高频）：**
- [ ] Q、K、V 分别代表什么？
  - Query = "我在找什么"
  - Key = "我有什么可以提供的"
  - Value = "我实际的内容"
  - 类比：图书馆搜索 — Q 是搜索词，K 是书名索引，V 是书的内容
- [ ] 为什么要除以 sqrt(d_k)？（当 d_k 很大时，点积的值会很大，softmax 会饱和，梯度接近 0）
- [ ] 注意力矩阵的形状是什么？(seq_len, seq_len) — 为什么？
- [ ] Self-Attention 的计算复杂度是多少？O(n^2 * d)，n 是序列长度，d 是维度

---

### Day 3 — Transformer 完整架构（3.5h）⭐⭐⭐

**学习内容：**
- Multi-Head Attention：多个注意力头并行，捕获不同类型的关系
- 位置编码（Positional Encoding）：正弦/余弦位置编码，RoPE（旋转位置编码）
- Encoder Block：Multi-Head Attention → Add & Norm → FFN → Add & Norm
- Decoder Block：Masked Multi-Head Attention → Cross Attention → FFN
- 残差连接（Residual Connection）和 Layer Normalization

**学习资源：**
- 论文："Attention Is All You Need"（可以先读博客再读论文）
  - https://arxiv.org/abs/1706.03762
- 代码实现：Harvard NLP — "The Annotated Transformer"
  - https://nlp.seas.harvard.edu/annotated-transformer/
- 视频：Andrej Karpathy — "Let's build GPT: from scratch, in code, spelled out"
  - https://www.youtube.com/watch?v=kCc8FmEb1nY （约 2 小时，强烈推荐！）

**动手实践：**
```python
import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_k = d_model // n_heads
        self.n_heads = n_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, Q, K, V, mask=None):
        batch_size = Q.size(0)

        # 线性变换并分成多头
        Q = self.W_q(Q).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        K = self.W_k(K).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        V = self.W_v(V).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        # 形状: (batch, n_heads, seq_len, d_k)

        # Scaled Dot-Product Attention
        scores = Q @ K.transpose(-2, -1) / math.sqrt(self.d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        attn = torch.softmax(scores, dim=-1)
        out = attn @ V

        # 合并多头
        out = out.transpose(1, 2).contiguous().view(batch_size, -1, self.n_heads * self.d_k)
        return self.W_o(out)

class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        self.attn = MultiHeadAttention(d_model, n_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model),
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # Self-Attention + Residual + LayerNorm
        attn_out = self.attn(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_out))
        # FFN + Residual + LayerNorm
        ffn_out = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_out))
        return x

# 测试
block = TransformerBlock(d_model=512, n_heads=8, d_ff=2048)
x = torch.randn(2, 10, 512)  # batch=2, seq_len=10, d_model=512
out = block(x)
print(f"Input: {x.shape} → Output: {out.shape}")  # 形状不变
```

**必须搞清楚的知识点（面试必问）：**
- [ ] Multi-Head 的好处是什么？（不同的头可以学习不同的注意力模式，如语法、语义）
- [ ] 为什么需要位置编码？（Attention 本身不包含位置信息，是"无序"的）
- [ ] 残差连接的作用？（缓解梯度消失，让深层网络更容易训练）
- [ ] LayerNorm vs BatchNorm 的区别？LN 对哪个维度归一化？
- [ ] FFN 层的作用？（非线性变换 + 升维再降维，增加模型表达能力）
- [ ] Decoder 中的 Mask 是什么？为什么需要？（防止看到未来的 token）

---

### Day 4 — GPT 架构精读（3.5h）

**学习内容：**
- GPT = Decoder-only Transformer
- 自回归生成（Autoregressive Generation）：一次生成一个 token
- Causal Mask（因果掩码）：只能看到之前的 token
- GPT vs BERT：生成式 vs 判别式

**学习资源：**
- Andrej Karpathy 视频（接 Day 3 的视频）
- GPT-2 论文："Language Models are Unsupervised Multitask Learners"
- nanoGPT 代码：https://github.com/karpathy/nanoGPT （简洁的 GPT 实现）

**动手实践：**
```python
# 理解自回归生成过程
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "gpt2"  # 先用小模型练手
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 手动逐 token 生成（理解自回归过程）
prompt = "The meaning of life is"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

generated = input_ids
for _ in range(20):
    with torch.no_grad():
        outputs = model(generated)
        next_token_logits = outputs.logits[:, -1, :]   # 取最后一个位置的 logits
        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)
        generated = torch.cat([generated, next_token], dim=-1)

result = tokenizer.decode(generated[0])
print(f"生成结果: {result}")
```

**必须搞清楚的知识点：**
- [ ] 自回归是什么意思？（每一步的输出作为下一步的输入）
- [ ] Causal Mask 长什么样？（下三角矩阵，对角线以上全是 -inf）
- [ ] GPT 为什么用 Decoder-only？BERT 为什么用 Encoder-only？
- [ ] Logits 是什么？（模型输出的原始分数，经过 Softmax 后变成概率）

---

### Day 5 — 模型加载与 HuggingFace 实践（3.5h）

**学习资源：**
- HuggingFace 文档：https://huggingface.co/docs/transformers/
- HuggingFace Model Hub：https://huggingface.co/models

**动手实践：**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# 1. 使用 pipeline（最简单的方式）
generator = pipeline("text-generation", model="gpt2")
result = generator("Artificial intelligence is", max_length=50)
print(result[0]["generated_text"])

# 2. 查看模型结构
model = AutoModelForCausalLM.from_pretrained("gpt2")
print(model)  # 打印完整模型架构

# 3. 统计参数量
total = sum(p.numel() for p in model.parameters())
print(f"GPT-2 参数量: {total / 1e6:.1f}M")  # ~124M

# 4. 查看模型配置
print(model.config)
# 关注：n_layer（层数）、n_head（注意力头数）、n_embd（隐藏维度）

# 5. 不同采样策略对比
input_ids = tokenizer.encode("Once upon a time", return_tensors="pt")

# Greedy（贪心）
greedy = model.generate(input_ids, max_length=50, do_sample=False)

# Top-K
topk = model.generate(input_ids, max_length=50, do_sample=True, top_k=50)

# Top-P (nucleus)
topp = model.generate(input_ids, max_length=50, do_sample=True, top_p=0.9)

# Temperature
temp = model.generate(input_ids, max_length=50, do_sample=True, temperature=0.7)

for name, ids in [("Greedy", greedy), ("Top-K", topk), ("Top-P", topp), ("Temp=0.7", temp)]:
    print(f"\n{name}: {tokenizer.decode(ids[0])}")
```

**必须搞清楚的知识点：**
- [ ] Temperature 是什么？值越高越随机还是越确定？（越高越随机）
- [ ] Top-K 和 Top-P 的区别？（Top-K 固定候选数量，Top-P 动态根据概率阈值）
- [ ] Greedy Decoding 的缺点？（容易重复、不够多样化）

---

# 第二阶段：大语言模型原理（第 5-7 周）

## 第 5 周：LLM 基础与推理过程（每天 3.5 小时）

### Day 1 — LLM 模型概览（3.5h）

**学习内容：**
- GPT 系列演进：GPT-1(117M) → GPT-2(1.5B) → GPT-3(175B) → GPT-4
- 开源模型生态：LLaMA 1/2/3、Mistral、Qwen、DeepSeek、Yi
- 模型规模：参数量(7B/13B/70B)、上下文长度(2K/4K/8K/128K)
- 模型文件格式：safetensors、bin、GGUF

**学习资源：**
- LLaMA 论文：https://arxiv.org/abs/2302.13971
- 模型对比排行：https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

**动手实践：**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

# 查看不同模型的配置（不需要下载完整模型权重）
configs = {
    "GPT-2": "gpt2",
    "LLaMA-2-7B": "meta-llama/Llama-2-7b-hf",
    "Mistral-7B": "mistralai/Mistral-7B-v0.1",
}

for name, model_id in configs.items():
    try:
        config = AutoConfig.from_pretrained(model_id)
        params = {
            "隐藏维度": getattr(config, "hidden_size", "N/A"),
            "层数": getattr(config, "num_hidden_layers", "N/A"),
            "注意力头数": getattr(config, "num_attention_heads", "N/A"),
            "词表大小": getattr(config, "vocab_size", "N/A"),
            "最大长度": getattr(config, "max_position_embeddings", "N/A"),
        }
        print(f"\n{name}: {params}")
    except Exception as e:
        print(f"{name}: 需要认证或不可用")
```

**必须搞清楚的知识点：**
- [ ] 7B 模型的 "B" 是什么？（Billion = 十亿参数）
- [ ] 7B 模型用 FP16 需要多少显存？（7B * 2 bytes = 14GB）
- [ ] 上下文长度是什么？为什么重要？
- [ ] LLaMA 相比原始 Transformer 做了哪些改进？（RoPE、RMSNorm、SwiGLU、GQA）

---

### Day 2 — LLM 推理过程详解（3.5h）⭐⭐⭐

**学习内容：**
- **Prefill 阶段**：处理整个输入提示（prompt），计算所有 token 的 KV Cache
- **Decode 阶段**：逐 token 生成，每次只处理新 token + 读取 KV Cache
- KV Cache 的原理：缓存已计算的 Key 和 Value，避免重复计算
- 为什么 Prefill 是计算密集的，Decode 是内存密集的

**学习资源：**
- 博客：https://kipp.ly/transformer-inference-arithmetic/ （推理算术：计算量与显存详细分析）
- 视频：https://www.youtube.com/watch?v=80bIUggRJf4 （NVIDIA — LLM Inference Optimization）

**动手实践：**
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

prompt = "The quick brown fox jumps over"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 对比有无 KV Cache 的推理速度
# 不使用 KV Cache（每步都重新计算所有 attention）
start = time.time()
generated_no_cache = input_ids.clone()
for _ in range(50):
    with torch.no_grad():
        outputs = model(generated_no_cache)
        next_token = outputs.logits[:, -1, :].argmax(dim=-1, keepdim=True)
        generated_no_cache = torch.cat([generated_no_cache, next_token], dim=-1)
time_no_cache = time.time() - start

# 使用 KV Cache
start = time.time()
generated_cache = input_ids.clone()
past_key_values = None
for _ in range(50):
    with torch.no_grad():
        outputs = model(
            generated_cache[:, -1:] if past_key_values else generated_cache,
            past_key_values=past_key_values,
            use_cache=True
        )
        past_key_values = outputs.past_key_values
        next_token = outputs.logits[:, -1, :].argmax(dim=-1, keepdim=True)
        generated_cache = torch.cat([generated_cache, next_token], dim=-1)
time_cache = time.time() - start

print(f"无 KV Cache: {time_no_cache:.3f}s")
print(f"有 KV Cache: {time_cache:.3f}s")
print(f"加速比: {time_no_cache / time_cache:.1f}x")

# 查看 KV Cache 的形状
print(f"\nKV Cache 层数: {len(past_key_values)}")
print(f"每层 Key 形状: {past_key_values[0][0].shape}")
print(f"每层 Value 形状: {past_key_values[0][1].shape}")
```

**必须搞清楚的知识点（面试必问）：**
- [ ] Prefill 和 Decode 分别是什么？
  - Prefill：一次性处理 prompt 中所有 token，计算并缓存 KV
  - Decode：每步只处理 1 个新 token，从 KV Cache 中读取历史信息
- [ ] KV Cache 存的是什么？（每一层的 Key 和 Value 矩阵）
- [ ] KV Cache 的显存占用怎么算？
  - = 2(K+V) * n_layers * seq_len * d_model * bytes_per_param
  - 7B 模型，seq_len=2048，FP16: 约 2 * 32 * 2048 * 4096 * 2 bytes ≈ 1GB
- [ ] 为什么 Decode 阶段是内存带宽受限的？（每步计算量小但要读取大量 KV Cache）

---

### Day 3 — Tokenizer 深入与 Embedding（3.5h）

**学习内容：**
- BPE（Byte Pair Encoding）训练过程详解
- SentencePiece 与 tiktoken 的区别
- 词嵌入层（Embedding Layer）的工作原理
- 位置编码：绝对位置编码 vs 旋转位置编码（RoPE）

**学习资源：**
- BPE 可视化：https://tiktokenizer.vercel.app/
- RoPE 论文：https://arxiv.org/abs/2104.09864
- 博客：https://blog.eleuther.ai/rotary-embeddings/

**动手实践：**
```python
# BPE 分词过程模拟
def simple_bpe(text, num_merges=10):
    """简化版 BPE 来理解原理"""
    # 初始化：每个字符是一个 token
    tokens = list(text)
    print(f"初始 tokens: {tokens}")

    for i in range(num_merges):
        # 统计所有相邻 token 对的频率
        pairs = {}
        for j in range(len(tokens) - 1):
            pair = (tokens[j], tokens[j+1])
            pairs[pair] = pairs.get(pair, 0) + 1

        if not pairs:
            break

        # 找到最频繁的对
        best_pair = max(pairs, key=pairs.get)
        new_token = best_pair[0] + best_pair[1]

        # 合并
        new_tokens = []
        j = 0
        while j < len(tokens):
            if j < len(tokens) - 1 and (tokens[j], tokens[j+1]) == best_pair:
                new_tokens.append(new_token)
                j += 2
            else:
                new_tokens.append(tokens[j])
                j += 1
        tokens = new_tokens
        print(f"Merge {i+1}: {best_pair} → '{new_token}', tokens: {tokens}")

    return tokens

simple_bpe("aaabdaaabac", num_merges=5)
```

**必须搞清楚的知识点：**
- [ ] BPE 是"贪心"算法吗？（是的，每次合并最频繁的对）
- [ ] 为什么 LLaMA 用 SentencePiece 而 GPT-4 用 tiktoken？
- [ ] RoPE 比绝对位置编码好在哪？（可以外推到更长的序列、编码相对位置信息）

---

### Day 4 — LLM 常见架构变体（3.5h）

**学习内容：**
- MHA (Multi-Head Attention) vs MQA (Multi-Query Attention) vs GQA (Grouped-Query Attention)
- RMSNorm vs LayerNorm
- SwiGLU 激活函数
- 为什么这些变化能加速推理

**学习资源：**
- GQA 论文：https://arxiv.org/abs/2305.13245
- 博客：GQA 图解 — 搜索 "Grouped Query Attention Explained"

**动手实践：**
```python
import torch
import torch.nn as nn

# 对比 MHA / MQA / GQA 的 KV Cache 大小
d_model = 4096
n_heads = 32
d_head = d_model // n_heads  # 128

# MHA: 每个 head 都有自己的 K, V
mha_kv_per_token = 2 * n_heads * d_head  # 2 * 32 * 128 = 8192

# MQA: 所有 head 共享一个 K, V
mqa_kv_per_token = 2 * 1 * d_head  # 2 * 1 * 128 = 256

# GQA: K, V 分成 n_kv_heads 组共享 (LLaMA-2 用 n_kv_heads=8)
n_kv_heads = 8
gqa_kv_per_token = 2 * n_kv_heads * d_head  # 2 * 8 * 128 = 2048

print(f"MHA KV Cache per token: {mha_kv_per_token} 元素")
print(f"MQA KV Cache per token: {mqa_kv_per_token} 元素 (MHA的 {mqa_kv_per_token/mha_kv_per_token*100:.1f}%)")
print(f"GQA KV Cache per token: {gqa_kv_per_token} 元素 (MHA的 {gqa_kv_per_token/mha_kv_per_token*100:.1f}%)")
```

**必须搞清楚的知识点：**
- [ ] MQA 为什么能加速推理？（KV Cache 小了，内存带宽需求降低）
- [ ] GQA 是 MHA 和 MQA 的折中——怎么理解？
- [ ] RMSNorm 和 LayerNorm 的公式区别？（RMSNorm 去掉了均值偏移，计算更快）

---

### Day 5 — 模型显存分析与计算量估算（3.5h）

**动手实践：**
```python
# LLM 显存估算器
def estimate_memory(
    params_billion: float,
    precision: str = "fp16",
    seq_len: int = 2048,
    batch_size: int = 1,
    n_layers: int = 32,
    d_model: int = 4096,
    n_kv_heads: int = 32,
):
    """估算 LLM 推理显存需求"""
    bytes_per_param = {"fp32": 4, "fp16": 2, "bf16": 2, "int8": 1, "int4": 0.5}
    bpp = bytes_per_param[precision]

    # 模型权重
    model_memory_gb = params_billion * 1e9 * bpp / (1024**3)

    # KV Cache
    d_head = d_model // 32  # 假设 32 个 attention heads
    kv_cache_gb = (2 * n_layers * seq_len * n_kv_heads * d_head * batch_size * 2) / (1024**3)

    # 激活值（推理时较小）
    activation_gb = batch_size * seq_len * d_model * 2 * 4 / (1024**3)  # 粗略估计

    total = model_memory_gb + kv_cache_gb + activation_gb
    print(f"=== {params_billion}B 模型 ({precision}) ===")
    print(f"模型权重: {model_memory_gb:.2f} GB")
    print(f"KV Cache: {kv_cache_gb:.2f} GB (seq_len={seq_len}, batch={batch_size})")
    print(f"激活值:   {activation_gb:.2f} GB")
    print(f"总计:     {total:.2f} GB")
    return total

# 不同场景
estimate_memory(7, "fp16", seq_len=2048)     # 7B FP16
print()
estimate_memory(7, "int4", seq_len=2048)     # 7B INT4 量化
print()
estimate_memory(70, "fp16", seq_len=4096)    # 70B FP16
```

**必须搞清楚的知识点：**
- [ ] 7B FP16 模型至少需要多少显存？（~14GB 仅权重）
- [ ] 量化到 INT4 能节省多少？（~3.5GB 仅权重，约 1/4）
- [ ] 为什么 batch size 增大时 KV Cache 成倍增长？
- [ ] 什么是 "memory-bound" vs "compute-bound"？推理时是哪个？

---

## 第 6 周：推理优化技术（一）（每天 4 小时）⭐⭐⭐ 核心周

### Day 1 — FlashAttention（4h）

**学习内容：**
- 标准 Attention 的问题：需要存储完整的 N*N 注意力矩阵
- GPU 内存层次：HBM（显存）vs SRAM（片上缓存）
- FlashAttention 核心思想：**Tiling**（分块计算）—— 不存储完整注意力矩阵
- IO-aware 算法：最小化 HBM 访问次数
- FlashAttention v1 vs v2 vs v3 的改进

**学习资源：**
- 论文：https://arxiv.org/abs/2205.14135 （FlashAttention v1）
- 论文：https://arxiv.org/abs/2307.08691 （FlashAttention v2）
- 必读博客：Tri Dao 的博客 — https://tridao.me/publications/flash2/flash2.html
- 视频：EfficientML.ai Lecture — "FlashAttention" （MIT Han Song 课程）

**动手实践：**
```python
import torch
import time

# 对比标准 Attention vs FlashAttention 性能
def standard_attention(Q, K, V):
    """标准实现 — 需要 O(N^2) 内存"""
    scores = Q @ K.transpose(-2, -1) / (Q.size(-1) ** 0.5)
    attn = torch.softmax(scores, dim=-1)  # 这个 N*N 矩阵就是内存瓶颈
    return attn @ V

# 安装 flash-attn: pip install flash-attn
# 使用 PyTorch 内置的 scaled_dot_product_attention（自动选择 FlashAttention）
def flash_attention_pytorch(Q, K, V):
    """PyTorch 2.0+ 内置 FlashAttention"""
    return torch.nn.functional.scaled_dot_product_attention(Q, K, V)

# 性能对比（需要 GPU）
if torch.cuda.is_available():
    device = "cuda"
    seq_lens = [1024, 2048, 4096, 8192]
    for seq_len in seq_lens:
        Q = torch.randn(1, 32, seq_len, 128, device=device, dtype=torch.float16)
        K = torch.randn(1, 32, seq_len, 128, device=device, dtype=torch.float16)
        V = torch.randn(1, 32, seq_len, 128, device=device, dtype=torch.float16)

        # Warmup
        for _ in range(3):
            _ = flash_attention_pytorch(Q, K, V)
        torch.cuda.synchronize()

        start = time.time()
        for _ in range(10):
            _ = flash_attention_pytorch(Q, K, V)
        torch.cuda.synchronize()
        flash_time = (time.time() - start) / 10

        print(f"seq_len={seq_len}: FlashAttn = {flash_time*1000:.2f}ms")
```

**必须搞清楚的知识点（面试高频）：**
- [ ] 标准 Attention 的内存复杂度是什么？O(N^2)，N 是序列长度
- [ ] FlashAttention 如何将内存降到 O(N)？（分块计算，不存储完整注意力矩阵）
- [ ] Tiling 是什么？为什么能减少 HBM 访问？（将数据分成小块，在 SRAM 中完成计算）
- [ ] FlashAttention 的计算量变了吗？（没有！FLOPs 一样，只是 IO 更少）
- [ ] FlashAttention v2 比 v1 改进了什么？（更好的并行化、减少非矩阵运算的 FLOPs）

---

### Day 2 — PagedAttention（4h）

**学习内容：**
- 传统 KV Cache 管理的问题：预分配连续内存 → 内存碎片 + 浪费
- PagedAttention 核心思想：借鉴操作系统的虚拟内存/分页机制
- Block 概念：KV Cache 被分成固定大小的 Block，按需分配
- Block Table：映射逻辑块到物理块

**学习资源：**
- vLLM 论文（必读）：https://arxiv.org/abs/2309.06180
  - "Efficient Memory Management for Large Language Model Serving with PagedAttention"
- 博客：https://blog.vllm.ai/2023/06/20/vllm.html （vLLM 官方博客）
- 视频：vLLM 作者 Woosuk Kwon 的演讲（YouTube 搜索 "vLLM PagedAttention"）

**动手实践：**
```python
# PagedAttention 概念模拟
class SimplePagedKVCache:
    """模拟 PagedAttention 的内存管理"""
    def __init__(self, block_size=16, num_blocks=100, d_model=128):
        self.block_size = block_size    # 每个 block 存多少个 token 的 KV
        self.d_model = d_model
        # 物理内存池（预分配）
        self.k_pool = [None] * num_blocks  # 物理 block 池
        self.v_pool = [None] * num_blocks
        self.free_blocks = list(range(num_blocks))  # 空闲 block 列表

        # 每个 sequence 的 block table
        self.block_tables = {}  # seq_id → [physical_block_id, ...]

    def allocate_block(self):
        if not self.free_blocks:
            raise RuntimeError("OOM: 没有空闲 block")
        block_id = self.free_blocks.pop(0)
        return block_id

    def append_token(self, seq_id, k_vector, v_vector):
        """为 sequence 追加一个 token 的 KV"""
        if seq_id not in self.block_tables:
            self.block_tables[seq_id] = []

        table = self.block_tables[seq_id]
        total_tokens = sum(
            self.block_size if self.k_pool[bid] is not None and len(self.k_pool[bid]) == self.block_size
            else (len(self.k_pool[bid]) if self.k_pool[bid] is not None else 0)
            for bid in table
        )

        # 检查当前最后一个 block 是否已满
        need_new_block = (len(table) == 0)
        if not need_new_block and self.k_pool[table[-1]] is not None:
            need_new_block = (len(self.k_pool[table[-1]]) >= self.block_size)

        if need_new_block:
            new_block = self.allocate_block()
            table.append(new_block)
            self.k_pool[new_block] = []
            self.v_pool[new_block] = []

        last_block = table[-1]
        self.k_pool[last_block].append(k_vector)
        self.v_pool[last_block].append(v_vector)

    def free_sequence(self, seq_id):
        """释放 sequence 占用的所有 block"""
        if seq_id in self.block_tables:
            for bid in self.block_tables[seq_id]:
                self.k_pool[bid] = None
                self.v_pool[bid] = None
                self.free_blocks.append(bid)
            del self.block_tables[seq_id]

    def stats(self):
        used = sum(1 for b in self.k_pool if b is not None)
        total = len(self.k_pool)
        print(f"Block 使用率: {used}/{total} ({used/total*100:.1f}%)")
        print(f"空闲 Block: {len(self.free_blocks)}")

# 模拟多个请求并发
cache = SimplePagedKVCache(block_size=4, num_blocks=20, d_model=64)

# 请求 1：10 个 token
for i in range(10):
    cache.append_token("req_1", f"k1_{i}", f"v1_{i}")

# 请求 2：6 个 token
for i in range(6):
    cache.append_token("req_2", f"k2_{i}", f"v2_{i}")

cache.stats()
print(f"请求1 用了 {len(cache.block_tables['req_1'])} 个 block")
print(f"请求2 用了 {len(cache.block_tables['req_2'])} 个 block")

# 请求 1 完成，释放
cache.free_sequence("req_1")
cache.stats()  # 空闲 block 增加了
```

**必须搞清楚的知识点（面试高频）：**
- [ ] 传统 KV Cache 为什么浪费内存？（预分配 max_seq_len 大小的连续内存，实际可能用不完）
- [ ] PagedAttention 和操作系统的虚拟内存有什么类比？
  - Block ↔ Page
  - Block Table ↔ Page Table
  - 物理 Block 池 ↔ 物理内存
- [ ] Block Size 大小的权衡？（太小 → 管理开销大；太大 → 内部碎片多）
- [ ] PagedAttention 带来了多少内存节省？（论文称 ~60-80% 的显存浪费被消除）

---

### Day 3 — Continuous Batching（4h）

**学习内容：**
- 静态 Batching 的问题：一批请求中最长的决定了所有请求的等待时间
- Continuous Batching（也叫 iteration-level scheduling）：
  - 每个 decode step 都可以加入新请求或移除已完成的请求
  - 大幅提升 GPU 利用率和吞吐量
- Prefill 和 Decode 的调度策略

**学习资源：**
- 论文：Orca（https://www.usenix.org/conference/osdi22/presentation/yu）
  - "Orca: A Distributed Serving System for Transformer-Based Generative Models"
- 博客：https://www.anyscale.com/blog/continuous-batching-llm-inference

**动手实践：**
```python
import time
import random

# 模拟 Static Batching vs Continuous Batching
class StaticBatcher:
    """静态批处理：等所有请求完成才处理下一批"""
    def process(self, requests):
        """requests: [(prompt_len, output_len), ...]"""
        total_time = 0
        batch_size = 4

        for i in range(0, len(requests), batch_size):
            batch = requests[i:i+batch_size]
            # 所有请求必须等最长的那个完成
            max_output = max(r[1] for r in batch)
            batch_time = max_output * 0.01  # 假设每个 decode step 10ms
            total_time += batch_time

            wasted_steps = sum(max_output - r[1] for r in batch)
            print(f"  Batch {i//batch_size}: max_steps={max_output}, "
                  f"wasted_steps={wasted_steps}")

        return total_time

class ContinuousBatcher:
    """连续批处理：请求完成立即替换"""
    def process(self, requests):
        total_time = 0
        active = []
        queue = list(requests)
        batch_size = 4
        step = 0

        # 初始填满
        while queue and len(active) < batch_size:
            active.append({"remaining": queue.pop(0)[1], "id": step})
            step += 1

        while active:
            total_time += 0.01  # 一个 decode step

            # 减少所有活跃请求的剩余步数
            for req in active:
                req["remaining"] -= 1

            # 移除完成的请求
            completed = [r for r in active if r["remaining"] <= 0]
            active = [r for r in active if r["remaining"] > 0]

            # 从队列中补充新请求
            while queue and len(active) < batch_size:
                active.append({"remaining": queue.pop(0)[1], "id": step})
                step += 1

        return total_time

# 模拟 20 个请求，输出长度差异很大
random.seed(42)
requests = [(50, random.randint(10, 200)) for _ in range(20)]
print("请求输出长度:", [r[1] for r in requests])

print("\n=== Static Batching ===")
t1 = StaticBatcher().process(requests)
print(f"总时间: {t1:.2f}s")

print("\n=== Continuous Batching ===")
t2 = ContinuousBatcher().process(requests)
print(f"总时间: {t2:.2f}s")
print(f"\nContinuous Batching 快 {t1/t2:.1f}x")
```

**必须搞清楚的知识点：**
- [ ] 为什么静态 Batching 效率低？（短请求必须等长请求完成，GPU 空闲计算能力被浪费）
- [ ] Continuous Batching 如何解决？（请求级调度 → iteration 级调度）
- [ ] Prefill 请求和 Decode 请求能不能混在同一个 batch？（可以，但需要分开处理）

---

### Day 4 — Speculative Decoding（4h）

**学习内容：**
- 核心思想：用一个小模型（draft model）快速猜测多个 token，再用大模型一次性验证
- 为什么能加速？大模型验证 N 个 token 的时间 ≈ 生成 1 个 token 的时间
- 接受/拒绝策略：保证输出分布与原始大模型完全一致
- 加速比取决于 draft model 的准确率

**学习资源：**
- 论文：https://arxiv.org/abs/2211.17192 （"Fast Inference from Transformers via Speculative Decoding"）
- 论文：https://arxiv.org/abs/2302.01318 （"Speculative Decoding with Big Little Decoder"）
- 博客：搜索 "Speculative Decoding Explained"

**动手实践：**
```python
import random

def speculative_decoding_simulation(
    draft_accuracy=0.8,    # 小模型的预测准确率
    num_speculative=5,     # 每次猜测的 token 数
    total_tokens=100,      # 需要生成的总 token 数
    draft_cost=0.1,        # 小模型生成一个 token 的时间（相对单位）
    verify_cost=1.0,       # 大模型验证一次的时间（不管验证几个 token）
):
    """模拟投机解码过程"""
    generated = 0
    total_cost = 0
    steps = 0

    while generated < total_tokens:
        steps += 1

        # Step 1: Draft model 快速生成 num_speculative 个 token
        draft_tokens = []
        for _ in range(num_speculative):
            is_correct = random.random() < draft_accuracy
            draft_tokens.append(is_correct)
        total_cost += num_speculative * draft_cost

        # Step 2: 大模型一次性验证所有 draft token
        total_cost += verify_cost
        accepted = 0
        for correct in draft_tokens:
            if correct:
                accepted += 1
            else:
                accepted += 1  # 拒绝的位置由大模型重新生成，也算 1 个 token
                break

        generated += accepted

    # 对比：纯大模型逐 token 生成
    baseline_cost = total_tokens * verify_cost

    print(f"=== Speculative Decoding (accuracy={draft_accuracy}) ===")
    print(f"总 token: {total_tokens}")
    print(f"总步数: {steps}")
    print(f"每步平均接受: {total_tokens/steps:.1f} token")
    print(f"投机解码总耗时: {total_cost:.1f}")
    print(f"纯大模型总耗时: {baseline_cost:.1f}")
    print(f"加速比: {baseline_cost/total_cost:.2f}x")

# 不同准确率的对比
for acc in [0.5, 0.7, 0.8, 0.9, 0.95]:
    random.seed(42)
    speculative_decoding_simulation(draft_accuracy=acc)
    print()
```

**必须搞清楚的知识点：**
- [ ] 为什么大模型验证 K 个 token 和生成 1 个 token 的时间差不多？（都是一次前向传播）
- [ ] Draft model 准确率越高加速比越高——为什么？
- [ ] Speculative Decoding 会改变最终输出的分布吗？（不会！通过接受/拒绝策略保证一致性）
- [ ] Draft model 通常是什么？（同系列小模型，如用 LLaMA-7B 做 LLaMA-70B 的 draft）

---

### Day 5 — 复习与整合（4h）

**任务：**
1. 画一张思维导图，把以下技术的关系梳理清楚：
   - KV Cache → PagedAttention（KV Cache 的高效管理）
   - Standard Attention → FlashAttention（Attention 计算的优化）
   - Static Batching → Continuous Batching（请求调度的优化）
   - Sequential Decoding → Speculative Decoding（生成速度的优化）
2. 用自己的话写一段总结，解释每个技术解决了什么问题

---

## 第 7 周：推理优化技术（二）— 量化、剪枝、分布式（每天 4 小时）⭐⭐⭐

### Day 1 — 量化基础（4h）

**学习内容：**
- 数据类型：FP32 / FP16 / BF16 / INT8 / INT4 / FP8
- FP16 vs BF16：为什么训练/推理偏好 BF16？（更大的动态范围）
- 量化的本质：用更少的 bit 表示权重/激活值，牺牲少量精度换取速度和内存
- PTQ（Post-Training Quantization）vs QAT（Quantization-Aware Training）

**学习资源：**
- NVIDIA 量化白皮书：搜索 "NVIDIA Integer Quantization for Deep Learning Inference"
- HuggingFace 量化指南：https://huggingface.co/docs/transformers/quantization
- 博客：https://huggingface.co/blog/hf-bitsandbytes-integration

**动手实践：**
```python
import struct
import numpy as np

# 理解不同精度的数据表示
def show_float_format(value):
    """展示一个数在不同精度下的存储"""
    # FP32: 1 sign + 8 exponent + 23 mantissa = 32 bits
    fp32 = np.float32(value)
    fp32_bytes = struct.pack('f', fp32)

    # FP16: 1 sign + 5 exponent + 10 mantissa = 16 bits
    fp16 = np.float16(value)

    # BF16: 1 sign + 8 exponent + 7 mantissa = 16 bits
    # BF16 和 FP32 有相同的 exponent 范围，但 mantissa 更少

    print(f"值: {value}")
    print(f"  FP32: {fp32} (4 bytes)")
    print(f"  FP16: {fp16} (2 bytes)")
    print(f"  FP16 范围: [{np.finfo(np.float16).min}, {np.finfo(np.float16).max}]")
    print(f"  FP32 范围: [{np.finfo(np.float32).min}, {np.finfo(np.float32).max}]")

show_float_format(3.14159)
show_float_format(65536.0)   # 注意 FP16 溢出！

# 简单的 INT8 量化模拟
def quantize_int8(tensor):
    """对称 INT8 量化"""
    scale = tensor.abs().max() / 127
    quantized = np.round(tensor / scale).astype(np.int8)
    return quantized, scale

def dequantize_int8(quantized, scale):
    return quantized.astype(np.float32) * scale

# 量化-反量化，观察精度损失
original = np.random.randn(10).astype(np.float32)
quantized, scale = quantize_int8(original)
recovered = dequantize_int8(quantized, scale)

print(f"\n原始值:   {original[:5]}")
print(f"量化后:   {quantized[:5]}")
print(f"反量化后: {recovered[:5]}")
print(f"最大误差: {np.max(np.abs(original - recovered)):.6f}")
```

**必须搞清楚的知识点：**
- [ ] FP16 最大能表示多大的数？（~65504）BF16 呢？（~3.4e38，和 FP32 一样）
- [ ] 为什么 BF16 在训练中更受欢迎？（不容易溢出，但精度比 FP16 低一点）
- [ ] 对称量化 vs 非对称量化的区别？
- [ ] 量化误差如何衡量？（通常看模型精度指标如 Perplexity 的变化）

---

### Day 2 — AWQ 量化（4h）

**学习内容：**
- AWQ = Activation-aware Weight Quantization
- 核心观察：权重中只有少数（~1%）对激活值影响很大（salient weights）
- 对 salient weights 做特殊处理（乘以一个 scale 再量化），而不是简单均匀量化
- AWQ 的优势：不需要校准数据集，速度快

**学习资源：**
- 论文：https://arxiv.org/abs/2306.00978
- MIT Han Song 课程 Lecture：搜索 "EfficientML AWQ"
- GitHub：https://github.com/mit-han-lab/llm-awq

**动手实践：**
```python
# 使用 AWQ 量化模型（实际操作）
# pip install autoawq

# 概念演示：为什么 salient weight 很重要
import numpy as np

np.random.seed(42)
# 模拟权重矩阵
weights = np.random.randn(100, 100).astype(np.float32) * 0.1

# 假设某些权重特别重要（salient）
salient_indices = [(5, 10), (20, 30), (50, 60)]
for i, j in salient_indices:
    weights[i, j] = 2.5  # 这些权重对输出影响很大

# 直接 INT4 量化
def naive_quantize_int4(w):
    scale = w.abs().max() / 7
    q = np.clip(np.round(w / scale), -8, 7).astype(np.int8)
    return q, scale

q_naive, s_naive = naive_quantize_int4(weights)
recovered_naive = q_naive.astype(np.float32) * s_naive

# AWQ 思路：先对 salient weight 进行缩放保护
def awq_quantize_int4(w, salient_mask, protect_scale=4.0):
    """简化版 AWQ：保护重要权重"""
    # Step 1: 对重要权重乘以一个大的 scale
    w_scaled = w.copy()
    w_scaled[salient_mask] *= protect_scale

    # Step 2: 量化
    scale = w_scaled.abs().max() / 7
    q = np.clip(np.round(w_scaled / scale), -8, 7).astype(np.int8)

    return q, scale, protect_scale

salient_mask = np.zeros_like(weights, dtype=bool)
for i, j in salient_indices:
    salient_mask[i, j] = True

q_awq, s_awq, ps = awq_quantize_int4(weights, salient_mask)
recovered_awq = q_awq.astype(np.float32) * s_awq
recovered_awq[salient_mask] /= ps  # 反缩放

# 对比重要权重的量化误差
for i, j in salient_indices:
    err_naive = abs(weights[i,j] - recovered_naive[i,j])
    err_awq = abs(weights[i,j] - recovered_awq[i,j])
    print(f"位置({i},{j}): 原始={weights[i,j]:.4f}, "
          f"Naive误差={err_naive:.4f}, AWQ误差={err_awq:.4f}")
```

**必须搞清楚的知识点：**
- [ ] AWQ 中 "Activation-aware" 是什么意思？（根据激活值的大小来判断哪些权重重要）
- [ ] 为什么不直接跳过 salient weights 不量化？（会导致混合精度计算，硬件效率低）
- [ ] AWQ vs RTN（Round-To-Nearest 最简单的量化）精度差多少？

---

### Day 3 — GPTQ 量化（4h）

**学习内容：**
- GPTQ = GPT Quantization，基于 OBQ（Optimal Brain Quantization）
- 核心思想：逐层量化，用 Hessian 矩阵来最小化量化误差
- 量化过程：逐列量化权重，用剩余列补偿已量化列的误差
- GPTQ vs AWQ 对比

**学习资源：**
- 论文：https://arxiv.org/abs/2210.17323
- GitHub：https://github.com/IST-DASLab/gptq
- AutoGPTQ：https://github.com/AutoGPTQ/AutoGPTQ

**动手实践：**
```bash
# 使用 AutoGPTQ 量化模型
pip install auto-gptq
```
```python
# 概念理解：GPTQ 的逐列量化
import numpy as np

def simplified_gptq(W, n_bits=4):
    """
    极简版 GPTQ 演示（真正的 GPTQ 用 Hessian 矩阵）
    核心思想：量化一列后，用其他列补偿误差
    """
    rows, cols = W.shape
    Q = np.zeros_like(W)  # 量化后的权重
    max_val = 2**(n_bits-1) - 1

    for j in range(cols):
        # 量化第 j 列
        scale = np.abs(W[:, j]).max() / max_val
        if scale == 0:
            scale = 1e-8
        Q[:, j] = np.clip(np.round(W[:, j] / scale), -max_val-1, max_val) * scale

        # 计算量化误差
        error = W[:, j] - Q[:, j]

        # 将误差分散到未量化的列中（误差补偿）
        if j + 1 < cols:
            # 简化：均匀分散到剩余列
            W[:, j+1:] += error[:, None] / (cols - j - 1)

    return Q

# 测试
np.random.seed(42)
W = np.random.randn(64, 64).astype(np.float32)
Q = simplified_gptq(W, n_bits=4)

mse = np.mean((W - Q) ** 2)
print(f"GPTQ 量化 MSE: {mse:.6f}")

# 对比直接 Round-To-Nearest
scale = np.abs(W).max() / 7
Q_rtn = np.clip(np.round(W / scale), -8, 7) * scale
mse_rtn = np.mean((W - Q_rtn) ** 2)
print(f"RTN 量化 MSE: {mse_rtn:.6f}")
print(f"GPTQ 误差减少: {(1 - mse/mse_rtn)*100:.1f}%")
```

**必须搞清楚的知识点：**
- [ ] GPTQ 为什么比简单量化精度高？（误差补偿机制——一列的量化误差会被其他列补偿）
- [ ] GPTQ 需要校准数据集吗？（需要少量，通常 128 条样本）
- [ ] AWQ vs GPTQ 对比：
  - AWQ：更快、不需要校准数据、推理速度更快
  - GPTQ：精度通常更高、需要校准数据、量化过程更慢

---

### Day 4 — 模型剪枝（Pruning）（4h）

**学习内容：**
- 非结构化剪枝：将单个权重置零（稀疏矩阵）
- 结构化剪枝：移除整个神经元/通道/注意力头
- 稀疏性（Sparsity）：如 50% sparsity = 一半的权重为 0
- SparseGPT、Wanda 等 LLM 剪枝方法
- 稀疏矩阵加速：NVIDIA Sparse Tensor Core（2:4 稀疏模式）

**学习资源：**
- SparseGPT：https://arxiv.org/abs/2301.00774
- Wanda：https://arxiv.org/abs/2306.11695
- NVIDIA 2:4 稀疏：https://developer.nvidia.com/blog/accelerating-sparse-deep-neural-networks/

**动手实践：**
```python
import torch
import torch.nn as nn

# 非结构化剪枝 vs 结构化剪枝
def magnitude_pruning(weight, sparsity=0.5):
    """按权重绝对值大小剪枝（非结构化）"""
    threshold = torch.quantile(weight.abs().flatten(), sparsity)
    mask = weight.abs() > threshold
    return weight * mask, mask

# 演示
linear = nn.Linear(100, 50)
original_weight = linear.weight.data.clone()

pruned_weight, mask = magnitude_pruning(original_weight, sparsity=0.5)
print(f"原始非零权重: {(original_weight != 0).sum().item()}")
print(f"剪枝后非零权重: {(pruned_weight != 0).sum().item()}")
print(f"稀疏度: {1 - pruned_weight.count_nonzero().item() / pruned_weight.numel():.1%}")

# 2:4 稀疏模式（NVIDIA Ampere+ GPU 硬件支持）
def apply_2_4_sparsity(weight):
    """
    2:4 稀疏：每 4 个连续元素中，保留 2 个最大的，其余置零
    这种模式可以被 Tensor Core 硬件加速
    """
    rows, cols = weight.shape
    sparse_weight = weight.clone()
    for i in range(rows):
        for j in range(0, cols, 4):
            group = weight[i, j:j+4].abs()
            # 找到最小的 2 个，置零
            _, indices = group.topk(2, largest=False)
            for idx in indices:
                sparse_weight[i, j + idx] = 0
    return sparse_weight

w = torch.randn(4, 8)
w_sparse = apply_2_4_sparsity(w)
print(f"\n原始权重:\n{w}")
print(f"\n2:4 稀疏:\n{w_sparse}")
```

**必须搞清楚的知识点：**
- [ ] 非结构化剪枝为什么难以获得实际加速？（稀疏矩阵不规则，GPU 不擅长处理）
- [ ] 结构化剪枝为什么更容易加速？（直接减少矩阵维度）
- [ ] 2:4 稀疏模式为什么 NVIDIA 硬件支持？（Tensor Core 有专门的稀疏计算指令）

---

### Day 5 — 分布式推理（4h）

**学习内容：**
- Tensor Parallelism (TP)：将一层的矩阵运算拆分到多个 GPU
- Pipeline Parallelism (PP)：将不同层放在不同 GPU
- TP vs PP 的适用场景
- 通信开销：AllReduce、AllGather

**学习资源：**
- Megatron-LM 论文：https://arxiv.org/abs/1909.08053
- 博客：https://huggingface.co/docs/transformers/parallelism

**动手实践：**
```python
# 理解 Tensor Parallelism 的原理
import numpy as np

# 假设要计算 Y = XW，W 太大放不下一个 GPU
X = np.random.randn(4, 8)     # 输入
W = np.random.randn(8, 16)    # 大权重矩阵

# 完整计算（单 GPU）
Y_full = X @ W

# Tensor Parallelism：列并行
# 把 W 按列拆成 2 份，分到 2 个 GPU
W_gpu0 = W[:, :8]     # GPU 0 拿前 8 列
W_gpu1 = W[:, 8:]     # GPU 1 拿后 8 列

Y_gpu0 = X @ W_gpu0   # GPU 0 计算
Y_gpu1 = X @ W_gpu1   # GPU 1 计算

# AllGather: 将结果拼接
Y_tp = np.concatenate([Y_gpu0, Y_gpu1], axis=1)
print(f"TP 结果正确: {np.allclose(Y_full, Y_tp)}")

# Pipeline Parallelism 概念
# Layer 0-15 在 GPU 0，Layer 16-31 在 GPU 1
# GPU 0 计算完一层的输出，发送给 GPU 1 继续
print(f"\nPipeline Parallelism:")
print(f"  GPU 0: Layer 0-15 → 输出发送给 GPU 1")
print(f"  GPU 1: Layer 16-31 → 最终输出")
print(f"  缺点: GPU 间传输增加延迟")
print(f"  优点: 每个 GPU 只需要存一半的模型权重")
```

**必须搞清楚的知识点：**
- [ ] TP 适合什么场景？（同一台机器内的多 GPU，通信带宽高）
- [ ] PP 适合什么场景？（跨机器，或者 TP 度数不够时）
- [ ] AllReduce 和 AllGather 分别做什么？
- [ ] 70B 模型需要几张 A100-80GB 才能推理？（FP16: ~140GB → 至少 2 张）

---

# 第三阶段：GPU 与 CUDA（第 8-10 周）

## 第 8 周：GPU 硬件架构（每天 3.5 小时）

### Day 1 — GPU vs CPU 架构（3.5h）

**学习内容：**
- CPU：少数高性能核心，优化延迟（Latency-oriented）
- GPU：数千个简单核心，优化吞吐（Throughput-oriented）
- SIMT（Single Instruction, Multiple Threads）执行模型
- SM（Streaming Multiprocessor）内部结构

**学习资源：**
- NVIDIA CUDA C Programming Guide 第 1-3 章：
  https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- 视频：NVIDIA GTC "How GPU Computing Works"
- 书籍：《Programming Massively Parallel Processors》第 1-3 章

**必须搞清楚的知识点：**
- [ ] 为什么 GPU 适合深度学习？（大量矩阵乘法 = 大量并行计算）
- [ ] 一个 SM 包含什么？（CUDA Cores、Tensor Cores、共享内存、寄存器文件）
- [ ] A100 有多少个 SM？多少个 CUDA Core？（108 SM, 6912 CUDA Cores）

### Day 2 — GPU 内存层次（3.5h）

**学习内容：**
- 全局内存（Global Memory / HBM）：最大但最慢（~2TB/s for A100）
- 共享内存（Shared Memory / SRAM）：小但快（~19TB/s）
- 寄存器（Registers）：最快但最少
- L1/L2 Cache

**动手实践：**
```bash
# 查看 GPU 内存信息
nvidia-smi
nvidia-smi --query-gpu=memory.total,memory.used,memory.free --format=csv
```

**必须搞清楚的知识点：**
- [ ] A100 的 HBM 带宽是多少？（2TB/s）SRAM 呢？（~19TB/s）
- [ ] 为什么 FlashAttention 要把计算放在 SRAM 中？（带宽差 10x）
- [ ] 什么是 Bank Conflict？如何避免？

### Day 3 — Tensor Core 与 Roofline Model（3.5h）

**学习内容：**
- Tensor Core：专门的矩阵乘法硬件（FP16/BF16/INT8/FP8）
- Arithmetic Intensity = FLOPs / Bytes（计算密度）
- Roofline Model：判断任务是计算密集还是内存密集

**学习资源：**
- NVIDIA Tensor Core 白皮书
- Roofline Model 入门：https://crd.lbl.gov/assets/Uploads/ECP20-Roofline-intro.pdf

**必须搞清楚的知识点：**
- [ ] A100 的 FP16 Tensor Core 算力是多少？（312 TFLOPS）
- [ ] LLM 推理中 Prefill 和 Decode 分别在 Roofline 图上的位置？
- [ ] 如果程序是内存密集型的，买更强的 GPU（更高 FLOPS）有用吗？（没用，瓶颈在内存带宽）

### Day 4-5 — NVIDIA GPU 架构演进 + nvidia-smi 详解（7h）

**学习内容：**
- Volta (V100) → Turing (T4) → Ampere (A100) → Hopper (H100) → Blackwell (B200)
- 每代的关键特性提升
- nvidia-smi 所有字段的含义
- CUDA 版本 vs Driver 版本的关系

**动手实践：**
```bash
# nvidia-smi 详解
nvidia-smi

# 查看详细信息
nvidia-smi -q

# 持续监控（每秒刷新）
nvidia-smi dmon -s pucvmet -d 1

# 查看 CUDA 版本
nvcc --version

# Python 中查看 GPU
python3 -c "
import torch
if torch.cuda.is_available():
    print(f'GPU: {torch.cuda.get_device_name(0)}')
    print(f'显存: {torch.cuda.get_device_properties(0).total_mem / 1024**3:.1f} GB')
    print(f'Compute Capability: {torch.cuda.get_device_capability(0)}')
    print(f'CUDA: {torch.version.cuda}')
"
```

---

## 第 9 周：CUDA 编程入门（每天 3.5 小时）

### Day 1-2 — CUDA 编程基础（7h）

**学习资源：**
- NVIDIA CUDA Samples: https://github.com/NVIDIA/cuda-samples
- 书籍：《CUDA by Example》（入门最友好）
- 在线课程：https://developer.nvidia.com/cuda-education

**动手实践：**
```c
// vector_add.cu — 第一个 CUDA 程序
#include <stdio.h>

// GPU kernel 函数
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1000000;
    size_t size = n * sizeof(float);

    // 分配 Host 内存
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // 初始化
    for (int i = 0; i < n; i++) {
        h_a[i] = 1.0f;
        h_b[i] = 2.0f;
    }

    // 分配 Device 内存
    float *d_a, *d_b, *d_c;
    cudaMalloc(&d_a, size);
    cudaMalloc(&d_b, size);
    cudaMalloc(&d_c, size);

    // 拷贝数据到 GPU
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // 启动 kernel
    int blockSize = 256;
    int numBlocks = (n + blockSize - 1) / blockSize;
    vectorAdd<<<numBlocks, blockSize>>>(d_a, d_b, d_c, n);

    // 拷贝结果回 CPU
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    printf("c[0] = %f (expected 3.0)\n", h_c[0]);

    // 释放内存
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
    free(h_a); free(h_b); free(h_c);
    return 0;
}
// 编译: nvcc vector_add.cu -o vector_add
```

**必须搞清楚的知识点：**
- [ ] `__global__` 函数在哪里运行？由谁调用？（GPU 运行，CPU 调用）
- [ ] `blockIdx.x * blockDim.x + threadIdx.x` 怎么理解？（计算全局线程 ID）
- [ ] `<<<numBlocks, blockSize>>>` 的含义？（Grid 和 Block 的维度）
- [ ] 为什么需要 `cudaMemcpy`？（CPU 和 GPU 有独立的内存空间）

### Day 3 — 共享内存与矩阵乘法（3.5h）

**动手实践：**
```c
// 用共享内存优化矩阵乘法
__global__ void matmul_shared(float *A, float *B, float *C, int N) {
    __shared__ float sA[16][16];  // 共享内存（所有线程共享）
    __shared__ float sB[16][16];

    int row = blockIdx.y * 16 + threadIdx.y;
    int col = blockIdx.x * 16 + threadIdx.x;
    float sum = 0.0f;

    for (int t = 0; t < N / 16; t++) {
        // 协作加载数据到共享内存
        sA[threadIdx.y][threadIdx.x] = A[row * N + t * 16 + threadIdx.x];
        sB[threadIdx.y][threadIdx.x] = B[(t * 16 + threadIdx.y) * N + col];
        __syncthreads();  // 确保所有线程都加载完

        // 从共享内存计算（快！）
        for (int k = 0; k < 16; k++)
            sum += sA[threadIdx.y][k] * sB[k][threadIdx.x];
        __syncthreads();
    }

    C[row * N + col] = sum;
}
```

**必须搞清楚的知识点：**
- [ ] 共享内存比全局内存快多少？（~10-100x）
- [ ] `__syncthreads()` 为什么必要？（同步 block 内所有线程，确保数据已加载）
- [ ] Warp 是什么？一个 Warp 有多少线程？（32 个线程同步执行）

### Day 4-5 — Nsight Systems & Nsight Compute（7h）

**学习资源：**
- NVIDIA Nsight Systems 文档：https://docs.nvidia.com/nsight-systems/
- NVIDIA Nsight Compute 文档：https://docs.nvidia.com/nsight-compute/

**动手实践：**
```bash
# Nsight Systems: 生成 timeline
nsys profile -o my_profile python3 my_inference_script.py
# 用 nsight-sys GUI 打开 .nsys-rep 文件

# Nsight Compute: 分析单个 kernel
ncu --set full python3 my_script.py
# 查看 kernel 的 occupancy, memory throughput, compute throughput 等
```

**必须搞清楚的知识点：**
- [ ] Nsight Systems 和 Nsight Compute 的区别？（Systems 看全局 timeline，Compute 看单个 kernel）
- [ ] Occupancy 是什么？为什么重要？（SM 上活跃 warp 的比例，越高通常越好）
- [ ] 如何从 profile 结果判断是内存瓶颈还是计算瓶颈？

---

## 第 10 周：CUDA 进阶与 cuBLAS/cuDNN（每天 3.5 小时）

### Day 1-2 — CUDA Streams 与异步执行（7h）

**动手实践：**
```c
// CUDA Streams: 让计算和内存传输重叠
cudaStream_t stream1, stream2;
cudaStreamCreate(&stream1);
cudaStreamCreate(&stream2);

// Stream 1: 传输 + 计算
cudaMemcpyAsync(d_a, h_a, size/2, cudaMemcpyHostToDevice, stream1);
kernel<<<grid, block, 0, stream1>>>(d_a, ...);

// Stream 2: 同时传输 + 计算另一半
cudaMemcpyAsync(d_b, h_b, size/2, cudaMemcpyHostToDevice, stream2);
kernel<<<grid, block, 0, stream2>>>(d_b, ...);

cudaStreamSynchronize(stream1);
cudaStreamSynchronize(stream2);
```

### Day 3-5 — cuBLAS / cuDNN / CUTLASS（10.5h）

**学习内容：**
- cuBLAS：GPU 上的 BLAS（基本线性代数）库，核心是 GEMM
- cuDNN：深度学习原语库（卷积、激活、Attention 等）
- CUTLASS：NVIDIA 的模板化 CUDA GEMM 库

**必须搞清楚的知识点：**
- [ ] GEMM 是什么？为什么是深度学习的核心？（General Matrix Multiplication，占了 >90% 计算）
- [ ] 什么时候用 cuBLAS vs 自己写 CUDA kernel？（除非有特殊需求，否则用库）

---

# 第四阶段：推理引擎实战（第 11-13 周）

## 第 11 周：vLLM 深入（每天 4 小时）⭐⭐⭐

### Day 1 — vLLM 安装与使用（4h）

**学习资源：**
- GitHub：https://github.com/vllm-project/vllm
- 文档：https://docs.vllm.ai/en/latest/

**动手实践：**
```bash
# 安装
pip install vllm

# 离线推理
python3 -c "
from vllm import LLM, SamplingParams
llm = LLM(model='facebook/opt-1.3b')  # 用小模型练习
params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=100)
outputs = llm.generate(['The future of AI is'], params)
print(outputs[0].outputs[0].text)
"

# API Server 模式
python3 -m vllm.entrypoints.openai.api_server \
    --model facebook/opt-1.3b \
    --port 8000

# 测试 API
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{"model": "facebook/opt-1.3b", "prompt": "Hello", "max_tokens": 50}'
```

### Day 2-3 — vLLM 架构与源码（8h）

**重点阅读的源码文件：**
```
vllm/
├── engine/
│   ├── llm_engine.py        # 核心引擎
│   └── async_llm_engine.py  # 异步引擎
├── core/
│   ├── scheduler.py         # 调度器（Continuous Batching 实现）
│   └── block_manager.py     # Block 管理（PagedAttention 内存管理）
├── worker/
│   └── worker.py            # GPU Worker
├── model_executor/
│   └── models/              # 各模型实现
└── entrypoints/
    └── openai/              # OpenAI 兼容 API
```

### Day 4-5 — vLLM 性能测试（8h）

**动手实践：**
```python
# vLLM 性能测试脚本
import time
import requests
import concurrent.futures

def benchmark_vllm(
    url="http://localhost:8000/v1/completions",
    model="facebook/opt-1.3b",
    num_requests=100,
    concurrency=10,
    max_tokens=100,
):
    """测试 vLLM 的吞吐量和延迟"""
    prompts = [f"Write a story about topic {i}" for i in range(num_requests)]
    results = []

    def send_request(prompt):
        start = time.time()
        response = requests.post(url, json={
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": 0.7,
        })
        latency = time.time() - start
        data = response.json()
        output_tokens = data["usage"]["completion_tokens"]
        return {
            "latency": latency,
            "output_tokens": output_tokens,
            "tps": output_tokens / latency,  # Tokens per second
        }

    start_all = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        results = list(executor.map(send_request, prompts))
    total_time = time.time() - start_all

    latencies = [r["latency"] for r in results]
    total_tokens = sum(r["output_tokens"] for r in results)

    print(f"=== vLLM Benchmark ===")
    print(f"总请求数: {num_requests}")
    print(f"并发数: {concurrency}")
    print(f"总时间: {total_time:.2f}s")
    print(f"吞吐量: {total_tokens / total_time:.1f} tokens/s")
    print(f"平均延迟: {sum(latencies)/len(latencies):.3f}s")
    print(f"P50 延迟: {sorted(latencies)[len(latencies)//2]:.3f}s")
    print(f"P95 延迟: {sorted(latencies)[int(len(latencies)*0.95)]:.3f}s")
    print(f"P99 延迟: {sorted(latencies)[int(len(latencies)*0.99)]:.3f}s")

benchmark_vllm()
```

---

## 第 12 周：TensorRT / TensorRT-LLM（每天 4 小时）⭐⭐⭐

### Day 1-2 — TensorRT 基础（8h）

**学习资源：**
- 文档：https://docs.nvidia.com/deeplearning/tensorrt/
- GitHub：https://github.com/NVIDIA/TensorRT

**学习内容：**
- TensorRT 优化流水线：Parse → Optimize → Build Engine → Runtime
- 关键优化：Layer Fusion、Precision Calibration、Kernel Auto-tuning

### Day 3-5 — TensorRT-LLM（12h）

**学习资源：**
- GitHub：https://github.com/NVIDIA/TensorRT-LLM
- 文档：https://nvidia.github.io/TensorRT-LLM/

**动手实践：**
```bash
# 安装（建议用 Docker）
docker pull nvcr.io/nvidia/tritonserver:xx.xx-trtllm-python-py3

# 构建 LLaMA 引擎
python3 convert_checkpoint.py --model_dir ./llama-7b-hf \
    --output_dir ./trt_ckpt --dtype float16

trtllm-build --checkpoint_dir ./trt_ckpt \
    --output_dir ./trt_engine \
    --gemm_plugin float16

# 运行推理
python3 run.py --engine_dir ./trt_engine \
    --tokenizer_dir ./llama-7b-hf \
    --max_output_len 100 \
    --input_text "Hello, how are you?"
```

**vLLM vs TensorRT-LLM 对比测试：**
```python
# 准备相同的测试数据
test_prompts = [
    "Explain quantum computing in simple terms",
    "Write a Python function to sort a list",
    "What is the meaning of life?",
    # ...更多
]

# 分别测试两个引擎，记录：
# 1. TTFT (Time to First Token) — 首个 token 延迟
# 2. TPS (Tokens per Second) — 生成速度
# 3. Throughput (tokens/s) — 吞吐量
# 4. Memory usage — 显存占用
# 5. 不同 batch size 下的性能变化
```

---

## 第 13 周：其他推理框架（每天 3.5 小时）

### Day 1 — llama.cpp（3.5h）

**学习资源：** https://github.com/ggerganov/llama.cpp

```bash
# 编译
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make -j

# 下载 GGUF 模型并推理
./llama-cli -m models/llama-2-7b.Q4_K_M.gguf \
    -p "Hello" -n 100

# 量化
./llama-quantize models/llama-2-7b-f16.gguf models/llama-2-7b-Q4_K_M.gguf Q4_K_M
```

### Day 2 — Triton Inference Server（3.5h）

**学习资源：** https://github.com/triton-inference-server/server

### Day 3-4 — 框架横向对比（7h）

编写对比报告，从以下维度对比：
1. 部署难度
2. 支持的模型格式
3. 量化支持
4. 性能（latency / throughput）
5. 功能完整性（streaming, function calling, multi-lora 等）

### Day 5 — OpenAI 兼容 API 测试（3.5h）

```python
# 完整的 OpenAI API 兼容性测试套件
import pytest
import requests

BASE_URL = "http://localhost:8000"

class TestOpenAICompat:
    def test_models_list(self):
        r = requests.get(f"{BASE_URL}/v1/models")
        assert r.status_code == 200
        assert "data" in r.json()

    def test_completion(self):
        r = requests.post(f"{BASE_URL}/v1/completions", json={
            "model": "test-model",
            "prompt": "Hello",
            "max_tokens": 10,
        })
        assert r.status_code == 200
        assert "choices" in r.json()

    def test_chat_completion(self):
        r = requests.post(f"{BASE_URL}/v1/chat/completions", json={
            "model": "test-model",
            "messages": [{"role": "user", "content": "Hi"}],
            "max_tokens": 10,
        })
        assert r.status_code == 200

    def test_streaming(self):
        r = requests.post(f"{BASE_URL}/v1/chat/completions", json={
            "model": "test-model",
            "messages": [{"role": "user", "content": "Count to 5"}],
            "stream": True,
        }, stream=True)
        chunks = []
        for line in r.iter_lines():
            if line and line != b"data: [DONE]":
                chunks.append(line)
        assert len(chunks) > 0

    def test_invalid_model(self):
        r = requests.post(f"{BASE_URL}/v1/completions", json={
            "model": "nonexistent",
            "prompt": "Hello",
        })
        assert r.status_code in [400, 404]

    @pytest.mark.parametrize("temperature", [0.0, 0.5, 1.0, 2.0])
    def test_temperature(self, temperature):
        r = requests.post(f"{BASE_URL}/v1/completions", json={
            "model": "test-model",
            "prompt": "Hello",
            "max_tokens": 20,
            "temperature": temperature,
        })
        assert r.status_code == 200
```

---

# 第五阶段：软件测试与 QA（第 14-16 周）

## 第 14 周：AI 系统测试策略（每天 3.5 小时）

### Day 1-2 — 测试金字塔与白盒测试（7h）

**学习资源：**
- 书籍：《Software Testing》（Srinivasan Desikan）
- pytest-cov：https://pytest-cov.readthedocs.io/
- gcov/lcov（C/C++覆盖率）：https://gcc.gnu.org/onlinedocs/gcc/Gcov.html

**动手实践：**
```bash
# Python 覆盖率
pytest --cov=mypackage --cov-report=html tests/

# C/C++ 覆盖率
gcc -fprofile-arcs -ftest-coverage mycode.c -o mycode
./mycode
gcov mycode.c
lcov --capture --directory . --output-file coverage.info
genhtml coverage.info --output-directory html_report
```

### Day 3 — 性能测试（3.5h）

**关键指标：**
```python
# LLM 推理性能指标定义
class LLMMetrics:
    """LLM 推理关键性能指标"""

    def __init__(self):
        self.metrics = {}

    def ttft(self):
        """Time to First Token: 从请求发送到收到第一个 token 的时间"""
        pass

    def tpot(self):
        """Time Per Output Token: 每个输出 token 的平均生成时间"""
        pass

    def e2e_latency(self):
        """End-to-End Latency: 从请求到完整响应的总时间"""
        # = TTFT + (output_tokens - 1) * TPOT
        pass

    def throughput(self):
        """Throughput: 单位时间内生成的 token 总数（所有请求）"""
        # tokens/second
        pass

    def rps(self):
        """Requests Per Second: 每秒处理的请求数"""
        pass
```

### Day 4-5 — 精度测试与兼容性测试（7h）

**动手实践：**
```python
# 量化模型精度验证
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import numpy as np

def compare_model_outputs(model_a, model_b, tokenizer, test_prompts):
    """对比两个模型的输出差异"""
    results = []
    for prompt in test_prompts:
        input_ids = tokenizer.encode(prompt, return_tensors="pt")

        with torch.no_grad():
            logits_a = model_a(input_ids).logits
            logits_b = model_b(input_ids).logits

        # 计算 logits 差异
        mse = torch.mean((logits_a - logits_b) ** 2).item()
        cos_sim = torch.nn.functional.cosine_similarity(
            logits_a.flatten(), logits_b.flatten(), dim=0
        ).item()

        # 比较 top-1 token 是否一致
        top1_a = logits_a[:, -1, :].argmax(dim=-1)
        top1_b = logits_b[:, -1, :].argmax(dim=-1)
        top1_match = (top1_a == top1_b).item()

        results.append({
            "prompt": prompt[:50],
            "mse": mse,
            "cos_sim": cos_sim,
            "top1_match": top1_match,
        })

    return results

# Perplexity 测试
def compute_perplexity(model, tokenizer, text):
    """计算困惑度——越低越好"""
    input_ids = tokenizer.encode(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    return torch.exp(outputs.loss).item()
```

---

## 第 15 周：CI/CD 与自动化（每天 3.5 小时）

### Day 1-2 — CI/CD 流水线（7h）

**动手实践：** 编写 GitHub Actions workflow
```yaml
# .github/workflows/llm-test.yml
name: LLM Test Suite
on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: pytest tests/unit/ -v --cov

  api-tests:
    runs-on: [self-hosted, gpu]
    steps:
      - uses: actions/checkout@v4
      - run: |
          python -m vllm.entrypoints.openai.api_server \
            --model test-model --port 8000 &
          sleep 30
          pytest tests/api/ -v
          kill %1

  performance-tests:
    runs-on: [self-hosted, gpu]
    steps:
      - uses: actions/checkout@v4
      - run: python benchmark.py --output results.json
      - run: python check_regression.py results.json
```

### Day 3-4 — Docker 容器化（7h）

**动手实践：**
```dockerfile
# Dockerfile for LLM Testing
FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip git
RUN pip3 install vllm pytest requests

COPY tests/ /app/tests/
COPY benchmark.py /app/

WORKDIR /app
CMD ["pytest", "tests/", "-v"]
```

```bash
# 运行带 GPU 的容器
docker run --gpus all -it my-llm-test-image
```

### Day 5 — 模型精度 Benchmark（3.5h）

**学习内容：**
- 常见评测集：MMLU、HumanEval、GSM8K、HellaSwag
- lm-evaluation-harness：https://github.com/EleutherAI/lm-evaluation-harness

```bash
# 使用 lm-evaluation-harness
pip install lm-eval
lm_eval --model hf \
    --model_args pretrained=facebook/opt-1.3b \
    --tasks hellaswag,mmlu \
    --batch_size 16
```

---

## 第 16 周：Profiling 与问题排查（每天 3.5 小时）

### Day 1-2 — Python & GPU Profiling（7h）

```python
# Python Profiling
import cProfile
import pstats

# 方式 1: cProfile
cProfile.run('my_function()', 'profile_output')
stats = pstats.Stats('profile_output')
stats.sort_stats('cumulative')
stats.print_stats(20)

# 方式 2: line_profiler (逐行分析)
# pip install line_profiler
# @profile  装饰在函数上
# kernprof -l -v my_script.py

# 方式 3: py-spy (低开销采样)
# pip install py-spy
# py-spy top --pid <PID>
# py-spy record -o profile.svg --pid <PID>  # 生成火焰图
```

```bash
# GPU Profiling
nsys profile -o inference_profile python3 run_inference.py
# 在 Nsight Systems GUI 中分析 timeline
```

### Day 3-4 — 常见问题排查（7h）

```python
# OOM (Out of Memory) 排查
import torch

# 查看显存使用
print(torch.cuda.memory_summary())

# 追踪显存分配
torch.cuda.memory._record_memory_history()
# ... 运行代码 ...
snapshot = torch.cuda.memory._snapshot()
# 分析哪里分配了最多显存

# KV Cache 显存计算
def estimate_kv_cache_memory(
    n_layers, n_kv_heads, d_head, seq_len, batch_size, dtype_bytes=2
):
    """精确计算 KV Cache 显存"""
    kv_cache_bytes = 2 * n_layers * n_kv_heads * d_head * seq_len * batch_size * dtype_bytes
    return kv_cache_bytes / (1024 ** 3)  # GB

# LLaMA-7B 的 KV Cache
mem = estimate_kv_cache_memory(
    n_layers=32, n_kv_heads=32, d_head=128,
    seq_len=4096, batch_size=16
)
print(f"LLaMA-7B KV Cache (batch=16, seq=4096): {mem:.2f} GB")
```

### Day 5 — 测试报告编写（3.5h）

**报告模板：**
```markdown
# LLM 推理引擎测试报告

## 1. 测试环境
- GPU: NVIDIA A100 80GB
- Driver: 535.xx
- CUDA: 12.1
- 模型: LLaMA-2-7B
- 框架: vLLM v0.x.x

## 2. 功能测试结果
| 测试项 | 状态 | 备注 |
|--------|------|------|
| 文本生成 | PASS | |
| 流式输出 | PASS | |
| 多轮对话 | PASS | |
| 量化推理 (AWQ) | PASS | |
| 量化推理 (GPTQ) | FAIL | Issue #xxx |

## 3. 性能测试结果
| 指标 | 值 |
|------|-----|
| TTFT (P50) | 45ms |
| TTFT (P99) | 120ms |
| TPS (单请求) | 35 tokens/s |
| Throughput (batch=32) | 800 tokens/s |

## 4. 精度测试
| 量化方式 | Perplexity | 相对基线变化 |
|----------|-----------|------------|
| FP16 (基线) | 5.68 | - |
| AWQ-INT4 | 5.82 | +2.5% |
| GPTQ-INT4 | 5.75 | +1.2% |

## 5. 问题列表
...
```

---

# 第六阶段：综合实战（第 17-18 周）

## 第 17-18 周：端到端项目（每天 4 小时）

**最终项目：构建一个完整的 LLM 推理测试框架**

```
llm-test-framework/
├── README.md
├── requirements.txt
├── config/
│   ├── models.yaml          # 测试模型配置
│   └── test_config.yaml     # 测试参数配置
├── tests/
│   ├── functional/
│   │   ├── test_completion.py
│   │   ├── test_chat.py
│   │   ├── test_streaming.py
│   │   └── test_edge_cases.py
│   ├── performance/
│   │   ├── test_latency.py
│   │   ├── test_throughput.py
│   │   └── test_scalability.py
│   ├── accuracy/
│   │   ├── test_perplexity.py
│   │   └── test_benchmarks.py
│   └── compatibility/
│       ├── test_quantization.py
│       └── test_multi_gpu.py
├── utils/
│   ├── metrics.py           # 性能指标收集
│   ├── report.py            # 报告生成
│   └── profiler.py          # Profiling 工具
├── Dockerfile
└── .github/workflows/ci.yml
```

---

# 附录：推荐资源汇总

## 必看视频课程
| 课程 | 平台 | 用途 |
|------|------|------|
| 吴恩达 Machine Learning Specialization | Coursera | ML 基础 |
| 李宏毅机器学习 2023 | YouTube | ML/DL 中文 |
| 3Blue1Brown Neural Networks | YouTube | 直觉理解 |
| Andrej Karpathy "Let's build GPT" | YouTube | Transformer 从零实现 |
| MIT EfficientML (Han Song) | YouTube | 模型优化 |
| Stanford CS231n | YouTube | 深度学习视觉 |

## 必读论文/博客
| 资源 | 主题 |
|------|------|
| "Attention Is All You Need" | Transformer 原始论文 |
| Jay Alammar Illustrated Transformer | Transformer 可视化解释 |
| vLLM 论文 (PagedAttention) | PagedAttention |
| FlashAttention v1/v2 论文 | Attention 优化 |
| AWQ 论文 | 量化 |
| GPTQ 论文 | 量化 |
| Chris Olah 博客 | 神经网络直觉 |
| Lilian Weng 博客 | LLM 综述 |
| kipp.ly 推理算术 | 推理性能分析 |

## 工具链
| 工具 | 用途 |
|------|------|
| PyTorch | 深度学习框架 |
| HuggingFace Transformers | 模型加载/推理 |
| vLLM | 高性能推理引擎 |
| TensorRT-LLM | NVIDIA 推理引擎 |
| llama.cpp | CPU/轻量推理 |
| pytest | Python 测试框架 |
| Nsight Systems/Compute | GPU Profiling |
| Docker + NVIDIA Container Toolkit | 容器化 |
| lm-evaluation-harness | 模型评测 |

## 推荐书籍
| 书籍 | 用途 |
|------|------|
| 《Deep Learning》(Goodfellow) | DL 理论基础 |
| 《CUDA by Example》 | CUDA 入门 |
| 《Programming Massively Parallel Processors》 | GPU 编程进阶 |
| 《Python Testing with pytest》 | 测试框架 |
| 《The Linux Command Line》 | Linux 基础 |

---

> **最后提醒：** 这份计划的核心是 **第 4-7 周**（Transformer + 推理优化）和 **第 11-12 周**（推理引擎实战），这是岗位面试和日常工作中最核心的部分。如果时间有限，优先保证这些部分的学习深度。
