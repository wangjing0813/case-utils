# AI/Deep Learning QA Engineer 16周完整学习指南

> **目标岗位**: AI/Deep Learning Software QA Engineer
> **当前背景**: 1年Java测试开发经验、2年Python经验、4年Linux经验
> **学习周期**: 16周（约4个月） | **总学时**: ~370小时

---

# 第一阶段: Python进阶 + C/C++基础（Week 1-3）

---

## Week 1: Python进阶

---

### Day 1: Python高级数据结构与性能优化

#### 1.1 collections模块详解

`collections`模块提供了Python内置容器(`dict`, `list`, `set`, `tuple`)的高性能替代方案。

**defaultdict —— 带默认值的字典**

普通`dict`在访问不存在的key时会抛出`KeyError`，而`defaultdict`会自动创建默认值：

```python
from collections import defaultdict

# ---- 普通dict vs defaultdict ----
# 普通dict: 统计词频需要先判断key是否存在
word_count_normal = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    if word in word_count_normal:
        word_count_normal[word] += 1
    else:
        word_count_normal[word] = 1

# defaultdict: 直接操作，不存在时自动创建默认值
word_count = defaultdict(int)  # int()默认值为0
for word in words:
    word_count[word] += 1

print(dict(word_count))  # {'apple': 3, 'banana': 2, 'cherry': 1}

# ---- 更复杂的例子：分组 ----
students = [
    ("ClassA", "Alice"), ("ClassB", "Bob"),
    ("ClassA", "Charlie"), ("ClassB", "David"),
]
groups = defaultdict(list)  # list()默认值为[]
for cls, name in students:
    groups[cls].append(name)

print(dict(groups))  # {'ClassA': ['Alice', 'Charlie'], 'ClassB': ['Bob', 'David']}

# ---- 嵌套defaultdict ----
# 自动创建多层嵌套结构
tree = lambda: defaultdict(tree)
taxonomy = tree()
taxonomy["Animal"]["Mammal"]["Dog"] = "Canis lupus"
taxonomy["Animal"]["Bird"]["Eagle"] = "Aquila chrysaetos"
```

**Counter —— 计数器**

```python
from collections import Counter

# 基本用法
text = "hello world hello python hello world"
counter = Counter(text.split())
print(counter)  # Counter({'hello': 3, 'world': 2, 'python': 1})

# most_common(n): 获取出现频率最高的n个元素
print(counter.most_common(2))  # [('hello', 3), ('world', 2)]

# 数学运算
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Counter({'a': 2})  -- 只保留正数

# 实用技巧：找两个列表的交集和差集（按频率）
list1 = [1, 1, 2, 3, 3, 3]
list2 = [1, 1, 1, 2, 2]
c1, c2 = Counter(list1), Counter(list2)
print(list((c1 & c2).elements()))  # [1, 1, 2] -- 交集（取最小频率）
print(list((c1 | c2).elements()))  # [1, 1, 1, 2, 2, 3, 3, 3] -- 并集（取最大频率）
```

**deque —— 双端队列**

```python
from collections import deque

# deque vs list 性能对比
# list: 头部插入/删除 O(n)，尾部插入/删除 O(1)
# deque: 头部和尾部插入/删除都是 O(1)

dq = deque([1, 2, 3])
dq.appendleft(0)   # 头部添加 O(1)
dq.append(4)        # 尾部添加 O(1)
dq.popleft()         # 头部弹出 O(1)
dq.pop()             # 尾部弹出 O(1)

# maxlen: 固定长度的滑动窗口
# 超过maxlen时，自动从另一端弹出
recent_logs = deque(maxlen=5)
for i in range(10):
    recent_logs.append(f"log_{i}")
print(list(recent_logs))  # ['log_5', 'log_6', 'log_7', 'log_8', 'log_9']

# rotate: 循环旋转
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)   # 右旋2步
print(list(dq))  # [4, 5, 1, 2, 3]
dq.rotate(-2)  # 左旋2步
print(list(dq))  # [1, 2, 3, 4, 5]
```

**namedtuple —— 命名元组**

```python
from collections import namedtuple

# 创建一个不可变的、有名称字段的元组
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)      # 1 2 (用名称访问)
print(p[0], p[1])     # 1 2 (用索引访问)

# 比普通tuple更具可读性
# 普通tuple: result = (200, "OK", {"data": [1,2,3]})
# 命名tuple:
Response = namedtuple('Response', ['status', 'message', 'data'])
result = Response(200, "OK", {"data": [1, 2, 3]})
print(result.status)   # 200
print(result.message)  # "OK"

# _asdict(): 转换为OrderedDict
print(result._asdict())  # {'status': 200, 'message': 'OK', 'data': {...}}

# _replace(): 创建修改后的新实例（原实例不变，因为不可变）
new_result = result._replace(status=404, message="Not Found")
```

**collections模块选择指南**:

| 数据结构 | 适用场景 | 相比内置类型的优势 |
|---------|---------|-----------------|
| `defaultdict` | 需要默认值的字典（统计、分组） | 避免KeyError，代码更简洁 |
| `Counter` | 计数、频率统计、Top-K | 内置计数方法，支持数学运算 |
| `deque` | 队列、栈、滑动窗口 | 两端O(1)操作，list头部操作是O(n) |
| `namedtuple` | 简单不可变数据类、替代小dict | 内存更小，不可变，支持索引和名称 |

#### 1.2 生成器(Generator)与迭代器(Iterator)深入理解

**迭代器协议**

Python中任何实现了`__iter__()`和`__next__()`方法的对象都是迭代器：

```python
class CountDown:
    """自定义迭代器：倒计时"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # 迭代器返回自身

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 迭代结束的信号
        self.current -= 1
        return self.current + 1

for num in CountDown(5):
    print(num, end=" ")  # 5 4 3 2 1
```

**生成器函数 —— 惰性求值(Lazy Evaluation)**

生成器是一种特殊的迭代器，使用`yield`关键字定义。核心特点是**惰性求值** —— 值只在被请求时才计算，而不是一次性全部计算。

```python
# ---- yield vs return ----
# return: 函数执行完毕，返回值，函数状态销毁
# yield:  函数暂停，返回值，函数状态保留，下次调用从暂停处继续

def fibonacci_generator(n):
    """斐波那契数列生成器 —— 惰性生成"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a          # 暂停并返回当前值
        a, b = b, a + b  # 下次调用时从这里继续
        count += 1

# 使用生成器
gen = fibonacci_generator(10)
print(next(gen))  # 0 -- 计算第一个值
print(next(gen))  # 1 -- 从上次暂停处继续
print(next(gen))  # 1

# for循环自动调用next()直到StopIteration
for num in fibonacci_generator(10):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34


# ---- 生成器的状态保持 ----
def stateful_counter():
    """演示生成器如何保持内部状态"""
    count = 0
    while True:
        received = yield count  # yield可以接收send()发送的值
        if received is not None:
            count = received
        else:
            count += 1

counter = stateful_counter()
next(counter)            # 启动生成器，必须先调用一次next
print(counter.send(10))  # 发送值10，输出: 10
print(next(counter))     # 输出: 11
print(next(counter))     # 输出: 12
```

**列表推导式 vs 生成器表达式的内存差异**

```python
import sys

# 列表推导式：一次性创建所有元素，存储在内存中
list_comp = [x * x for x in range(1_000_000)]

# 生成器表达式：惰性计算，只存储生成逻辑
gen_expr = (x * x for x in range(1_000_000))

print(f"列表内存占用: {sys.getsizeof(list_comp):>12,} bytes")  # ~8,448,728 bytes
print(f"生成器内存占用: {sys.getsizeof(gen_expr):>10,} bytes")  # ~200 bytes (固定大小)

# 更详细的内存对比
def memory_comparison():
    """对比处理100万条数据的内存差异"""
    import tracemalloc

    # 方法1: 列表（急切求值）
    tracemalloc.start()
    data_list = [i ** 2 for i in range(1_000_000)]
    total_list = sum(data_list)
    _, peak_list = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 方法2: 生成器（惰性求值）
    tracemalloc.start()
    data_gen = (i ** 2 for i in range(1_000_000))
    total_gen = sum(data_gen)
    _, peak_gen = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"列表方式 - 峰值内存: {peak_list / 1024 / 1024:.2f} MB, 结果: {total_list}")
    print(f"生成器方式 - 峰值内存: {peak_gen / 1024 / 1024:.2f} MB, 结果: {total_gen}")
    # 列表方式 - 峰值内存: ~38.15 MB
    # 生成器方式 - 峰值内存: ~0.00 MB

memory_comparison()
```

**练习1: 大文件逐行读取并统计词频**

```python
from collections import Counter
from typing import Iterator

def read_lines(filepath: str) -> Iterator[str]:
    """生成器：逐行读取大文件，不将整个文件加载到内存"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:  # 文件对象本身就是迭代器，逐行读取
            yield line.strip()

def tokenize(lines: Iterator[str]) -> Iterator[str]:
    """生成器：将行拆分为单词（管道式处理）"""
    for line in lines:
        for word in line.lower().split():
            # 去除标点符号
            word = word.strip('.,!?;:()[]{}"\'-')
            if word:
                yield word

def word_frequency(filepath: str, top_n: int = 10) -> list:
    """统计大文件的词频（使用生成器管道，内存友好）"""
    lines = read_lines(filepath)      # 生成器1: 逐行读取
    words = tokenize(lines)           # 生成器2: 逐词提取
    counter = Counter(words)          # Counter内部逐个消费生成器
    return counter.most_common(top_n)

# 使用示例 (假设有一个大文本文件)
# result = word_frequency("large_text_file.txt", top_n=20)
# for word, count in result:
#     print(f"{word}: {count}")

# ---- 创建测试文件并运行 ----
def demo():
    import tempfile
    import os

    # 创建测试文件（模拟大文件）
    content = "hello world\nhello python\npython is great\nhello world again\n" * 10000
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(content)
        filepath = f.name

    result = word_frequency(filepath, top_n=5)
    print("Top 5词频:")
    for word, count in result:
        print(f"  {word}: {count}")

    os.unlink(filepath)

demo()
```

**练习2: list vs generator内存占用对比**

```python
import sys
import time

def compare_list_vs_generator(n: int = 1_000_000):
    """对比list和generator处理n条数据的内存和时间"""

    # ---- 列表方式 ----
    start = time.perf_counter()
    data_list = [x ** 2 for x in range(n)]
    list_result = sum(data_list)
    list_time = time.perf_counter() - start
    list_size = sys.getsizeof(data_list)

    # ---- 生成器方式 ----
    start = time.perf_counter()
    data_gen = (x ** 2 for x in range(n))
    gen_result = sum(data_gen)
    gen_time = time.perf_counter() - start
    gen_size = sys.getsizeof(data_gen)

    print(f"数据量: {n:,} 条")
    print(f"{'':10} {'内存占用':>15} {'耗时':>12} {'结果':>20}")
    print(f"{'列表':10} {list_size:>12,} B {list_time:>10.4f}s {list_result:>20}")
    print(f"{'生成器':10} {gen_size:>12,} B {gen_time:>10.4f}s {gen_result:>20}")
    print(f"内存节省: {list_size / gen_size:.0f}x")

compare_list_vs_generator(1_000_000)
compare_list_vs_generator(10_000_000)
```

**重点掌握: 生成器惰性求值 vs 列表急切求值**

| 特性 | 列表(List) | 生成器(Generator) |
|------|-----------|-----------------|
| 求值方式 | 急切(Eager): 一次性计算所有元素 | 惰性(Lazy): 按需计算 |
| 内存占用 | O(n) — 与数据量成正比 | O(1) — 固定大小 |
| 可重复迭代 | 是 | 否（耗尽后需重新创建） |
| 支持索引 | 是 (`list[i]`) | 否 |
| 支持len() | 是 | 否 |
| 适用场景 | 数据量小，需要多次访问 | 数据量大，只需遍历一次 |

---

### Day 2: Python装饰器与上下文管理器

#### 2.1 装饰器原理（闭包 -> 装饰器 -> 带参装饰器）

**闭包(Closure) —— 装饰器的基础**

闭包是指一个内部函数引用了外部函数的变量，当外部函数执行完毕后，内部函数仍然可以访问这些变量：

```python
def outer(x):
    """外部函数"""
    def inner(y):
        """内部函数（闭包）: 捕获了外部变量x"""
        return x + y  # x是自由变量，来自外部作用域
    return inner

add_5 = outer(5)      # x=5 被闭包捕获
print(add_5(3))       # 8
print(add_5(10))      # 15
print(add_5.__closure__[0].cell_contents)  # 5 (查看捕获的变量)
```

**装饰器 —— 本质是接受函数并返回函数的高阶函数**

```python
import functools
import time

# ---- 基本装饰器 ----
def simple_decorator(func):
    """最简单的装饰器"""
    @functools.wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数返回: {result}")
        return result
    return wrapper

@simple_decorator  # 语法糖，等价于: greet = simple_decorator(greet)
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

print(greet("World"))
print(greet.__name__)  # "greet" (如果不用@wraps，会显示"wrapper")
print(greet.__doc__)   # "问候函数" (如果不用@wraps，会显示wrapper的文档)
```

**functools.wraps的作用**:
- 保留原函数的`__name__`（函数名）
- 保留原函数的`__doc__`（文档字符串）
- 保留原函数的`__module__`（模块名）
- 保留原函数的`__qualname__`（限定名）
- 保留原函数的`__annotations__`（类型注解）

**练习: @timer装饰器**

```python
import functools
import time

def timer(func):
    """记录函数执行时间的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__}() 执行时间: {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_function(n):
    """模拟耗时操作"""
    total = sum(i * i for i in range(n))
    return total

result = slow_function(1_000_000)
# [TIMER] slow_function() 执行时间: 0.082345s
```

**练习: @retry(max_retries=3) 带参数的装饰器**

```python
import functools
import time
import random

def retry(max_retries=3, delay=1.0, exceptions=(Exception,)):
    """
    带参数的重试装饰器
    三层嵌套结构:
      retry(参数) -> decorator(func) -> wrapper(*args, **kwargs)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"[RETRY] {func.__name__}() 第{attempt}次失败: {e}")
                    if attempt < max_retries:
                        print(f"  等待 {delay}s 后重试...")
                        time.sleep(delay)
            raise last_exception  # 所有重试都失败，抛出最后一个异常
        return wrapper
    return decorator

# 使用带参数的装饰器
@retry(max_retries=3, delay=0.5, exceptions=(ConnectionError, TimeoutError))
def unreliable_api_call():
    """模拟不稳定的API调用"""
    if random.random() < 0.7:  # 70%概率失败
        raise ConnectionError("网络连接失败")
    return {"status": "success", "data": [1, 2, 3]}

try:
    result = unreliable_api_call()
    print(f"成功: {result}")
except ConnectionError as e:
    print(f"所有重试失败: {e}")
```

**类装饰器**

```python
class CacheResult:
    """类装饰器: 缓存函数结果（简易版memoize）"""
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

    def clear_cache(self):
        self.cache.clear()

@CacheResult
def expensive_computation(n):
    """模拟耗时计算"""
    time.sleep(0.1)
    return n ** 2 + n

print(expensive_computation(5))   # 30 (计算并缓存)
print(expensive_computation(5))   # 30 (从缓存读取，无延迟)
print(expensive_computation(10))  # 110 (计算并缓存)
expensive_computation.clear_cache()  # 清除缓存
```

#### 2.2 上下文管理器

```python
from contextlib import contextmanager
import sqlite3
import time

# ---- 方式1: 类实现 (__enter__ / __exit__) ----
class DatabaseConnection:
    """数据库连接管理器（类方式）"""
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        """进入with块时调用: 建立连接"""
        self.conn = sqlite3.connect(self.db_path)
        print(f"数据库连接已建立: {self.db_path}")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出with块时调用: 关闭连接"""
        if self.conn:
            if exc_type is None:
                self.conn.commit()   # 无异常则提交
                print("事务已提交")
            else:
                self.conn.rollback()  # 有异常则回滚
                print(f"事务已回滚 (异常: {exc_type.__name__}: {exc_val})")
            self.conn.close()
            print("数据库连接已关闭")
        return False  # False: 不抑制异常; True: 抑制异常

# 使用
with DatabaseConnection(":memory:") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO test VALUES (1, 'Alice')")


# ---- 方式2: @contextmanager 装饰器（更简洁） ----
@contextmanager
def timer_context(label="操作"):
    """计时上下文管理器"""
    start = time.perf_counter()
    print(f"[{label}] 开始...")
    try:
        yield  # yield之前 = __enter__, yield之后 = __exit__
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] 完成, 耗时: {elapsed:.4f}s")

with timer_context("数据处理"):
    data = [x ** 2 for x in range(1_000_000)]
    total = sum(data)


@contextmanager
def temp_directory():
    """临时目录上下文管理器"""
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()
    try:
        yield tmpdir  # 提供临时目录路径
    finally:
        shutil.rmtree(tmpdir)  # 清理临时目录
        print(f"临时目录已清理: {tmpdir}")

with temp_directory() as tmpdir:
    print(f"使用临时目录: {tmpdir}")
    # 在这里进行文件操作...
```

---

### Day 3: Python并发编程

#### 3.1 GIL（全局解释器锁）详解

**GIL是什么**: CPython解释器中的一个互斥锁(mutex)，确保同一时刻只有一个线程执行Python字节码。

**为什么需要GIL**: CPython的内存管理（引用计数）不是线程安全的。如果没有GIL，多线程同时修改引用计数可能导致内存泄漏或提前释放。

**GIL的影响**:

| 场景 | 多线程表现 | 原因 | 推荐方案 |
|------|----------|------|---------|
| CPU密集型 | 无法加速，甚至更慢 | GIL阻止多线程并行执行 | multiprocessing |
| IO密集型 | 可以加速 | 线程等待IO时释放GIL | threading/asyncio |
| C扩展代码 | 可以加速 | C代码可以主动释放GIL | threading |

```python
import threading
import multiprocessing
import time

def cpu_intensive(n):
    """CPU密集型任务: 计算大量素数"""
    count = 0
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

N = 100_000

# ---- 单线程 ----
start = time.perf_counter()
cpu_intensive(N)
cpu_intensive(N)
print(f"单线程: {time.perf_counter() - start:.2f}s")

# ---- 多线程(受GIL限制, 无法加速CPU密集型) ----
start = time.perf_counter()
t1 = threading.Thread(target=cpu_intensive, args=(N,))
t2 = threading.Thread(target=cpu_intensive, args=(N,))
t1.start(); t2.start()
t1.join(); t2.join()
print(f"多线程: {time.perf_counter() - start:.2f}s")  # 几乎等于单线程

# ---- 多进程(绕过GIL, 真正并行) ----
start = time.perf_counter()
p1 = multiprocessing.Process(target=cpu_intensive, args=(N,))
p2 = multiprocessing.Process(target=cpu_intensive, args=(N,))
p1.start(); p2.start()
p1.join(); p2.join()
print(f"多进程: {time.perf_counter() - start:.2f}s")  # 约为单线程的一半
```

#### 3.2 concurrent.futures模块

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import urllib.request
import time

# ---- ThreadPoolExecutor: 适合IO密集型 ----
URLS = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
]

def fetch_url(url):
    """下载网页（IO密集型）"""
    with urllib.request.urlopen(url, timeout=10) as response:
        return len(response.read())

# 串行下载
start = time.perf_counter()
results_serial = [fetch_url(url) for url in URLS]
print(f"串行下载: {time.perf_counter() - start:.2f}s")

# 并发下载
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as executor:
    results_concurrent = list(executor.map(fetch_url, URLS))
print(f"并发下载: {time.perf_counter() - start:.2f}s")


# ---- ProcessPoolExecutor: 适合CPU密集型 ----
def compute_sum_of_squares(n):
    return sum(i * i for i in range(n))

numbers = [10_000_000] * 4

start = time.perf_counter()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(compute_sum_of_squares, numbers))
print(f"多进程计算: {time.perf_counter() - start:.2f}s")

# submit + as_completed: 获取先完成的结果
from concurrent.futures import as_completed

with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_url = {executor.submit(fetch_url, url): url for url in URLS}
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            size = future.result()
            print(f"{url}: {size} bytes")
        except Exception as e:
            print(f"{url} 失败: {e}")
```

#### 3.3 asyncio异步编程

```python
import asyncio
import aiohttp  # pip install aiohttp
import time

async def fetch_url_async(session, url):
    """异步下载网页"""
    async with session.get(url) as response:
        data = await response.read()
        return len(data)

async def main():
    urls = [f'https://httpbin.org/delay/1' for _ in range(5)]

    async with aiohttp.ClientSession() as session:
        # 并发发送所有请求
        tasks = [fetch_url_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for url, size in zip(urls, results):
        print(f"{url}: {size} bytes")

start = time.perf_counter()
asyncio.run(main())
print(f"异步下载: {time.perf_counter() - start:.2f}s")
# 5个1秒的请求并发执行，总耗时约1秒
```

**并发方案选择总结**:

| 方案 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| `threading` | IO密集型(网络/文件) | 共享内存，切换开销小 | 受GIL限制，无法并行CPU计算 |
| `multiprocessing` | CPU密集型 | 真正并行，绕过GIL | 内存不共享，进程开销大 |
| `asyncio` | 高并发IO(上千连接) | 单线程高并发，开销极小 | 需要async/await，生态依赖 |
| `ThreadPoolExecutor` | IO密集+简单API | API简洁，易于使用 | 线程数有限 |
| `ProcessPoolExecutor` | CPU密集+简单API | API简洁，真正并行 | 数据序列化开销 |

---

### Day 4: Python类型注解与单元测试

#### 4.1 类型注解(Type Hints)

```python
from typing import (
    Optional, Union, List, Dict, Tuple,
    TypeVar, Generic, Callable, Iterator
)

# ---- 基本类型注解 ----
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Optional[X] = Union[X, None]
def find_user(user_id: int) -> Optional[dict]:
    """返回用户信息，找不到返回None"""
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)

# Union: 多种类型
def process_input(data: Union[str, list, dict]) -> str:
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return ", ".join(str(x) for x in data)
    return str(data)

# 复杂类型
def parse_config(filepath: str) -> Dict[str, List[Tuple[str, int]]]:
    """返回: {"section": [("key", value), ...]}"""
    return {"database": [("host", 3306), ("port", 5432)]}

# TypeVar: 泛型
T = TypeVar('T')

def first_element(items: List[T]) -> Optional[T]:
    """返回列表第一个元素（类型安全）"""
    return items[0] if items else None

# Callable: 函数类型
def apply_func(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

result = apply_func(lambda x, y: x + y, 3, 4)  # 7
```

#### 4.2 pytest测试框架

**练习: 计算器类及完整测试**

```python
# ---- calculator.py ----
class Calculator:
    """简单计算器"""
    def __init__(self, precision: int = 2):
        self.precision = precision
        self.history: list = []

    def add(self, a: float, b: float) -> float:
        result = round(a + b, self.precision)
        self.history.append(('add', a, b, result))
        return result

    def subtract(self, a: float, b: float) -> float:
        result = round(a - b, self.precision)
        self.history.append(('subtract', a, b, result))
        return result

    def multiply(self, a: float, b: float) -> float:
        result = round(a * b, self.precision)
        self.history.append(('multiply', a, b, result))
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        result = round(a / b, self.precision)
        self.history.append(('divide', a, b, result))
        return result

    def get_history(self) -> list:
        return self.history.copy()

    def clear_history(self) -> None:
        self.history.clear()
```

```python
# ---- test_calculator.py ----
import pytest
from calculator import Calculator

# ---- Fixture ----
@pytest.fixture
def calc():
    """每个测试函数前创建新的Calculator实例"""
    return Calculator(precision=2)

@pytest.fixture(scope="module")
def shared_calc():
    """模块级fixture: 整个模块共享一个实例"""
    return Calculator(precision=4)

# ---- 基本测试 ----
class TestCalculatorBasic:
    def test_add(self, calc):
        assert calc.add(2, 3) == 5

    def test_subtract(self, calc):
        assert calc.subtract(10, 3) == 7

    def test_multiply(self, calc):
        assert calc.multiply(4, 5) == 20

    def test_divide(self, calc):
        assert calc.divide(10, 3) == 3.33

    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError, match="除数不能为零"):
            calc.divide(10, 0)

# ---- 参数化测试 ----
class TestCalculatorParametrized:
    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (-1, -1, -2),
        (0.1, 0.2, 0.3),
        (1000000, 1000000, 2000000),
        (1.005, 2.005, 3.01),  # 测试精度
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5.0),
        (1, 3, 0.33),
        (-6, 2, -3.0),
        (0, 5, 0.0),
    ])
    def test_divide_parametrized(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected

# ---- 历史记录测试 ----
class TestCalculatorHistory:
    def test_history_recording(self, calc):
        calc.add(1, 2)
        calc.multiply(3, 4)
        history = calc.get_history()
        assert len(history) == 2
        assert history[0] == ('add', 1, 2, 3)
        assert history[1] == ('multiply', 3, 4, 12)

    def test_clear_history(self, calc):
        calc.add(1, 2)
        calc.clear_history()
        assert calc.get_history() == []

    def test_history_is_copy(self, calc):
        """确保返回的是副本，外部修改不影响内部"""
        calc.add(1, 2)
        history = calc.get_history()
        history.clear()
        assert len(calc.get_history()) == 1  # 内部未受影响

# ---- 边界测试 ----
class TestCalculatorEdgeCases:
    def test_large_numbers(self, calc):
        result = calc.add(1e15, 1e15)
        assert result == 2e15

    def test_very_small_numbers(self, calc):
        result = calc.add(1e-10, 2e-10)
        assert result == 0.0  # 因为precision=2

    @pytest.mark.parametrize("a, b", [
        (float('inf'), 1),
        (1, float('inf')),
    ])
    def test_infinity(self, calc, a, b):
        result = calc.add(a, b)
        assert result == float('inf')
```

**Mock测试: 模拟外部API**

```python
# ---- api_client.py ----
import requests

class WeatherClient:
    def __init__(self, api_key: str, base_url: str = "https://api.weather.com"):
        self.api_key = api_key
        self.base_url = base_url

    def get_temperature(self, city: str) -> float:
        """获取城市温度（调用外部API）"""
        response = requests.get(
            f"{self.base_url}/current",
            params={"city": city, "key": self.api_key}
        )
        response.raise_for_status()
        return response.json()["temperature"]

    def is_hot(self, city: str, threshold: float = 30.0) -> bool:
        return self.get_temperature(city) > threshold
```

```python
# ---- test_api_client.py ----
import pytest
from unittest.mock import patch, MagicMock
from api_client import WeatherClient

@pytest.fixture
def client():
    return WeatherClient(api_key="test-key")

class TestWeatherClient:
    @patch('api_client.requests.get')
    def test_get_temperature(self, mock_get, client):
        """模拟API响应"""
        # 设置mock返回值
        mock_response = MagicMock()
        mock_response.json.return_value = {"temperature": 25.5}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # 调用被测函数
        temp = client.get_temperature("Beijing")

        # 验证
        assert temp == 25.5
        mock_get.assert_called_once_with(
            "https://api.weather.com/current",
            params={"city": "Beijing", "key": "test-key"}
        )

    @patch('api_client.requests.get')
    def test_is_hot_true(self, mock_get, client):
        mock_response = MagicMock()
        mock_response.json.return_value = {"temperature": 35.0}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        assert client.is_hot("Dubai") is True

    @patch('api_client.requests.get')
    def test_is_hot_false(self, mock_get, client):
        mock_response = MagicMock()
        mock_response.json.return_value = {"temperature": 15.0}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        assert client.is_hot("London") is False

    @patch('api_client.requests.get')
    def test_api_error(self, mock_get, client):
        """测试API错误处理"""
        mock_get.side_effect = ConnectionError("Network error")
        with pytest.raises(ConnectionError):
            client.get_temperature("Unknown")
```

**pytest fixture scope对比**:

| Scope | 创建时机 | 销毁时机 | 典型用途 |
|-------|---------|---------|---------|
| `function` | 每个测试函数前 | 每个测试函数后 | 独立测试状态（默认值） |
| `class` | 每个测试类前 | 每个测试类后 | 类内共享的setup |
| `module` | 每个.py文件前 | 每个.py文件后 | 模块级资源(DB连接) |
| `session` | 整个测试会话前 | 整个测试会话后 | 全局资源(服务启动) |

---

### Day 5: Python包管理与项目工程化

#### 5.1 项目结构与pyproject.toml

```
my_project/
├── pyproject.toml          # 项目配置（替代setup.py）
├── README.md
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── conftest.py         # 全局fixture
│   ├── test_core.py
│   └── test_utils.py
└── .github/
    └── workflows/
        └── test.yml
```

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "my-project"
version = "0.1.0"
description = "AI推理测试框架"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.28.0",
    "pytest>=7.0.0",
    "pyyaml>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest-cov>=4.0",
    "black>=23.0",
    "mypy>=1.0",
    "flake8>=6.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short --cov=src/my_project --cov-report=term-missing"

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true

[tool.black]
line-length = 100
target-version = ['py310']
```

#### 5.2 logging最佳实践

```python
# ---- logging_config.py ----
import logging
import logging.handlers
import os
from datetime import datetime

def setup_logging(
    log_dir: str = "logs",
    level: int = logging.DEBUG,
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
):
    """
    配置分级日志输出
    - DEBUG/INFO: 写入debug.log
    - WARNING及以上: 写入error.log
    - 所有级别: 输出到控制台（INFO及以上）
    """
    os.makedirs(log_dir, exist_ok=True)

    # 根日志器
    logger = logging.getLogger()
    logger.setLevel(level)

    # 日志格式
    detailed_fmt = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    simple_fmt = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%H:%M:%S'
    )

    # Handler 1: 控制台 (INFO及以上)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_fmt)

    # Handler 2: 调试日志文件 (DEBUG及以上, 自动轮转)
    debug_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, 'debug.log'),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(detailed_fmt)

    # Handler 3: 错误日志文件 (WARNING及以上)
    error_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, 'error.log'),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.WARNING)
    error_handler.setFormatter(detailed_fmt)

    logger.addHandler(console_handler)
    logger.addHandler(debug_handler)
    logger.addHandler(error_handler)

    return logger

# 使用
logger = setup_logging()
logger.debug("调试信息 - 仅在debug.log中")
logger.info("一般信息 - 控制台 + debug.log")
logger.warning("警告信息 - 控制台 + debug.log + error.log")
logger.error("错误信息 - 所有输出")
logger.critical("严重错误 - 所有输出")
```

**日志级别说明**:

| 级别 | 数值 | 用途 |
|------|------|------|
| DEBUG | 10 | 详细调试信息，开发时使用 |
| INFO | 20 | 确认程序按预期运行 |
| WARNING | 30 | 发生了不期望的事情，但程序仍正常运行 |
| ERROR | 40 | 更严重的问题，某些功能无法执行 |
| CRITICAL | 50 | 非常严重的错误，程序可能无法继续运行 |

---

### Day 6-7: NumPy与性能分析

#### 6.1 NumPy广播(Broadcasting)机制

广播是NumPy中一种隐式的数组扩展机制，允许不同形状的数组进行运算：

**广播规则**:
1. 如果两个数组维度数不同，在较小数组的形状前面补1
2. 如果两个数组在某个维度上大小不同，且其中一个为1，则将该维度扩展
3. 如果两个数组在某个维度上大小不同且都不为1，则报错

```python
import numpy as np

# ---- 标量与数组 ----
a = np.array([1, 2, 3])
print(a * 2)  # [2, 4, 6]  --  2被广播为[2, 2, 2]

# ---- 不同形状数组 ----
# (3,1) + (1,4) -> (3,4)
col = np.array([[1], [2], [3]])  # shape: (3,1)
row = np.array([10, 20, 30, 40])  # shape: (4,) -> 自动变为(1,4)

result = col + row
print(result)
# [[11, 21, 31, 41],
#  [12, 22, 32, 42],
#  [13, 23, 33, 43]]
print(f"col.shape={col.shape}, row.shape={row.shape}, result.shape={result.shape}")

# ---- 实用示例: 归一化 ----
# 矩阵每行减去该行的均值
data = np.random.randn(4, 5)
row_means = data.mean(axis=1, keepdims=True)  # shape: (4,1)
normalized = data - row_means  # (4,5) - (4,1) -> (4,5) 广播
print(f"归一化后每行均值: {normalized.mean(axis=1)}")  # 接近0
```

#### 6.2 矩阵乘法三种方式性能对比

```python
import numpy as np
import time

def matrix_multiply_python(A, B):
    """纯Python循环实现矩阵乘法"""
    n = len(A)
    m = len(B[0])
    k = len(B)
    C = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for p in range(k):
                C[i][j] += A[i][p] * B[p][j]
    return C

def matrix_multiply_numpy_basic(A, B):
    """NumPy基本实现"""
    return np.dot(A, B)

def matrix_multiply_numpy_optimized(A, B):
    """NumPy @ 运算符（等价于np.matmul，可能更快）"""
    return A @ B

def benchmark_matrix_multiplication():
    """基准测试"""
    sizes = [64, 128, 256]

    for size in sizes:
        print(f"\n--- 矩阵大小: {size}x{size} ---")

        # 准备数据
        A_list = [[float(np.random.randn()) for _ in range(size)] for _ in range(size)]
        B_list = [[float(np.random.randn()) for _ in range(size)] for _ in range(size)]
        A_np = np.array(A_list)
        B_np = np.array(B_list)

        # 方法1: 纯Python (只对小矩阵测试)
        if size <= 128:
            start = time.perf_counter()
            C1 = matrix_multiply_python(A_list, B_list)
            t_python = time.perf_counter() - start
            print(f"  纯Python循环:  {t_python:.4f}s")
        else:
            t_python = float('inf')
            print(f"  纯Python循环:  跳过(太慢)")

        # 方法2: NumPy np.dot
        start = time.perf_counter()
        for _ in range(10):  # 重复10次取平均
            C2 = np.dot(A_np, B_np)
        t_numpy = (time.perf_counter() - start) / 10
        print(f"  NumPy np.dot:  {t_numpy:.6f}s")

        # 方法3: NumPy @运算符
        start = time.perf_counter()
        for _ in range(10):
            C3 = A_np @ B_np
        t_optimized = (time.perf_counter() - start) / 10
        print(f"  NumPy A @ B:   {t_optimized:.6f}s")

        if t_python != float('inf'):
            print(f"  加速比: {t_python / t_numpy:.0f}x (Python vs NumPy)")

benchmark_matrix_multiplication()
```

#### 6.3 性能分析工具

```python
# ---- cProfile使用 ----
import cProfile
import pstats
from io import StringIO

def inefficient_function():
    """一个有性能问题的函数"""
    result = []
    for i in range(10000):
        result.append(sum(range(i)))  # sum(range(i))每次重新计算
    return result

def optimized_function():
    """优化版本"""
    result = []
    running_sum = 0
    for i in range(10000):
        running_sum += i
        result.append(running_sum)
    return result

# 使用cProfile分析
print("=== 低效版本 ===")
cProfile.run('inefficient_function()', sort='cumulative')

print("=== 优化版本 ===")
cProfile.run('optimized_function()', sort='cumulative')

# 编程方式使用cProfile (更灵活)
profiler = cProfile.Profile()
profiler.enable()
result = inefficient_function()
profiler.disable()

stream = StringIO()
stats = pstats.Stats(profiler, stream=stream).sort_stats('cumulative')
stats.print_stats(10)  # 只打印前10项
print(stream.getvalue())
```

```python
# ---- NumPy图像处理示例 ----
import numpy as np

def create_sample_image(height=100, width=100):
    """创建示例RGB图像"""
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

def rgb_to_grayscale(image):
    """RGB转灰度图 (加权平均法)"""
    # ITU-R BT.601标准: Y = 0.299*R + 0.587*G + 0.114*B
    weights = np.array([0.299, 0.587, 0.114])
    grayscale = np.dot(image, weights)  # 广播: (H,W,3) @ (3,) -> (H,W)
    return grayscale.astype(np.uint8)

def box_blur(image, kernel_size=3):
    """均值模糊滤波（简单版本，使用NumPy实现）"""
    if image.ndim == 3:  # RGB图像，对每个通道分别处理
        return np.stack([box_blur(image[:,:,c], kernel_size) for c in range(3)], axis=2)

    h, w = image.shape
    pad = kernel_size // 2
    # 使用零填充
    padded = np.pad(image.astype(np.float64), pad, mode='edge')
    result = np.zeros_like(image, dtype=np.float64)

    # 利用NumPy切片实现卷积（避免Python循环）
    for di in range(kernel_size):
        for dj in range(kernel_size):
            result += padded[di:di+h, dj:dj+w]

    return (result / (kernel_size * kernel_size)).astype(np.uint8)

# 测试
image = create_sample_image(200, 200)
print(f"原始图像: shape={image.shape}, dtype={image.dtype}")

grayscale = rgb_to_grayscale(image)
print(f"灰度图: shape={grayscale.shape}, dtype={grayscale.dtype}")

blurred = box_blur(image, kernel_size=5)
print(f"模糊图: shape={blurred.shape}, dtype={blurred.dtype}")

# 性能测试
import time
image_large = create_sample_image(1000, 1000)
start = time.perf_counter()
_ = rgb_to_grayscale(image_large)
print(f"灰度转换(1000x1000): {time.perf_counter()-start:.4f}s")

start = time.perf_counter()
_ = box_blur(image_large, kernel_size=5)
print(f"模糊滤波(1000x1000): {time.perf_counter()-start:.4f}s")
```

---

## Week 2: C/C++基础

---

### Day 1: C语言基础

#### 编译过程详解

```
源代码(.c) -> 预处理(.i) -> 编译(.s) -> 汇编(.o) -> 链接(可执行文件)
```

| 阶段 | 输入 | 输出 | 工作内容 | gcc选项 |
|------|------|------|---------|---------|
| 预处理 | .c | .i | 展开宏、包含头文件、去注释 | `-E` |
| 编译 | .i | .s | 将C代码转为汇编代码 | `-S` |
| 汇编 | .s | .o | 将汇编转为机器码（目标文件） | `-c` |
| 链接 | .o | 可执行 | 合并目标文件，解析符号引用 | 默认 |

```bash
# gcc常用选项
gcc hello.c -o hello        # 编译并输出可执行文件
gcc -E hello.c -o hello.i   # 只预处理
gcc -S hello.c -o hello.s   # 只编译到汇编
gcc -c hello.c -o hello.o   # 只编译到目标文件
gcc -Wall hello.c -o hello  # 开启所有警告
gcc -g hello.c -o hello     # 包含调试信息（gdb用）
gcc -O0 hello.c -o hello    # 不优化
gcc -O2 hello.c -o hello    # 中等优化
gcc -O3 hello.c -o hello    # 最高优化
```

**练习: 冒泡排序与二分查找**

```c
/* sort_search.c */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* 冒泡排序 */
void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (!swapped) break;  /* 优化: 如果一轮没有交换，说明已排序 */
    }
}

/* 二分查找 (要求数组已排序) */
int binary_search(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  /* 防止溢出 */
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;  /* 未找到 */
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("排序前: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    bubble_sort(arr, n);

    printf("排序后: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    int target = 25;
    int idx = binary_search(arr, n, target);
    if (idx != -1)
        printf("找到 %d 在索引 %d\n", target, idx);
    else
        printf("未找到 %d\n", target);

    return 0;
}

/* 编译和运行:
   gcc -O0 sort_search.c -o sort_O0 && time ./sort_O0
   gcc -O2 sort_search.c -o sort_O2 && time ./sort_O2
*/
```

---

### Day 2: 指针与内存管理

```c
/* dynamic_array.c - 可自动扩容的动态数组 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *data;      /* 指向数据的指针 */
    int size;       /* 当前元素数量 */
    int capacity;   /* 当前容量 */
} DynamicArray;

DynamicArray* da_create(int initial_capacity) {
    DynamicArray *da = (DynamicArray*)malloc(sizeof(DynamicArray));
    if (!da) { perror("malloc failed"); exit(1); }
    da->data = (int*)malloc(initial_capacity * sizeof(int));
    if (!da->data) { perror("malloc failed"); free(da); exit(1); }
    da->size = 0;
    da->capacity = initial_capacity;
    return da;
}

void da_push(DynamicArray *da, int value) {
    /* 容量不足时扩容为2倍 */
    if (da->size >= da->capacity) {
        da->capacity *= 2;
        int *new_data = (int*)realloc(da->data, da->capacity * sizeof(int));
        if (!new_data) { perror("realloc failed"); exit(1); }
        da->data = new_data;
        printf("[扩容] 新容量: %d\n", da->capacity);
    }
    da->data[da->size++] = value;
}

int da_get(DynamicArray *da, int index) {
    if (index < 0 || index >= da->size) {
        fprintf(stderr, "索引越界: %d (size=%d)\n", index, da->size);
        exit(1);
    }
    return da->data[index];
}

void da_free(DynamicArray *da) {
    free(da->data);  /* 先释放数据 */
    free(da);        /* 再释放结构体 */
}

int main() {
    DynamicArray *arr = da_create(4);

    for (int i = 0; i < 20; i++) {
        da_push(arr, i * 10);
    }

    printf("数组内容: ");
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", da_get(arr, i));
    }
    printf("\nsize=%d, capacity=%d\n", arr->size, arr->capacity);

    da_free(arr);  /* 务必释放！ */
    return 0;
}

/* 编译: gcc -Wall -g dynamic_array.c -o dynamic_array
   检测内存泄漏: valgrind --leak-check=full ./dynamic_array */
```

**链表实现**:

```c
/* linked_list.c */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *head;
    int size;
} LinkedList;

LinkedList* ll_create() {
    LinkedList *list = (LinkedList*)malloc(sizeof(LinkedList));
    list->head = NULL;
    list->size = 0;
    return list;
}

/* 头部插入 O(1) */
void ll_insert_front(LinkedList *list, int data) {
    Node *new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = list->head;
    list->head = new_node;
    list->size++;
}

/* 删除指定值 */
int ll_delete(LinkedList *list, int data) {
    Node *prev = NULL, *curr = list->head;
    while (curr) {
        if (curr->data == data) {
            if (prev) prev->next = curr->next;
            else list->head = curr->next;
            free(curr);
            list->size--;
            return 1;  /* 删除成功 */
        }
        prev = curr;
        curr = curr->next;
    }
    return 0;  /* 未找到 */
}

/* 遍历打印 */
void ll_print(LinkedList *list) {
    Node *curr = list->head;
    printf("[");
    while (curr) {
        printf("%d", curr->data);
        if (curr->next) printf(" -> ");
        curr = curr->next;
    }
    printf("] (size=%d)\n", list->size);
}

/* 释放所有节点 */
void ll_free(LinkedList *list) {
    Node *curr = list->head;
    while (curr) {
        Node *next = curr->next;
        free(curr);
        curr = next;
    }
    free(list);
}

int main() {
    LinkedList *list = ll_create();
    ll_insert_front(list, 30);
    ll_insert_front(list, 20);
    ll_insert_front(list, 10);
    ll_print(list);  /* [10 -> 20 -> 30] (size=3) */

    ll_delete(list, 20);
    ll_print(list);  /* [10 -> 30] (size=2) */

    ll_free(list);
    return 0;
}
```

**valgrind内存泄漏检测**:

```c
/* memory_leak.c - 故意制造内存泄漏 */
#include <stdlib.h>

int main() {
    /* 泄漏1: malloc后未free */
    int *p1 = (int*)malloc(100 * sizeof(int));
    /* 忘记 free(p1); */

    /* 泄漏2: 覆盖了指针，丢失了对分配内存的引用 */
    char *p2 = (char*)malloc(50);
    p2 = (char*)malloc(100);  /* 第一次分配的50字节泄漏了 */
    free(p2);  /* 只释放了第二次分配的 */

    return 0;
}
/* 编译: gcc -g memory_leak.c -o memory_leak
   检测: valgrind --leak-check=full --show-leak-kinds=all ./memory_leak
   输出会显示:
     definitely lost: 400 bytes in 1 blocks  (p1)
     definitely lost: 50 bytes in 1 blocks   (p2第一次)
*/
```

**重点: 指针相关概念**

| 概念 | 含义 | 危害 | 避免方法 |
|------|------|------|---------|
| 内存泄漏 | malloc后未free | 内存持续增长 | 始终配对使用malloc/free |
| 野指针 | 未初始化的指针 | 访问随机内存 | 声明时初始化为NULL |
| 悬空指针 | free后继续使用 | 访问已释放内存 | free后置为NULL |
| 越界访问 | 超出分配的内存范围 | 覆盖其他数据 | 检查边界，使用valgrind |

---

### Day 3-5: C++基础（OOP、模板、STL）

**多态示例**:

```cpp
// shapes.cpp
#include <iostream>
#include <vector>
#include <memory>
#include <cmath>

class Shape {
public:
    virtual ~Shape() = default;  // 虚析构函数（多态基类必须）
    virtual double area() const = 0;     // 纯虚函数
    virtual double perimeter() const = 0;
    virtual std::string name() const = 0;

    void print_info() const {
        std::cout << name() << ": area=" << area()
                  << ", perimeter=" << perimeter() << std::endl;
    }
};

class Circle : public Shape {
    double radius_;
public:
    explicit Circle(double r) : radius_(r) {}
    double area() const override { return M_PI * radius_ * radius_; }
    double perimeter() const override { return 2 * M_PI * radius_; }
    std::string name() const override { return "Circle"; }
};

class Rectangle : public Shape {
    double width_, height_;
public:
    Rectangle(double w, double h) : width_(w), height_(h) {}
    double area() const override { return width_ * height_; }
    double perimeter() const override { return 2 * (width_ + height_); }
    std::string name() const override { return "Rectangle"; }
};

int main() {
    // 用智能指针管理多态对象
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5.0));
    shapes.push_back(std::make_unique<Rectangle>(4.0, 6.0));
    shapes.push_back(std::make_unique<Circle>(3.0));

    for (const auto& shape : shapes) {
        shape->print_info();  // 多态调用
    }
    // 自动释放内存(unique_ptr析构时自动delete)
    return 0;
}
// 编译: g++ -std=c++17 shapes.cpp -o shapes
```

**模板与STL**:

```cpp
// stl_demo.cpp
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <memory>

// ---- 函数模板 ----
template <typename T>
T findMax(const std::vector<T>& vec) {
    if (vec.empty()) throw std::runtime_error("空向量");
    return *std::max_element(vec.begin(), vec.end());
}

// ---- 学生成绩管理系统 ----
struct Student {
    std::string name;
    std::vector<int> scores;

    double average() const {
        if (scores.empty()) return 0.0;
        return std::accumulate(scores.begin(), scores.end(), 0.0) / scores.size();
    }
};

int main() {
    // 模板函数
    std::vector<int> ints = {3, 1, 4, 1, 5, 9};
    std::vector<double> doubles = {3.14, 2.72, 1.41};
    std::cout << "int max: " << findMax(ints) << std::endl;
    std::cout << "double max: " << findMax(doubles) << std::endl;

    // 学生管理
    std::map<std::string, Student> students;
    students["S001"] = {"Alice", {90, 85, 92}};
    students["S002"] = {"Bob", {78, 88, 82}};
    students["S003"] = {"Charlie", {95, 90, 88}};

    // 遍历并输出
    for (const auto& [id, student] : students) {
        std::cout << id << " " << student.name
                  << " avg=" << student.average() << std::endl;
    }

    // 找到平均分最高的学生
    auto best = std::max_element(students.begin(), students.end(),
        [](const auto& a, const auto& b) {
            return a.second.average() < b.second.average();
        });
    std::cout << "最优: " << best->second.name
              << " avg=" << best->second.average() << std::endl;

    return 0;
}
```

**STL容器时间复杂度对比**:

| 容器 | 访问 | 插入/删除(头) | 插入/删除(尾) | 查找 | 特点 |
|------|------|------------|------------|------|------|
| `vector` | O(1) | O(n) | O(1)均摊 | O(n) | 连续内存，缓存友好 |
| `deque` | O(1) | O(1) | O(1) | O(n) | 双端队列 |
| `list` | O(n) | O(1) | O(1) | O(n) | 双向链表 |
| `map` | O(log n) | - | - | O(log n) | 红黑树，有序 |
| `unordered_map` | O(1)平均 | - | - | O(1)平均 | 哈希表，无序 |
| `set` | - | - | - | O(log n) | 红黑树，有序唯一 |

**智能指针使用场景**:

| 智能指针 | 所有权 | 拷贝 | 引用计数 | 适用场景 |
|---------|--------|------|---------|---------|
| `unique_ptr` | 独占 | 不可拷贝，可移动 | 无 | 独一无二的资源拥有者 |
| `shared_ptr` | 共享 | 可拷贝 | 有 | 多个对象共享同一资源 |
| `weak_ptr` | 无（观察者） | 可拷贝 | 不增加 | 解决shared_ptr循环引用 |

---

### Day 6-7: C/C++与Python交互

#### pybind11示例

```cpp
// mylib.cpp - C++库
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <numeric>
#include <cmath>

namespace py = pybind11;

class Matrix {
    std::vector<std::vector<double>> data_;
    int rows_, cols_;
public:
    Matrix(int rows, int cols) : rows_(rows), cols_(cols) {
        data_.resize(rows, std::vector<double>(cols, 0.0));
    }

    void set(int i, int j, double val) { data_[i][j] = val; }
    double get(int i, int j) const { return data_[i][j]; }
    int rows() const { return rows_; }
    int cols() const { return cols_; }

    Matrix multiply(const Matrix& other) const {
        Matrix result(rows_, other.cols_);
        for (int i = 0; i < rows_; i++)
            for (int j = 0; j < other.cols_; j++)
                for (int k = 0; k < cols_; k++)
                    result.data_[i][j] += data_[i][k] * other.data_[k][j];
        return result;
    }

    std::string repr() const {
        return "Matrix(" + std::to_string(rows_) + "x" + std::to_string(cols_) + ")";
    }
};

PYBIND11_MODULE(mylib, m) {
    m.doc() = "C++矩阵库Python绑定";

    py::class_<Matrix>(m, "Matrix")
        .def(py::init<int, int>())
        .def("set", &Matrix::set)
        .def("get", &Matrix::get)
        .def("rows", &Matrix::rows)
        .def("cols", &Matrix::cols)
        .def("multiply", &Matrix::multiply)
        .def("__repr__", &Matrix::repr);
}
// 编译: c++ -O3 -shared -std=c++17 -fPIC $(python3 -m pybind11 --includes) mylib.cpp -o mylib$(python3-config --extension-suffix)
```

```python
# 使用pybind11封装的库
import mylib

a = mylib.Matrix(2, 3)
b = mylib.Matrix(3, 2)
for i in range(2):
    for j in range(3):
        a.set(i, j, (i + 1) * (j + 1))
for i in range(3):
    for j in range(2):
        b.set(i, j, (i + 1) + (j + 1))

c = a.multiply(b)
print(f"结果: {c}")
for i in range(c.rows()):
    for j in range(c.cols()):
        print(f"  c[{i}][{j}] = {c.get(i, j)}")
```

#### ctypes调用C库

```c
// matrix_c.c - C矩阵乘法库
#include <stdlib.h>

void matrix_multiply(double *A, double *B, double *C, int M, int N, int K) {
    /* C[M,N] = A[M,K] * B[K,N] */
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++) {
            C[i * N + j] = 0.0;
            for (int k = 0; k < K; k++)
                C[i * N + j] += A[i * K + k] * B[k * N + j];
        }
}
// 编译: gcc -shared -fPIC -O2 matrix_c.c -o libmatrix.so
```

```python
# 用ctypes从Python调用C矩阵乘法
import ctypes
import numpy as np
import time

# 加载共享库
lib = ctypes.CDLL('./libmatrix.so')

# 定义函数签名
lib.matrix_multiply.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # A
    ctypes.POINTER(ctypes.c_double),  # B
    ctypes.POINTER(ctypes.c_double),  # C
    ctypes.c_int,                      # M
    ctypes.c_int,                      # N
    ctypes.c_int,                      # K
]
lib.matrix_multiply.restype = None

def c_matrix_multiply(A, B):
    """调用C库进行矩阵乘法"""
    M, K = A.shape
    K2, N = B.shape
    assert K == K2
    C = np.zeros((M, N), dtype=np.float64)
    lib.matrix_multiply(
        A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        M, N, K
    )
    return C

# 测试
size = 256
A = np.random.randn(size, size)
B = np.random.randn(size, size)

start = time.perf_counter()
C_ctypes = c_matrix_multiply(A, B)
print(f"C (ctypes): {time.perf_counter()-start:.4f}s")

start = time.perf_counter()
C_numpy = A @ B
print(f"NumPy:      {time.perf_counter()-start:.4f}s")

# 验证结果一致
print(f"结果一致: {np.allclose(C_ctypes, C_numpy)}")
```

**gdb核心命令速查**:

| 命令 | 缩写 | 功能 |
|------|------|------|
| `break main` | `b main` | 在main函数设断点 |
| `break file.c:20` | `b file.c:20` | 在第20行设断点 |
| `run` | `r` | 运行程序 |
| `next` | `n` | 下一行（不进入函数） |
| `step` | `s` | 下一行（进入函数） |
| `continue` | `c` | 继续运行到下一个断点 |
| `print x` | `p x` | 打印变量x的值 |
| `print *ptr` | `p *ptr` | 打印指针指向的值 |
| `backtrace` | `bt` | 打印调用栈 |
| `info locals` | - | 打印当前函数所有局部变量 |
| `watch x` | - | 当x的值变化时停止 |
| `quit` | `q` | 退出gdb |

---

## Week 3: Python自动化测试框架深入

---

### Day 1-2: pytest高级特性与API测试

#### conftest.py层级配置

```
tests/
├── conftest.py              # 顶层conftest (session级fixture)
├── unit/
│   ├── conftest.py          # 单元测试conftest
│   └── test_core.py
├── integration/
│   ├── conftest.py          # 集成测试conftest
│   └── test_api.py
└── performance/
    └── test_benchmark.py
```

```python
# tests/conftest.py (顶层 - session级)
import pytest
import logging

@pytest.fixture(scope="session")
def base_url():
    """API基础URL（整个测试会话共享）"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """全局日志配置"""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s')

@pytest.fixture
def sample_data():
    """通用测试数据"""
    return {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1
    }
```

```python
# tests/integration/conftest.py
import pytest
import requests

@pytest.fixture(scope="module")
def api_session(base_url):
    """共享HTTP session（模块级）"""
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    yield session
    session.close()
```

#### 完整API测试套件

```python
# tests/integration/test_api.py
import pytest
import requests
import jsonschema

# ---- JSON Schema定义 ----
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"},
    },
    "required": ["id", "title", "body", "userId"]
}

POSTS_LIST_SCHEMA = {
    "type": "array",
    "items": POST_SCHEMA
}


class TestGetPosts:
    """GET /posts 测试"""

    def test_get_all_posts(self, api_session, base_url):
        """获取所有帖子"""
        resp = api_session.get(f"{base_url}/posts")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) > 0
        jsonschema.validate(data, POSTS_LIST_SCHEMA)

    def test_get_single_post(self, api_session, base_url):
        """获取单个帖子"""
        resp = api_session.get(f"{base_url}/posts/1")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1
        jsonschema.validate(data, POST_SCHEMA)

    def test_get_nonexistent_post(self, api_session, base_url):
        """获取不存在的帖子"""
        resp = api_session.get(f"{base_url}/posts/99999")
        assert resp.status_code == 404

    @pytest.mark.parametrize("post_id", [1, 2, 3, 50, 100])
    def test_get_various_posts(self, api_session, base_url, post_id):
        """参数化测试不同ID的帖子"""
        resp = api_session.get(f"{base_url}/posts/{post_id}")
        assert resp.status_code == 200
        assert resp.json()["id"] == post_id


class TestCreatePost:
    """POST /posts 测试"""

    def test_create_post(self, api_session, base_url, sample_data):
        resp = api_session.post(f"{base_url}/posts", json=sample_data)
        assert resp.status_code == 201
        data = resp.json()
        assert data["title"] == sample_data["title"]
        assert "id" in data

    @pytest.mark.parametrize("field", ["title", "body", "userId"])
    def test_create_post_with_missing_field(self, api_session, base_url, sample_data, field):
        """测试缺少字段的情况"""
        incomplete_data = {k: v for k, v in sample_data.items() if k != field}
        resp = api_session.post(f"{base_url}/posts", json=incomplete_data)
        # JSONPlaceholder不做严格校验，实际API应返回400
        assert resp.status_code in [201, 400]


class TestUpdatePost:
    """PUT /posts/:id 测试"""

    def test_update_post(self, api_session, base_url):
        update_data = {"title": "Updated Title", "body": "Updated body", "userId": 1}
        resp = api_session.put(f"{base_url}/posts/1", json=update_data)
        assert resp.status_code == 200
        assert resp.json()["title"] == "Updated Title"


class TestDeletePost:
    """DELETE /posts/:id 测试"""

    def test_delete_post(self, api_session, base_url):
        resp = api_session.delete(f"{base_url}/posts/1")
        assert resp.status_code == 200
```

---

### Day 3: 性能测试基础

```python
# benchmark_demo.py - 性能基准测试
import time
import statistics
from typing import Callable, Any
from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    """基准测试结果"""
    name: str
    iterations: int
    times: list
    p50: float
    p90: float
    p99: float
    mean: float
    min_time: float
    max_time: float
    ops_per_sec: float

def benchmark(func: Callable, *args, iterations: int = 100,
              warmup: int = 10, name: str = None, **kwargs) -> BenchmarkResult:
    """通用基准测试函数"""
    name = name or func.__name__

    # 预热
    for _ in range(warmup):
        func(*args, **kwargs)

    # 正式测试
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    times.sort()
    return BenchmarkResult(
        name=name,
        iterations=iterations,
        times=times,
        p50=times[int(iterations * 0.50)],
        p90=times[int(iterations * 0.90)],
        p99=times[int(iterations * 0.99)],
        mean=statistics.mean(times),
        min_time=min(times),
        max_time=max(times),
        ops_per_sec=iterations / sum(times),
    )

def print_benchmark_result(result: BenchmarkResult):
    """打印基准测试结果"""
    print(f"\n{'='*50}")
    print(f"基准测试: {result.name}")
    print(f"{'='*50}")
    print(f"  迭代次数:  {result.iterations}")
    print(f"  平均耗时:  {result.mean*1000:.3f} ms")
    print(f"  P50:       {result.p50*1000:.3f} ms")
    print(f"  P90:       {result.p90*1000:.3f} ms")
    print(f"  P99:       {result.p99*1000:.3f} ms")
    print(f"  最小:      {result.min_time*1000:.3f} ms")
    print(f"  最大:      {result.max_time*1000:.3f} ms")
    print(f"  吞吐量:    {result.ops_per_sec:.1f} ops/s")

# 测试示例
def sort_list(n=10000):
    import random
    data = [random.random() for _ in range(n)]
    data.sort()

result = benchmark(sort_list, iterations=50, name="List Sort (10K)")
print_benchmark_result(result)
```

**P50/P90/P99延迟解释**:

| 百分位 | 含义 | 重要性 |
|--------|------|--------|
| P50 (中位数) | 50%的请求在此时间内完成 | 反映典型用户体验 |
| P90 | 90%的请求在此时间内完成 | SLA常用指标 |
| P99 | 99%的请求在此时间内完成 | 反映尾延迟(tail latency) |
| P999 | 99.9%的请求在此时间内完成 | 极端情况监控 |

---

### Day 6-7: 综合项目 - API自动化测试框架

```python
# ---- framework/config.py ----
import yaml
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Environment:
    name: str
    base_url: str
    timeout: int = 30
    headers: Dict[str, str] = None

class ConfigManager:
    """多环境配置管理"""
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self._config = yaml.safe_load(f)
        self._env_name = self._config.get("active_env", "dev")

    @property
    def env(self) -> Environment:
        env_data = self._config["environments"][self._env_name]
        return Environment(
            name=self._env_name,
            base_url=env_data["base_url"],
            timeout=env_data.get("timeout", 30),
            headers=env_data.get("headers", {})
        )

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)
```

```yaml
# config.yaml
active_env: dev

environments:
  dev:
    base_url: "http://localhost:8000"
    timeout: 10
    headers:
      X-API-Key: "dev-key"
  staging:
    base_url: "https://staging.api.example.com"
    timeout: 30
    headers:
      X-API-Key: "staging-key"
  prod:
    base_url: "https://api.example.com"
    timeout: 60
    headers:
      X-API-Key: "prod-key"
```

```python
# ---- framework/api_client.py ----
import requests
import logging
import time
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class APIClient:
    """封装HTTP请求，带重试、日志、超时"""

    def __init__(self, base_url: str, headers: Dict[str, str] = None,
                 timeout: int = 30, max_retries: int = 3):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)
        self.timeout = timeout
        self.max_retries = max_retries

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"
        kwargs.setdefault('timeout', self.timeout)

        for attempt in range(1, self.max_retries + 1):
            start = time.perf_counter()
            try:
                response = self.session.request(method, url, **kwargs)
                elapsed = time.perf_counter() - start
                logger.info(
                    f"[{method}] {url} -> {response.status_code} ({elapsed:.3f}s)"
                )
                return response
            except requests.RequestException as e:
                elapsed = time.perf_counter() - start
                logger.warning(
                    f"[{method}] {url} 失败 (尝试{attempt}/{self.max_retries}): {e} ({elapsed:.3f}s)"
                )
                if attempt == self.max_retries:
                    raise

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request('GET', path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request('POST', path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request('PUT', path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request('DELETE', path, **kwargs)

    def close(self):
        self.session.close()
```

```python
# ---- framework/assertions.py ----
import jsonschema
from typing import Any, Dict

class ResponseAssertions:
    """响应断言封装"""

    def __init__(self, response):
        self.response = response
        self.data = None
        try:
            self.data = response.json()
        except Exception:
            pass

    def status_code(self, expected: int) -> 'ResponseAssertions':
        assert self.response.status_code == expected, \
            f"期望状态码 {expected}, 实际 {self.response.status_code}"
        return self

    def json_schema(self, schema: Dict) -> 'ResponseAssertions':
        jsonschema.validate(self.data, schema)
        return self

    def has_field(self, field: str) -> 'ResponseAssertions':
        assert field in self.data, f"响应中缺少字段: {field}"
        return self

    def field_equals(self, field: str, expected: Any) -> 'ResponseAssertions':
        actual = self.data.get(field)
        assert actual == expected, f"字段 {field}: 期望 {expected}, 实际 {actual}"
        return self

    def response_time_under(self, max_seconds: float) -> 'ResponseAssertions':
        elapsed = self.response.elapsed.total_seconds()
        assert elapsed < max_seconds, \
            f"响应时间 {elapsed:.3f}s 超过阈值 {max_seconds}s"
        return self


def assert_response(response) -> ResponseAssertions:
    """链式断言入口"""
    return ResponseAssertions(response)
```

---

# 第二阶段: 深度学习基础 + GPU/CUDA基础（Week 4-6）

---

## Week 4: 深度学习基础

---

### Day 1: 机器学习基础概念

#### 1.1 监督学习 vs 无监督学习 vs 强化学习

| 类型 | 数据特点 | 目标 | 典型任务 | 算法示例 |
|------|---------|------|---------|---------|
| 监督学习 | 有标签 (X→Y) | 学习输入到输出的映射 | 分类、回归 | 线性回归、SVM、神经网络 |
| 无监督学习 | 无标签 (只有X) | 发现数据内在结构 | 聚类、降维 | K-means、PCA、自编码器 |
| 强化学习 | 环境反馈(奖励) | 学习最优策略 | 游戏、机器人控制 | Q-Learning、PPO |

#### 1.2 训练(Training) vs 推理(Inference) —— 核心区别

这是本岗位最核心的概念之一：

| 维度 | 训练(Training) | 推理(Inference) |
|------|--------------|----------------|
| **目标** | 学习模型参数（权重） | 用训练好的模型做预测 |
| **计算** | 前向传播 + 反向传播 + 参数更新 | 仅前向传播 |
| **数据** | 大量训练数据，多轮(epoch) | 单条或小批量输入 |
| **精度** | 通常需要FP32或BF16 | 可用FP16/INT8/INT4降低精度 |
| **显存** | 需存储梯度、优化器状态（3-4x模型大小） | 只需存储模型权重 + KV Cache |
| **硬件** | 多卡/集群（A100/H100） | 可单卡或边缘设备 |
| **延迟要求** | 不敏感（天/周级） | 极敏感（毫秒/秒级） |
| **优化目标** | 收敛速度、最终精度 | 延迟、吞吐量、资源效率 |
| **批大小** | 通常较大(32-4096) | 从1到动态批处理 |
| **梯度** | 需要计算和存储 | 不需要（torch.no_grad） |

#### 1.3 梯度下降与反向传播

```python
import numpy as np

# ---- 手动实现线性回归的梯度下降 ----

# 生成数据: y = 3x + 2 + noise
np.random.seed(42)
X = np.random.randn(100, 1)
y = 3 * X + 2 + np.random.randn(100, 1) * 0.3

# 初始化参数
w = np.random.randn(1, 1)  # 权重
b = np.zeros((1, 1))        # 偏置
learning_rate = 0.1
epochs = 100

print(f"初始参数: w={w[0,0]:.4f}, b={b[0,0]:.4f}")

for epoch in range(epochs):
    # 1. 前向传播: 计算预测值
    y_pred = X @ w + b  # (100,1)

    # 2. 计算损失: MSE = (1/n) * sum((y_pred - y)^2)
    loss = np.mean((y_pred - y) ** 2)

    # 3. 反向传播: 计算梯度
    # dL/dw = (2/n) * X^T @ (y_pred - y)
    # dL/db = (2/n) * sum(y_pred - y)
    n = len(X)
    dw = (2 / n) * X.T @ (y_pred - y)
    db = (2 / n) * np.sum(y_pred - y)

    # 4. 参数更新
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 20 == 0:
        print(f"Epoch {epoch:3d}: loss={loss:.4f}, w={w[0,0]:.4f}, b={b[0,0]:.4f}")

print(f"\n最终: w={w[0,0]:.4f} (真实值: 3.0), b={b[0,0]:.4f} (真实值: 2.0)")
```

#### 1.4 用numpy实现2层神经网络

```python
import numpy as np

class TwoLayerNet:
    """
    2层神经网络（纯numpy）
    结构: 输入层 -> 隐藏层(ReLU) -> 输出层(Softmax)
    """
    def __init__(self, input_size, hidden_size, output_size):
        # Xavier初始化
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def forward(self, X):
        """前向传播"""
        self.z1 = X @ self.W1 + self.b1      # 线性变换
        self.a1 = self.relu(self.z1)          # ReLU激活
        self.z2 = self.a1 @ self.W2 + self.b2 # 线性变换
        self.a2 = self.softmax(self.z2)        # Softmax输出
        return self.a2

    def compute_loss(self, y_pred, y_true):
        """交叉熵损失"""
        n = len(y_true)
        log_probs = -np.log(y_pred[range(n), y_true] + 1e-8)
        return np.mean(log_probs)

    def backward(self, X, y_true, learning_rate=0.01):
        """反向传播"""
        n = len(y_true)

        # 输出层梯度
        dz2 = self.a2.copy()
        dz2[range(n), y_true] -= 1
        dz2 /= n

        dW2 = self.a1.T @ dz2
        db2 = np.sum(dz2, axis=0, keepdims=True)

        # 隐藏层梯度
        da1 = dz2 @ self.W2.T
        dz1 = da1 * self.relu_derivative(self.z1)

        dW1 = X.T @ dz1
        db1 = np.sum(dz1, axis=0, keepdims=True)

        # 参数更新
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1

    def predict(self, X):
        probs = self.forward(X)
        return np.argmax(probs, axis=1)

# ---- 训练示例 ----
from sklearn.datasets import make_moons

# 生成二分类数据
X, y = make_moons(n_samples=500, noise=0.2, random_state=42)

# 创建网络
net = TwoLayerNet(input_size=2, hidden_size=32, output_size=2)

# 训练
for epoch in range(1000):
    # 前向传播
    probs = net.forward(X)
    loss = net.compute_loss(probs, y)

    # 反向传播
    net.backward(X, y, learning_rate=0.5)

    if epoch % 100 == 0:
        predictions = net.predict(X)
        accuracy = np.mean(predictions == y)
        print(f"Epoch {epoch}: loss={loss:.4f}, accuracy={accuracy:.4f}")
```

#### 1.5 评估指标

| 指标 | 公式 | 含义 |
|------|------|------|
| Accuracy | (TP+TN) / (TP+TN+FP+FN) | 总体准确率 |
| Precision | TP / (TP+FP) | 预测为正的样本中，真正是正的比例 |
| Recall | TP / (TP+FN) | 所有正样本中，被正确预测出来的比例 |
| F1 Score | 2 * P * R / (P + R) | Precision和Recall的调和平均 |

---

### Day 3: Transformer架构 —— Self-Attention详解

#### Self-Attention计算过程

这是所有LLM和推理优化技术的基础，必须深刻理解：

```
输入: X (n个token的embedding矩阵, shape: [n, d_model])

步骤1: 通过线性变换生成Q, K, V
  Q = X @ W_Q    (shape: [n, d_k])
  K = X @ W_K    (shape: [n, d_k])
  V = X @ W_V    (shape: [n, d_v])

步骤2: 计算注意力分数
  Score = Q @ K^T    (shape: [n, n])  -- 这就是O(n^2)复杂度的来源！

步骤3: 缩放
  Score = Score / sqrt(d_k)    -- 防止softmax梯度消失

步骤4: Softmax归一化
  Attention_Weights = Softmax(Score)    (shape: [n, n], 每行和为1)

步骤5: 加权求和
  Output = Attention_Weights @ V    (shape: [n, d_v])
```

**手动计算2x2 Self-Attention示例**:

```python
import numpy as np

# 假设有2个token，embedding维度为3
X = np.array([
    [1.0, 0.0, 1.0],  # Token 1
    [0.0, 1.0, 1.0],  # Token 2
])

# 权重矩阵 (简化: d_model=3, d_k=d_v=2)
W_Q = np.array([[1, 0], [0, 1], [1, 0]])  # (3, 2)
W_K = np.array([[0, 1], [1, 0], [0, 1]])  # (3, 2)
W_V = np.array([[1, 0], [0, 1], [1, 1]])  # (3, 2)

# 步骤1: 生成Q, K, V
Q = X @ W_Q  # (2, 2)
K = X @ W_K  # (2, 2)
V = X @ W_V  # (2, 2)
print(f"Q =\n{Q}")
print(f"K =\n{K}")
print(f"V =\n{V}")

# 步骤2: 计算注意力分数 Q @ K^T
d_k = K.shape[1]
scores = Q @ K.T  # (2, 2)
print(f"\nScores (Q @ K^T) =\n{scores}")

# 步骤3: 缩放
scores_scaled = scores / np.sqrt(d_k)
print(f"Scaled Scores =\n{scores_scaled}")

# 步骤4: Softmax
def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

attention_weights = softmax(scores_scaled)
print(f"Attention Weights =\n{attention_weights}")
print(f"每行之和 = {attention_weights.sum(axis=1)}")  # [1.0, 1.0]

# 步骤5: 加权求和
output = attention_weights @ V
print(f"\nOutput =\n{output}")

# attention_weights[i][j] = Token i 对 Token j 的注意力权重
# 权重越大，说明Token i越"关注"Token j
```

**Multi-Head Attention**: 将Q, K, V分成多个"头"(head)，每个头独立做Attention，最后拼接：

```
MultiHead(Q,K,V) = Concat(head_1, ..., head_h) @ W_O
  其中 head_i = Attention(Q @ W_Q_i, K @ W_K_i, V @ W_V_i)
```

---

### Day 4: LLM推理核心 —— Prefill/Decode与KV Cache

#### Prefill阶段 vs Decode阶段

```
用户输入: "请解释什么是深度学习"

=== Prefill阶段 ===
- 输入: 整个prompt的所有token [请, 解释, 什么, 是, 深度, 学习]
- 操作: 一次性并行处理所有token
- 输出: 第一个生成token + 所有token的KV Cache
- 特点: 计算密集型(Compute-bound), GPU计算单元满载
- 决定: TTFT (Time To First Token)

=== Decode阶段 ===
- 输入: 上一步生成的token (每次只有1个)
- 操作: 查询KV Cache + 计算新token
- 输出: 下一个token
- 特点: 内存密集型(Memory-bound), 大量时间花在读取KV Cache
- 决定: TPOT (Time Per Output Token)
- 循环直到: 遇到结束符或达到max_tokens

为什么Decode是Memory-bound?
- 每个token的计算量很小(只有1个token的QKV计算)
- 但需要读取整个KV Cache来做Attention
- GPU的算力远远超过需要的计算量, 瓶颈在于内存读取速度
```

#### KV Cache原理

```python
# KV Cache原理演示（伪代码）

def llm_inference_without_cache(model, input_tokens):
    """不使用KV Cache的推理（极慢）"""
    generated = list(input_tokens)
    for step in range(max_new_tokens):
        # 每次都重新计算所有token的K和V
        all_tokens = generated
        output = model.forward(all_tokens)  # O(n^2) 每一步！
        next_token = sample(output[-1])
        generated.append(next_token)
    return generated

def llm_inference_with_cache(model, input_tokens):
    """使用KV Cache的推理（高效）"""
    # Prefill: 一次性处理所有输入token
    output, kv_cache = model.forward(input_tokens, kv_cache=None)
    generated = [sample(output[-1])]

    for step in range(max_new_tokens):
        # Decode: 只处理新生成的1个token，利用缓存的KV
        output, kv_cache = model.forward(
            [generated[-1]],     # 只输入最新1个token
            kv_cache=kv_cache     # 传入之前缓存的KV
        )
        next_token = sample(output[-1])
        generated.append(next_token)

        # kv_cache在每步自动追加新token的K,V
    return generated
```

#### KV Cache大小计算

```python
def calculate_kv_cache_size(
    num_layers: int,
    num_kv_heads: int,
    head_dim: int,
    seq_len: int,
    batch_size: int = 1,
    dtype_bytes: int = 2  # FP16 = 2 bytes
) -> dict:
    """
    计算KV Cache大小

    KV Cache = 2 (K+V) * num_layers * num_kv_heads * head_dim * seq_len * batch_size * dtype_bytes
    """
    kv_cache_bytes = (
        2 *               # K和V各一份
        num_layers *       # 每层都有
        num_kv_heads *     # KV头数(GQA可能少于Q头数)
        head_dim *         # 每个头的维度
        seq_len *          # 序列长度
        batch_size *       # 批大小
        dtype_bytes        # 每个元素的字节数
    )
    return {
        "bytes": kv_cache_bytes,
        "MB": kv_cache_bytes / (1024 ** 2),
        "GB": kv_cache_bytes / (1024 ** 3),
    }

# ---- 各模型KV Cache大小 (FP16, 单条序列, seq_len=2048) ----
models = {
    "LLaMA-7B":  {"num_layers": 32, "num_kv_heads": 32, "head_dim": 128},
    "LLaMA-13B": {"num_layers": 40, "num_kv_heads": 40, "head_dim": 128},
    "LLaMA-70B": {"num_layers": 80, "num_kv_heads": 8, "head_dim": 128},  # GQA: 8 KV heads
    "Mistral-7B": {"num_layers": 32, "num_kv_heads": 8, "head_dim": 128},  # GQA: 8 KV heads
}

print(f"{'模型':<15} {'KV Cache (2048 tokens)':<25} {'KV Cache (4096 tokens)':<25}")
print("-" * 65)
for name, params in models.items():
    size_2k = calculate_kv_cache_size(**params, seq_len=2048)
    size_4k = calculate_kv_cache_size(**params, seq_len=4096)
    print(f"{name:<15} {size_2k['MB']:.0f} MB ({size_2k['GB']:.2f} GB)     "
          f"{size_4k['MB']:.0f} MB ({size_4k['GB']:.2f} GB)")

# ---- 模型参数显存计算 ----
def calculate_model_memory(num_params_billions: float, dtype: str = "fp16") -> dict:
    """计算模型权重占用的显存"""
    bytes_per_param = {"fp32": 4, "fp16": 2, "bf16": 2, "int8": 1, "int4": 0.5}
    total_bytes = num_params_billions * 1e9 * bytes_per_param[dtype]
    return {"GB": total_bytes / (1024**3), "dtype": dtype}

print("\n--- 7B模型不同精度的显存需求 ---")
for dtype in ["fp32", "fp16", "int8", "int4"]:
    mem = calculate_model_memory(7, dtype)
    print(f"  {dtype:<5}: {mem['GB']:.1f} GB")
```

---

### Day 5: 模型格式与精度类型

**精度类型详细对比**:

| 类型 | 位数 | 范围 | 显存(7B) | 速度 | 精度 | 适用场景 |
|------|------|------|---------|------|------|---------|
| FP32 | 32 | ~1e38 | ~26GB | 基线 | 最高 | 训练 |
| FP16 | 16 | ~65504 | ~13GB | ~2x | 高 | 推理默认 |
| BF16 | 16 | ~3.4e38 | ~13GB | ~2x | 高(大范围) | 训练+推理 |
| INT8 | 8 | -128~127 | ~6.5GB | ~3-4x | 较高 | 推理优化 |
| INT4 | 4 | -8~7 | ~3.3GB | ~4-6x | 中等 | 边缘部署 |
| FP8(E4M3) | 8 | ~448 | ~6.5GB | ~3-4x | 较高 | H100推理 |

**FP16 vs BF16**:
- FP16: 1位符号 + 5位指数 + 10位尾数 → 精度高但范围小(易溢出)
- BF16: 1位符号 + 8位指数 + 7位尾数 → 范围大(等同FP32)但精度低

---

## Week 5: GPU架构与CUDA基础

---

### Day 1: GPU硬件架构

#### CPU vs GPU架构对比

| 特性 | CPU | GPU |
|------|-----|-----|
| 设计哲学 | 延迟优化(Latency) | 吞吐量优化(Throughput) |
| 核心数量 | 4-128个复杂核心 | 数千个简单核心 |
| 时钟频率 | 3-5+ GHz | 1-2 GHz |
| 缓存 | 大(MB级L1/L2/L3) | 小(KB级L1/L2) |
| 控制逻辑 | 复杂(分支预测、乱序执行) | 简单(SIMT) |
| 内存带宽 | ~50-100 GB/s | ~1-3 TB/s(HBM) |
| 适合任务 | 串行、复杂逻辑、低延迟 | 大规模并行、高吞吐 |

#### NVIDIA GPU关键规格对比

| 规格 | A100 (80GB) | H100 (80GB) | A10 (24GB) | RTX 4090 (24GB) |
|------|------------|------------|----------|----------------|
| 架构 | Ampere | Hopper | Ampere | Ada Lovelace |
| CUDA Core | 6912 | 14592 | 9216 | 16384 |
| Tensor Core | 432 (3代) | 456 (4代) | 288 (3代) | 512 (4代) |
| FP16 TFLOPS | 312 | 989 | 125 | 330 |
| 显存 | 80GB HBM2e | 80GB HBM3 | 24GB GDDR6 | 24GB GDDR6X |
| 显存带宽 | 2039 GB/s | 3350 GB/s | 600 GB/s | 1008 GB/s |
| 互联 | NVLink 600GB/s | NVLink 900GB/s | PCIe 4.0 | PCIe 4.0 |
| FP8支持 | 否 | 是 | 否 | 是 |
| 定位 | 数据中心 | 数据中心 | 推理 | 消费级/研究 |

#### Memory-bound vs Compute-bound

**Roofline Model**:
- **算术强度(Arithmetic Intensity)** = FLOPs / Bytes (每传输1字节数据执行的浮点运算数)
- 如果算术强度 < 硬件的FLOPs/Bandwidth → **Memory-bound**
- 如果算术强度 > 硬件的FLOPs/Bandwidth → **Compute-bound**

```
以A100为例:
  FP16计算能力: 312 TFLOPS
  显存带宽: 2039 GB/s
  平衡点(Ridge Point): 312000 / 2039 ≈ 153 FLOPs/Byte

操作分析:
  - 向量加法: 每元素2bytes读 + 2bytes写 + 1FLOP → 0.25 FLOPs/Byte → Memory-bound
  - 矩阵乘法(大): 接近 2*N FLOPs/Byte → 当N>77时 Compute-bound
  - LLM Decode: 读取大量KV Cache, 计算量小 → Memory-bound
  - LLM Prefill: 大矩阵乘法 → Compute-bound
```

#### Tensor Core vs CUDA Core

| 特性 | CUDA Core | Tensor Core |
|------|-----------|-------------|
| 运算单元 | 标量(FMA: a*b+c) | 矩阵(D=A*B+C, 4x4) |
| 每周期运算量 | 1 FMA | 16+ FMA (4x4矩阵) |
| 支持精度 | FP32/FP64/INT32 | FP16/BF16/TF32/FP8/INT8/INT4 |
| 加速倍数 | 基线 | 对矩阵运算加速8-16x |
| 适用场景 | 通用计算 | 矩阵乘法(GEMM)、深度学习 |

---

### Day 2-3: CUDA编程

```cuda
// vector_add.cu - CUDA向量加法
#include <stdio.h>
#include <cuda_runtime.h>

// GPU Kernel函数
__global__ void vectorAdd(float *A, float *B, float *C, int N) {
    // 计算全局线程ID
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N) {
        C[i] = A[i] + B[i];
    }
}

int main() {
    int N = 1 << 20;  // 1M elements
    size_t size = N * sizeof(float);

    // 1. 分配Host内存
    float *h_A = (float*)malloc(size);
    float *h_B = (float*)malloc(size);
    float *h_C = (float*)malloc(size);

    // 初始化
    for (int i = 0; i < N; i++) {
        h_A[i] = rand() / (float)RAND_MAX;
        h_B[i] = rand() / (float)RAND_MAX;
    }

    // 2. 分配Device内存
    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, size);
    cudaMalloc(&d_B, size);
    cudaMalloc(&d_C, size);

    // 3. Host -> Device 数据拷贝
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

    // 4. 启动Kernel
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    printf("Grid: %d blocks, Block: %d threads\n", blocksPerGrid, threadsPerBlock);

    // 计时
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start);

    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);

    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
    printf("Kernel执行时间: %.3f ms\n", milliseconds);

    // 5. Device -> Host 拷贝结果
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

    // 6. 验证
    for (int i = 0; i < 5; i++) {
        printf("%.2f + %.2f = %.2f\n", h_A[i], h_B[i], h_C[i]);
    }

    // 7. 释放内存
    cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
    free(h_A); free(h_B); free(h_C);
    return 0;
}
// 编译: nvcc vector_add.cu -o vector_add
```

**Tiled矩阵乘法（Shared Memory优化）**:

```cuda
// tiled_matmul.cu
#include <stdio.h>
#include <cuda_runtime.h>

#define TILE_SIZE 16

__global__ void matmulTiled(float *A, float *B, float *C, int N) {
    // 声明Shared Memory
    __shared__ float sA[TILE_SIZE][TILE_SIZE];
    __shared__ float sB[TILE_SIZE][TILE_SIZE];

    int row = blockIdx.y * TILE_SIZE + threadIdx.y;
    int col = blockIdx.x * TILE_SIZE + threadIdx.x;
    float sum = 0.0f;

    // 分块计算
    for (int tile = 0; tile < (N + TILE_SIZE - 1) / TILE_SIZE; tile++) {
        // 每个线程加载一个元素到Shared Memory
        if (row < N && tile * TILE_SIZE + threadIdx.x < N)
            sA[threadIdx.y][threadIdx.x] = A[row * N + tile * TILE_SIZE + threadIdx.x];
        else
            sA[threadIdx.y][threadIdx.x] = 0.0f;

        if (col < N && tile * TILE_SIZE + threadIdx.y < N)
            sB[threadIdx.y][threadIdx.x] = B[(tile * TILE_SIZE + threadIdx.y) * N + col];
        else
            sB[threadIdx.y][threadIdx.x] = 0.0f;

        __syncthreads();  // 等所有线程加载完成

        // 在Shared Memory中计算
        for (int k = 0; k < TILE_SIZE; k++)
            sum += sA[threadIdx.y][k] * sB[k][threadIdx.x];

        __syncthreads();  // 确保所有线程完成计算再加载下一块
    }

    if (row < N && col < N)
        C[row * N + col] = sum;
}

/*
为什么Shared Memory优化有效？
- 无优化: 每个线程从Global Memory(HBM)读取2N个元素
- 有优化: 每个线程从HBM读取2N/TILE_SIZE个元素，其余从Shared Memory读取
- Shared Memory访问延迟~5个时钟周期 vs Global Memory ~400-600个时钟周期
- 减少了约TILE_SIZE倍的Global Memory访问
*/
```

---

## Week 6: 深度学习推理流程深入

---

### Day 1-2: 推理Pipeline与性能指标

#### 解码策略对比

| 策略 | 原理 | 输出特点 | 适用场景 |
|------|------|---------|---------|
| Greedy | 每步选概率最高的token | 确定性，可能不是全局最优 | 快速生成、代码补全 |
| Beam Search | 维护K个候选序列 | 质量较高，计算量大 | 翻译、摘要 |
| Top-K | 从概率最高的K个token中采样 | 随机但受控 | 创意写作 |
| Top-P (Nucleus) | 从累积概率达到P的最小集合中采样 | 自适应候选集 | 通用生成 |
| Temperature | 调整logits的分布 (logits/T) | T>1更随机，T<1更确定 | 与Top-K/P结合使用 |

#### LLM推理性能测量脚本

```python
"""
LLM推理性能测量工具
测量TTFT, TPOT, Throughput等核心指标
"""
import time
import statistics
import json
from dataclasses import dataclass, field, asdict
from typing import List, Optional
import requests

@dataclass
class InferenceMetrics:
    """单次推理的指标"""
    prompt_tokens: int = 0
    completion_tokens: int = 0
    ttft: float = 0.0            # Time To First Token (seconds)
    total_time: float = 0.0      # 总时间
    tpot: float = 0.0            # Time Per Output Token
    tokens_per_second: float = 0.0

@dataclass
class BenchmarkReport:
    """基准测试报告"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_time: float = 0.0
    avg_ttft: float = 0.0
    p50_ttft: float = 0.0
    p90_ttft: float = 0.0
    p99_ttft: float = 0.0
    avg_tpot: float = 0.0
    p50_tpot: float = 0.0
    p90_tpot: float = 0.0
    p99_tpot: float = 0.0
    throughput_tokens_per_sec: float = 0.0
    throughput_requests_per_sec: float = 0.0


class LLMBenchmark:
    """LLM推理性能基准测试"""

    def __init__(self, base_url: str, model: str = "default"):
        self.base_url = base_url.rstrip('/')
        self.model = model
        self.metrics: List[InferenceMetrics] = []

    def measure_streaming(self, prompt: str, max_tokens: int = 100,
                          temperature: float = 0.0) -> InferenceMetrics:
        """测量流式推理的TTFT和TPOT"""
        metrics = InferenceMetrics()

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": True,
        }

        start_time = time.perf_counter()
        first_token_time = None
        token_times = []
        token_count = 0

        try:
            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                stream=True,
                timeout=120
            )
            response.raise_for_status()

            for line in response.iter_lines():
                if not line:
                    continue
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]
                    if data_str.strip() == '[DONE]':
                        break
                    try:
                        data = json.loads(data_str)
                        delta = data['choices'][0].get('delta', {})
                        if 'content' in delta and delta['content']:
                            current_time = time.perf_counter()
                            if first_token_time is None:
                                first_token_time = current_time
                                metrics.ttft = first_token_time - start_time
                            token_times.append(current_time)
                            token_count += 1
                    except json.JSONDecodeError:
                        pass

            end_time = time.perf_counter()
            metrics.total_time = end_time - start_time
            metrics.completion_tokens = token_count

            if len(token_times) > 1:
                inter_token_times = [
                    token_times[i] - token_times[i-1]
                    for i in range(1, len(token_times))
                ]
                metrics.tpot = statistics.mean(inter_token_times)

            if token_count > 0:
                metrics.tokens_per_second = token_count / metrics.total_time

        except Exception as e:
            print(f"请求失败: {e}")

        self.metrics.append(metrics)
        return metrics

    def run_benchmark(self, prompts: List[str], max_tokens: int = 100,
                      warmup: int = 2) -> BenchmarkReport:
        """运行基准测试"""
        self.metrics = []

        # 预热
        print(f"预热 ({warmup} 次)...")
        for i in range(min(warmup, len(prompts))):
            self.measure_streaming(prompts[i % len(prompts)], max_tokens)
        self.metrics = []  # 清除预热数据

        # 正式测试
        print(f"正式测试 ({len(prompts)} 次)...")
        start = time.perf_counter()
        for i, prompt in enumerate(prompts):
            m = self.measure_streaming(prompt, max_tokens)
            print(f"  [{i+1}/{len(prompts)}] TTFT={m.ttft:.3f}s, "
                  f"TPOT={m.tpot*1000:.1f}ms, {m.tokens_per_second:.1f} tok/s")
        total_time = time.perf_counter() - start

        # 生成报告
        successful = [m for m in self.metrics if m.completion_tokens > 0]
        if not successful:
            return BenchmarkReport()

        ttfts = sorted([m.ttft for m in successful])
        tpots = sorted([m.tpot for m in successful if m.tpot > 0])
        total_tokens = sum(m.completion_tokens for m in successful)

        def percentile(data, p):
            idx = int(len(data) * p / 100)
            return data[min(idx, len(data)-1)]

        report = BenchmarkReport(
            total_requests=len(self.metrics),
            successful_requests=len(successful),
            failed_requests=len(self.metrics) - len(successful),
            total_time=total_time,
            avg_ttft=statistics.mean(ttfts),
            p50_ttft=percentile(ttfts, 50),
            p90_ttft=percentile(ttfts, 90),
            p99_ttft=percentile(ttfts, 99),
            avg_tpot=statistics.mean(tpots) if tpots else 0,
            p50_tpot=percentile(tpots, 50) if tpots else 0,
            p90_tpot=percentile(tpots, 90) if tpots else 0,
            p99_tpot=percentile(tpots, 99) if tpots else 0,
            throughput_tokens_per_sec=total_tokens / total_time,
            throughput_requests_per_sec=len(successful) / total_time,
        )

        return report

    @staticmethod
    def print_report(report: BenchmarkReport):
        print("\n" + "=" * 60)
        print("LLM推理性能基准测试报告")
        print("=" * 60)
        print(f"总请求数:      {report.total_requests}")
        print(f"成功请求:      {report.successful_requests}")
        print(f"失败请求:      {report.failed_requests}")
        print(f"总耗时:        {report.total_time:.2f}s")
        print(f"\n--- TTFT (Time To First Token) ---")
        print(f"  平均:  {report.avg_ttft*1000:.1f} ms")
        print(f"  P50:   {report.p50_ttft*1000:.1f} ms")
        print(f"  P90:   {report.p90_ttft*1000:.1f} ms")
        print(f"  P99:   {report.p99_ttft*1000:.1f} ms")
        print(f"\n--- TPOT (Time Per Output Token) ---")
        print(f"  平均:  {report.avg_tpot*1000:.1f} ms")
        print(f"  P50:   {report.p50_tpot*1000:.1f} ms")
        print(f"  P90:   {report.p90_tpot*1000:.1f} ms")
        print(f"  P99:   {report.p99_tpot*1000:.1f} ms")
        print(f"\n--- 吞吐量 ---")
        print(f"  Tokens/s:   {report.throughput_tokens_per_sec:.1f}")
        print(f"  Requests/s: {report.throughput_requests_per_sec:.2f}")
        print("=" * 60)


# 使用示例
if __name__ == "__main__":
    bench = LLMBenchmark("http://localhost:8000", model="Qwen/Qwen2-1.5B")
    prompts = [
        "What is deep learning?",
        "Explain the Transformer architecture.",
        "Write a Python function to sort a list.",
        "What is the difference between CPU and GPU?",
        "How does attention mechanism work?",
    ] * 2  # 10次测试

    report = bench.run_benchmark(prompts, max_tokens=100, warmup=2)
    bench.print_report(report)
```

#### FastAPI推理服务（OpenAI兼容）

```python
"""
LLM推理服务 - OpenAI兼容API
支持流式和非流式响应
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Union
import json
import time
import asyncio
import uvicorn

app = FastAPI(title="LLM Inference Service")

# ---- 数据模型 (OpenAI API兼容) ----
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "default"
    messages: List[ChatMessage]
    max_tokens: Optional[int] = 256
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 1.0
    stream: Optional[bool] = False
    stop: Optional[Union[str, List[str]]] = None

class ChatChoice(BaseModel):
    index: int = 0
    message: ChatMessage
    finish_reason: str = "stop"

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class ChatResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatChoice]
    usage: Usage

# ---- 模拟推理引擎 ----
class MockInferenceEngine:
    """模拟LLM推理引擎（实际项目中替换为vLLM/transformers等）"""
    async def generate(self, prompt: str, max_tokens: int,
                       temperature: float) -> str:
        # 模拟生成
        response = f"This is a simulated response to: {prompt[:50]}..."
        await asyncio.sleep(0.1)  # 模拟推理延迟
        return response

    async def generate_stream(self, prompt: str, max_tokens: int,
                              temperature: float):
        """流式生成"""
        words = f"This is a simulated streaming response to the query about {prompt[:30]}".split()
        for word in words[:max_tokens]:
            await asyncio.sleep(0.05)  # 模拟token生成延迟
            yield word + " "

engine = MockInferenceEngine()

# ---- API端点 ----
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/v1/models")
async def list_models():
    return {"data": [{"id": "default", "object": "model"}]}

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatRequest):
    prompt = request.messages[-1].content if request.messages else ""

    if request.stream:
        return StreamingResponse(
            stream_response(request, prompt),
            media_type="text/event-stream"
        )

    # 非流式响应
    response_text = await engine.generate(
        prompt, request.max_tokens, request.temperature
    )

    return ChatResponse(
        id=f"chatcmpl-{int(time.time())}",
        created=int(time.time()),
        model=request.model,
        choices=[ChatChoice(
            message=ChatMessage(role="assistant", content=response_text)
        )],
        usage=Usage(
            prompt_tokens=len(prompt.split()),
            completion_tokens=len(response_text.split()),
            total_tokens=len(prompt.split()) + len(response_text.split())
        )
    )

async def stream_response(request: ChatRequest, prompt: str):
    """SSE流式响应生成"""
    async for token in engine.generate_stream(
        prompt, request.max_tokens, request.temperature
    ):
        chunk = {
            "id": f"chatcmpl-{int(time.time())}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": request.model,
            "choices": [{"index": 0, "delta": {"content": token}, "finish_reason": None}]
        }
        yield f"data: {json.dumps(chunk)}\n\n"

    # 发送结束标记
    final = {
        "id": f"chatcmpl-{int(time.time())}",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": request.model,
        "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]
    }
    yield f"data: {json.dumps(final)}\n\n"
    yield "data: [DONE]\n\n"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

# 第三阶段: LLM推理引擎（Week 7-9）

---

## Week 7: vLLM深入

---

### Day 1-2: vLLM架构与PagedAttention

#### vLLM核心组件

```
                    用户请求
                       │
                 ┌─────▼──────┐
                 │  LLMEngine  │  ← 核心引擎，协调所有组件
                 └──────┬──────┘
                        │
           ┌────────────┼────────────┐
           │            │            │
     ┌─────▼─────┐ ┌───▼────┐ ┌────▼──────┐
     │ Scheduler  │ │ Worker │ │CacheEngine│
     │ (调度器)   │ │ (执行)  │ │ (缓存管理) │
     └─────┬─────┘ └───┬────┘ └────┬──────┘
           │            │            │
     ┌─────▼─────┐ ┌───▼─────┐ ┌───▼────────┐
     │BlockManager│ │ModelRunner│ │BlockAllocator│
     │(块管理器)  │ │(模型执行) │ │ (块分配器)   │
     └───────────┘ └─────────┘ └────────────┘
```

- **LLMEngine**: 顶层引擎，接收请求，调用Scheduler调度，调用Worker执行
- **Scheduler**: 决定哪些请求在当前迭代中被处理，管理Waiting/Running/Swapped队列
- **BlockManager**: 管理KV Cache的Block分配，维护Block Table
- **Worker**: 管理GPU设备，执行模型推理
- **ModelRunner**: 实际执行模型前向传播
- **CacheEngine**: 管理GPU/CPU之间的KV Cache交换

#### PagedAttention原理详解

```
传统KV Cache:
  请求A(长度100): [██████████████████████████        ] 预分配256空间, 浪费60%
  请求B(长度200): [████████████████████████████████████████████████        ] 预分配256
  请求C(长度50):  [████████████          ] 预分配256, 浪费80%
  → 内存碎片严重，利用率低

PagedAttention:
  物理Block池: [B0][B1][B2][B3][B4][B5][B6][B7][B8][B9]...

  请求A(100 tokens, block_size=16):
    Block Table: [B0, B3, B5, B7, B1, B9, B2] → 7个block, 最后一个block部分填充
    逻辑block 0 → 物理block B0
    逻辑block 1 → 物理block B3  (不需要连续!)
    ...

  请求B(200 tokens):
    Block Table: [B4, B6, B8, ...] → 使用不同的物理block

  → 按需分配，无碎片，利用率接近100%

Block共享（Prefix Caching）:
  请求1: "You are a helpful assistant. What is AI?"
  请求2: "You are a helpful assistant. Explain GPU."

  共同前缀 "You are a helpful assistant." 的KV Cache可以共享:
    请求1 Block Table: [B0*, B1*, B2, B3]  (* = 共享块)
    请求2 Block Table: [B0*, B1*, B5, B6]  (* = 同一物理块)
  → 节省显存，减少重复计算
```

#### vLLM基本使用

```python
# ---- vLLM离线推理 ----
from vllm import LLM, SamplingParams

# 加载模型
llm = LLM(
    model="Qwen/Qwen2-1.5B-Instruct",
    tensor_parallel_size=1,       # GPU数量
    gpu_memory_utilization=0.9,   # GPU显存使用比例
    max_model_len=2048,           # 最大序列长度
    dtype="auto",                 # 自动选择精度
)

# 设置采样参数
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=256,
    stop=["\n\n"],
)

# 批量推理
prompts = [
    "What is deep learning?",
    "Explain the Transformer architecture.",
    "What is the difference between training and inference?",
]

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated = output.outputs[0].text
    print(f"Prompt: {prompt[:50]}...")
    print(f"Output: {generated[:100]}...")
    print(f"Tokens: {len(output.outputs[0].token_ids)}")
    print()
```

```bash
# ---- vLLM在线服务 ----
# 启动OpenAI兼容API服务
vllm serve Qwen/Qwen2-1.5B-Instruct \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --max-num-seqs 64 \
    --port 8000

# 测试 (curl)
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "Qwen/Qwen2-1.5B-Instruct",
        "messages": [{"role": "user", "content": "What is AI?"}],
        "max_tokens": 100,
        "stream": false
    }'
```

**vLLM关键配置参数详解**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `tensor-parallel-size` | 1 | Tensor并行GPU数量，模型太大单卡放不下时使用 |
| `max-model-len` | 模型默认 | 最大序列长度(输入+输出)，越大显存越多 |
| `gpu-memory-utilization` | 0.9 | GPU显存使用比例，留一些给CUDA和系统 |
| `max-num-seqs` | 256 | 最大并发序列数，影响batch大小 |
| `dtype` | auto | 数据类型(float16/bfloat16/float32) |
| `quantization` | None | 量化方法(awq/gptq/squeezellm) |
| `enforce-eager` | False | 禁用CUDA Graph，调试时使用 |
| `enable-prefix-caching` | False | 启用前缀缓存 |

---

### Day 3: Continuous Batching详解

**Static Batching vs Continuous Batching**:

```
=== Static Batching (传统方式) ===

时间轴 →
请求A: [████████████████]              完成
请求B: [████████████████████████████]  完成
请求C: [████████]                      完成(但必须等B)

批次1结束 → 才能开始批次2
GPU利用率: 低(A和C完成后空等B)

=== Continuous Batching (vLLM方式) ===

时间轴 →
请求A: [████████]完成
请求B: [████████████████████████]完成
请求C: [████████████]完成
请求D:          [████████████████]完成   ← A完成后立即加入
请求E:              [██████████████]完成  ← C完成后立即加入

每次迭代(forward pass)后重新调度
GPU利用率: 高(几乎没有空闲)
```

| 特性 | Static Batching | Continuous Batching |
|------|----------------|-------------------|
| 调度粒度 | 批次级 | 迭代级(每次forward pass) |
| GPU利用率 | 低(短请求等长请求) | 高(动态填充空位) |
| 吞吐量 | 低 | 高(2-8x提升) |
| 新请求处理 | 等当前批次完成 | 随时加入 |
| 实现复杂度 | 简单 | 复杂(需要精细调度) |

#### vLLM调度器三队列

```
Waiting Queue: 等待被调度的请求
  → 有新请求时加入

Running Queue: 正在GPU上执行的请求
  → Scheduler选中后从Waiting移入
  → 完成后移出

Swapped Queue: 被抢占(preempted)的请求，KV Cache被交换到CPU
  → GPU显存不足时，低优先级请求从Running移入
  → 有空间时从Swapped恢复到Running

调度策略:
  FCFS: 先来先服务，按请求到达时间排序
  抢占: 当显存不足时:
    - Swap: 将KV Cache从GPU复制到CPU（保留计算结果）
    - Recompute: 丢弃KV Cache（重新计算，节省CPU内存）
```

---

### Day 5: vLLM性能测试

```python
# ---- vLLM功能测试套件 ----
import pytest
import requests
import json
import time
import asyncio
import aiohttp
from typing import List, Dict

BASE_URL = "http://localhost:8000"
MODEL = "Qwen/Qwen2-1.5B-Instruct"


class TestVLLMFunctional:
    """vLLM功能测试"""

    def test_health_check(self):
        """健康检查"""
        resp = requests.get(f"{BASE_URL}/health")
        assert resp.status_code == 200

    def test_list_models(self):
        """模型列表"""
        resp = requests.get(f"{BASE_URL}/v1/models")
        assert resp.status_code == 200
        data = resp.json()
        assert "data" in data
        assert len(data["data"]) > 0

    def test_basic_completion(self):
        """基本文本生成"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Say hello"}],
            "max_tokens": 50,
            "temperature": 0.0,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert "choices" in data
        assert len(data["choices"]) > 0
        assert data["choices"][0]["message"]["content"]
        assert data["usage"]["completion_tokens"] > 0

    def test_streaming(self):
        """流式输出"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Count from 1 to 5"}],
            "max_tokens": 100,
            "stream": True,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions",
                           json=payload, stream=True)
        assert resp.status_code == 200

        chunks = []
        for line in resp.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: ') and line != 'data: [DONE]':
                    chunks.append(json.loads(line[6:]))

        assert len(chunks) > 0
        # 验证最后一个chunk有finish_reason
        last_choice = chunks[-1]["choices"][0]
        assert last_choice.get("finish_reason") is not None or \
               last_choice.get("delta", {}).get("content") is not None

    @pytest.mark.parametrize("temperature", [0.0, 0.5, 1.0, 1.5])
    def test_temperature(self, temperature):
        """不同temperature测试"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": "What is 1+1?"}],
            "max_tokens": 50,
            "temperature": temperature,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        assert resp.status_code == 200

    @pytest.mark.parametrize("max_tokens", [1, 10, 50, 100, 256])
    def test_max_tokens(self, max_tokens):
        """不同max_tokens测试"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Write a story"}],
            "max_tokens": max_tokens,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        assert resp.status_code == 200
        # 验证输出token数不超过max_tokens
        assert resp.json()["usage"]["completion_tokens"] <= max_tokens + 5

    def test_empty_message(self):
        """空消息测试"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": ""}],
            "max_tokens": 50,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        # 应该返回200或400，取决于实现
        assert resp.status_code in [200, 400]

    def test_multi_turn_conversation(self):
        """多轮对话测试"""
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "My name is Alice."},
                {"role": "assistant", "content": "Hello Alice! Nice to meet you."},
                {"role": "user", "content": "What is my name?"},
            ],
            "max_tokens": 50,
            "temperature": 0.0,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        assert resp.status_code == 200
        content = resp.json()["choices"][0]["message"]["content"].lower()
        assert "alice" in content


class TestVLLMConcurrency:
    """并发测试"""

    def test_concurrent_requests(self):
        """并发请求测试"""
        async def send_request(session, i):
            payload = {
                "model": MODEL,
                "messages": [{"role": "user", "content": f"What is {i}+{i}?"}],
                "max_tokens": 20,
            }
            async with session.post(
                f"{BASE_URL}/v1/chat/completions",
                json=payload
            ) as resp:
                assert resp.status == 200
                return await resp.json()

        async def run_concurrent():
            async with aiohttp.ClientSession() as session:
                tasks = [send_request(session, i) for i in range(10)]
                results = await asyncio.gather(*tasks)
                return results

        results = asyncio.run(run_concurrent())
        assert len(results) == 10
        for r in results:
            assert r["choices"][0]["message"]["content"]


class TestVLLMEdgeCases:
    """边界条件测试"""

    def test_very_long_input(self):
        """超长输入测试"""
        long_text = "hello " * 1000
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": long_text}],
            "max_tokens": 10,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        # 可能返回200(截断)或400(超出限制)
        assert resp.status_code in [200, 400]

    def test_special_characters(self):
        """特殊字符测试"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Hello! @#$%^&*() 你好世界 🌍"}],
            "max_tokens": 50,
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        assert resp.status_code == 200

    def test_stop_sequence(self):
        """停止序列测试"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Count: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"}],
            "max_tokens": 100,
            "stop": [","],
        }
        resp = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload)
        assert resp.status_code == 200
```

---

## Week 8: TensorRT与TensorRT-LLM

### TensorRT优化技术详解

**Layer Fusion (算子融合)**:
```
融合前:
  Conv → Bias → ReLU  (3个kernel, 3次内存读写)

融合后:
  Conv+Bias+ReLU  (1个kernel, 1次内存读写)

收益: 减少kernel启动开销和内存带宽消耗
```

**vLLM vs TensorRT-LLM vs llama.cpp vs SGLang 详细对比**:

| 维度 | vLLM | TensorRT-LLM | llama.cpp | SGLang |
|------|------|-------------|-----------|--------|
| **性能** | 优秀 | 最佳(NVIDIA优化) | 中等(CPU也可) | 优秀 |
| **易用性** | pip install即用 | 需Build Engine | 编译即用 | pip install |
| **硬件** | NVIDIA GPU | NVIDIA GPU(深绑定) | CPU/GPU/Metal | NVIDIA GPU |
| **模型支持** | 广泛(社区快) | 需显式适配 | GGUF格式 | 广泛 |
| **量化** | AWQ/GPTQ/FP8 | FP8/INT8/INT4 | Q2-Q8各级 | AWQ/GPTQ/FP8 |
| **特色** | PagedAttention | Inflight Batching | CPU推理/边缘 | RadixAttention |
| **社区** | 活跃开源 | NVIDIA维护 | 活跃开源 | 研究导向 |
| **部署** | 简单 | 需Triton | 轻量 | 简单 |
| **场景** | 通用生产 | 极致性能 | 资源受限 | 结构化生成 |

---

## Week 9: 推理引擎进阶

### Tensor Parallelism vs Pipeline Parallelism

```
=== Tensor Parallelism (TP) ===
将单层的权重矩阵切分到多个GPU

GPU 0: [W的前半列] ─────┐
                         ├─→ All-Reduce → 完整输出
GPU 1: [W的后半列] ─────┘

特点: 
- 每层都需要GPU间通信(All-Reduce)
- 通信量: O(batch_size * hidden_size) 每层
- 适合: NVLink连接的同节点GPU(高带宽)

=== Pipeline Parallelism (PP) ===
将不同层分配到不同GPU

GPU 0: 层 1-16 ───→ GPU 1: 层 17-32

特点:
- 只在层边界通信(传递激活值)
- 有Pipeline Bubble(填充和排空阶段GPU空闲)
- 适合: 跨节点(通信少)
```

| 特性 | Tensor Parallelism | Pipeline Parallelism |
|------|-------------------|---------------------|
| 切分方式 | 权重矩阵切分(层内) | 层切分(层间) |
| 通信模式 | All-Reduce(每层) | 点对点(层边界) |
| 通信频率 | 高(每层都通信) | 低(只在层边界) |
| 带宽要求 | 高(需NVLink) | 低(PCIe即可) |
| 延迟影响 | 小(并行计算) | 大(流水线气泡) |
| 适合场景 | 同节点内GPU | 跨节点GPU |
| 典型配置 | 2/4/8路TP | 2/4路PP |
| 负载均衡 | 天然均衡 | 需要仔细分层 |

### 多引擎测试平台架构

```python
# ---- 适配器模式: 统一推理引擎接口 ----
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import time
import json
import requests

@dataclass
class InferenceRequest:
    """统一的推理请求"""
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.0
    top_p: float = 1.0
    stream: bool = False

@dataclass
class InferenceResponse:
    """统一的推理响应"""
    text: str
    prompt_tokens: int
    completion_tokens: int
    ttft: float = 0.0
    total_time: float = 0.0
    tokens_per_second: float = 0.0
    engine: str = ""

class EngineAdapter(ABC):
    """推理引擎适配器基类"""

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def generate(self, request: InferenceRequest) -> InferenceResponse:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass


class VLLMAdapter(EngineAdapter):
    """vLLM适配器"""

    def __init__(self, base_url: str = "http://localhost:8000",
                 model: str = "default"):
        self.base_url = base_url
        self.model = model

    def name(self) -> str:
        return "vLLM"

    def is_available(self) -> bool:
        try:
            resp = requests.get(f"{self.base_url}/health", timeout=5)
            return resp.status_code == 200
        except:
            return False

    def generate(self, request: InferenceRequest) -> InferenceResponse:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": request.prompt}],
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "top_p": request.top_p,
            "stream": False,
        }
        start = time.perf_counter()
        resp = requests.post(f"{self.base_url}/v1/chat/completions",
                           json=payload, timeout=120)
        total_time = time.perf_counter() - start
        resp.raise_for_status()
        data = resp.json()

        completion_tokens = data["usage"]["completion_tokens"]
        return InferenceResponse(
            text=data["choices"][0]["message"]["content"],
            prompt_tokens=data["usage"]["prompt_tokens"],
            completion_tokens=completion_tokens,
            total_time=total_time,
            tokens_per_second=completion_tokens / total_time if total_time > 0 else 0,
            engine="vLLM",
        )


class OpenAIAdapter(EngineAdapter):
    """通用OpenAI兼容API适配器"""

    def __init__(self, base_url: str, model: str, api_key: str = ""):
        self.base_url = base_url
        self.model = model
        self.api_key = api_key

    def name(self) -> str:
        return f"OpenAI-Compatible({self.base_url})"

    def is_available(self) -> bool:
        try:
            resp = requests.get(f"{self.base_url}/v1/models", timeout=5,
                              headers={"Authorization": f"Bearer {self.api_key}"})
            return resp.status_code == 200
        except:
            return False

    def generate(self, request: InferenceRequest) -> InferenceResponse:
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": request.prompt}],
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
        }
        start = time.perf_counter()
        resp = requests.post(f"{self.base_url}/v1/chat/completions",
                           json=payload, headers=headers, timeout=120)
        total_time = time.perf_counter() - start
        resp.raise_for_status()
        data = resp.json()
        ct = data["usage"]["completion_tokens"]
        return InferenceResponse(
            text=data["choices"][0]["message"]["content"],
            prompt_tokens=data["usage"]["prompt_tokens"],
            completion_tokens=ct,
            total_time=total_time,
            tokens_per_second=ct / total_time if total_time > 0 else 0,
            engine=self.name(),
        )


class EngineComparisonTest:
    """多引擎对比测试"""

    def __init__(self, engines: List[EngineAdapter]):
        self.engines = [e for e in engines if e.is_available()]
        print(f"可用引擎: {[e.name() for e in self.engines]}")

    def compare(self, prompts: List[str], max_tokens: int = 100) -> Dict:
        """对比多个引擎的性能"""
        results = {}
        for engine in self.engines:
            print(f"\n测试引擎: {engine.name()}")
            engine_results = []
            for i, prompt in enumerate(prompts):
                req = InferenceRequest(prompt=prompt, max_tokens=max_tokens)
                try:
                    resp = engine.generate(req)
                    engine_results.append(resp)
                    print(f"  [{i+1}/{len(prompts)}] {resp.tokens_per_second:.1f} tok/s")
                except Exception as e:
                    print(f"  [{i+1}/{len(prompts)}] 失败: {e}")
            results[engine.name()] = engine_results

        return results

    def print_comparison(self, results: Dict):
        """打印对比报告"""
        print("\n" + "=" * 70)
        print("多引擎性能对比报告")
        print("=" * 70)
        print(f"{'引擎':<20} {'平均延迟(s)':<15} {'平均tok/s':<15} {'成功率':<10}")
        print("-" * 60)
        for engine_name, responses in results.items():
            if responses:
                avg_time = sum(r.total_time for r in responses) / len(responses)
                avg_tps = sum(r.tokens_per_second for r in responses) / len(responses)
                print(f"{engine_name:<20} {avg_time:<15.3f} {avg_tps:<15.1f} "
                      f"{len(responses)}/{len(responses)}")
```

---

# 第四阶段: 推理优化技术（Week 10-12）

---

## Week 10: Attention优化

### FlashAttention原理详解

**核心问题**: 标准Attention需要实例化完整的 n×n 注意力矩阵，导致:
1. 内存 O(n^2) — 长序列时显存爆炸
2. 大量HBM读写 — GPU的计算速度远快于内存带宽

**FlashAttention解决方案: Tiling + IO-Awareness**

```
标准Attention的HBM访问:
  1. 从HBM读取Q, K → 计算S = QK^T → 写入HBM (n×n矩阵!)
  2. 从HBM读取S → 计算P = Softmax(S) → 写入HBM
  3. 从HBM读取P, V → 计算O = PV → 写入HBM
  总HBM访问: O(n^2 * d) 读 + O(n^2) 写

FlashAttention的Tiling策略:
  1. 将Q分成小块 Q_1, Q_2, ... (每块放入SRAM)
  2. 将K, V分成小块 K_1, K_2, ... (每块放入SRAM)
  3. 对每对(Q_i, K_j)在SRAM中计算局部Attention
  4. 使用Online Softmax合并局部结果
  5. 只写入最终输出O到HBM
  总HBM访问: O(n^2 * d^2 / SRAM_size) — 大幅减少!

关键技术 - Online Softmax:
  普通Softmax需要知道所有值才能计算（需要全局max和sum）
  Online Softmax可以分块计算:
    1. 对当前块计算局部max和局部sum
    2. 当处理下一块时, 更新全局max和sum
    3. 同时修正之前块的结果
  → 不需要存储完整的n×n矩阵!
```

**FlashAttention版本对比**:

| 版本 | 改进 | 加速 |
|------|------|------|
| v1 | Tiling + Online Softmax | 2-4x vs 标准 |
| v2 | 更好的并行性，减少非矩阵运算 | 2x vs v1 |
| v3 | Hopper架构异步特性，warp级调度 | 1.5-2x vs v2 (H100) |

```python
# FlashAttention vs 标准Attention对比测试
import torch
import time

def standard_attention(Q, K, V):
    """标准Attention实现"""
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    weights = torch.softmax(scores, dim=-1)
    return torch.matmul(weights, V)

def benchmark_attention(seq_len, d_model=128, num_heads=8, batch_size=4):
    """对比标准Attention和FlashAttention"""
    head_dim = d_model // num_heads
    Q = torch.randn(batch_size, num_heads, seq_len, head_dim, device='cuda', dtype=torch.float16)
    K = torch.randn(batch_size, num_heads, seq_len, head_dim, device='cuda', dtype=torch.float16)
    V = torch.randn(batch_size, num_heads, seq_len, head_dim, device='cuda', dtype=torch.float16)

    # 预热
    for _ in range(3):
        _ = standard_attention(Q, K, V)
    torch.cuda.synchronize()

    # 标准Attention
    torch.cuda.reset_peak_memory_stats()
    start = time.perf_counter()
    for _ in range(10):
        out_std = standard_attention(Q, K, V)
    torch.cuda.synchronize()
    std_time = (time.perf_counter() - start) / 10
    std_mem = torch.cuda.max_memory_allocated() / 1024**2

    # FlashAttention (通过scaled_dot_product_attention)
    torch.cuda.reset_peak_memory_stats()
    start = time.perf_counter()
    for _ in range(10):
        out_flash = torch.nn.functional.scaled_dot_product_attention(Q, K, V)
    torch.cuda.synchronize()
    flash_time = (time.perf_counter() - start) / 10
    flash_mem = torch.cuda.max_memory_allocated() / 1024**2

    print(f"  seq_len={seq_len}: Standard={std_time*1000:.1f}ms/{std_mem:.0f}MB "
          f"| Flash={flash_time*1000:.1f}ms/{flash_mem:.0f}MB "
          f"| 加速={std_time/flash_time:.1f}x")

# 不同序列长度测试
if torch.cuda.is_available():
    for seq_len in [512, 1024, 2048, 4096]:
        benchmark_attention(seq_len)
```

### MHA / GQA / MQA 对比

```
=== Multi-Head Attention (MHA) ===
Q: [h个头] K: [h个头] V: [h个头]
每个Q头有自己独立的K,V头
KV Cache大小: 2 * num_layers * h * d_head * seq_len

=== Multi-Query Attention (MQA) ===
Q: [h个头] K: [1个头] V: [1个头]
所有Q头共享同一组K,V
KV Cache大小: 2 * num_layers * 1 * d_head * seq_len
KV Cache缩小: h倍

=== Grouped-Query Attention (GQA) ===
Q: [h个头] K: [g个头] V: [g个头]  (h可以整除g)
每g/h个Q头共享一组K,V
KV Cache大小: 2 * num_layers * g * d_head * seq_len
KV Cache缩小: h/g倍
```

```python
def compare_kv_cache_sizes():
    """对比MHA, GQA, MQA的KV Cache大小"""
    configs = {
        "LLaMA-2-70B (GQA)": {"layers": 80, "q_heads": 64, "kv_heads": 8, "head_dim": 128},
        "如果用MHA":          {"layers": 80, "q_heads": 64, "kv_heads": 64, "head_dim": 128},
        "如果用MQA":          {"layers": 80, "q_heads": 64, "kv_heads": 1, "head_dim": 128},
    }

    seq_len = 4096
    dtype_bytes = 2  # FP16

    print(f"序列长度: {seq_len}, 精度: FP16")
    print(f"{'配置':<25} {'KV Heads':<10} {'KV Cache (MB)':<15} {'相对MHA':<10}")
    print("-" * 60)

    mha_size = None
    for name, cfg in configs.items():
        size_bytes = 2 * cfg["layers"] * cfg["kv_heads"] * cfg["head_dim"] * seq_len * dtype_bytes
        size_mb = size_bytes / (1024 ** 2)
        if mha_size is None and "MHA" in name:
            mha_size = size_mb
        elif mha_size is None:
            mha_size = size_mb  # GQA行作为参考

        ratio = size_mb / (mha_size if mha_size else size_mb)
        print(f"{name:<25} {cfg['kv_heads']:<10} {size_mb:<15.0f} {ratio:<10.2f}x")

compare_kv_cache_sizes()
# LLaMA-2-70B (GQA)      8         640            0.12x (相对MHA)
# 如果用MHA              64        5120           1.00x
# 如果用MQA               1          80            0.02x
```

**为什么GQA是主流**:
- MQA: KV Cache最小，但质量损失明显（太多Q头共享一个KV头）
- MHA: 质量最好，但KV Cache太大
- GQA: 平衡点 — KV Cache显著减小，质量损失极小
- LLaMA-2-70B, Mistral-7B, Qwen-2等均使用GQA

---

## Week 11: 量化技术

### 量化基础

```python
import numpy as np

def symmetric_quantize_int8(tensor: np.ndarray) -> tuple:
    """对称量化到INT8"""
    # scale = max(|tensor|) / 127
    abs_max = np.max(np.abs(tensor))
    scale = abs_max / 127.0

    # 量化: q = round(x / scale)
    quantized = np.round(tensor / scale).astype(np.int8)

    return quantized, scale

def dequantize_int8(quantized: np.ndarray, scale: float) -> np.ndarray:
    """反量化"""
    return quantized.astype(np.float32) * scale

def asymmetric_quantize_int8(tensor: np.ndarray) -> tuple:
    """非对称量化到INT8"""
    min_val = tensor.min()
    max_val = tensor.max()

    # scale = (max - min) / 255
    scale = (max_val - min_val) / 255.0
    # zero_point = round(-min / scale)
    zero_point = np.round(-min_val / scale).astype(np.int8)

    # 量化: q = round(x / scale) + zero_point
    quantized = np.round(tensor / scale + zero_point).astype(np.uint8)

    return quantized, scale, zero_point

# 对比不同量化粒度
def compare_quantization_granularity():
    """对比Per-Tensor vs Per-Channel量化精度"""
    # 模拟一个权重矩阵(不同通道有不同的值范围)
    np.random.seed(42)
    weight = np.random.randn(4, 8).astype(np.float32)
    weight[0] *= 10   # 第0行范围大
    weight[1] *= 0.1  # 第1行范围小

    # Per-Tensor量化 (整个矩阵用一个scale)
    q_tensor, scale_tensor = symmetric_quantize_int8(weight)
    dq_tensor = dequantize_int8(q_tensor, scale_tensor)
    error_tensor = np.mean((weight - dq_tensor) ** 2)

    # Per-Channel量化 (每行一个scale)
    q_channel = np.zeros_like(weight, dtype=np.int8)
    scales = np.zeros(weight.shape[0])
    for i in range(weight.shape[0]):
        q_channel[i], scales[i] = symmetric_quantize_int8(weight[i])
    dq_channel = np.zeros_like(weight)
    for i in range(weight.shape[0]):
        dq_channel[i] = dequantize_int8(q_channel[i], scales[i])
    error_channel = np.mean((weight - dq_channel) ** 2)

    print(f"Per-Tensor MSE: {error_tensor:.6f}")
    print(f"Per-Channel MSE: {error_channel:.6f}")
    print(f"Per-Channel精度提升: {error_tensor/error_channel:.1f}x")
    # Per-Channel精度明显更高，因为每个通道有独立的scale

compare_quantization_granularity()
```

### GPTQ vs AWQ对比

| 维度 | GPTQ | AWQ |
|------|------|-----|
| **原理** | Hessian矩阵指导的逐列量化 | 激活值感知的权重缩放 |
| **核心思想** | 量化一个权重后,用Hessian补偿其他权重 | 找到"重要通道",通过缩放而非保留来保护 |
| **校准数据** | 需要(128-256条) | 需要(较少依赖) |
| **量化速度** | 慢(需要求Hessian逆) | 快(无需复杂矩阵运算) |
| **精度保持** | 好 | 略好(尤其在低bit) |
| **泛化性** | 与校准数据相关 | 更好(激活感知更鲁棒) |
| **推理速度** | 快(INT4 kernel) | 快(INT4 kernel) |
| **工具** | AutoGPTQ | AutoAWQ |

### Speculative Decoding详解

```
=== Speculative Decoding流程 ===

Draft Model (小模型, 如1B): 快速猜测5个token
  输入: "The capital of France is"
  猜测: ["Paris", ",", " which", " is", " a"]

Target Model (大模型, 如70B): 一次forward pass验证5+1=6个位置
  位置0: P_target("Paris" | "The capital of France is") = 0.95  ✓ 接受
  位置1: P_target("," | "...France is Paris") = 0.80             ✓ 接受
  位置2: P_target("which" | "...is Paris,") = 0.60               ✓ 接受
  位置3: P_target("is" | "...Paris, which") = 0.70               ✓ 接受
  位置4: P_target("a" | "...which is") = 0.30                    ✗ 拒绝!
         重新从Target分布采样 → "known"
  位置5: 额外生成一个bonus token → "for"

结果: 一步生成了 "Paris, which is known for" (5个有效token!)
     传统方式需要5次forward pass才能生成5个token

=== 为什么无损? ===
接受/拒绝的概率设计保证:
  - 如果 P_draft(x) <= P_target(x): 以 P_target(x)/P_draft(x) 的概率接受
  - 否则: 接受后按 (P_target - P_draft) 重新采样
  → 最终token分布完全等同于直接从Target Model采样

=== 加速比分析 ===
设 acceptance rate = α (每个token被接受的概率)
理论加速比 ≈ 1 / (1 - α)

α = 0.5 → 加速2x
α = 0.7 → 加速3.3x
α = 0.9 → 加速10x

实际中 α 通常在 0.5-0.8，加速1.5-3x
```

---

## Week 12: 高级优化综合

### 推理优化技术全景图

```
┌─────────────────────────────────────────────────────────────┐
│                    LLM推理优化技术全景                        │
├─────────────┬─────────────┬─────────────┬──────────────────┤
│  模型级优化  │  算法级优化  │  系统级优化  │   硬件级优化      │
├─────────────┼─────────────┼─────────────┼──────────────────┤
│ 量化         │FlashAttention│Continuous  │ Tensor Core      │
│  GPTQ       │             │ Batching    │                  │
│  AWQ        │PagedAttention│             │ NVLink          │
│  FP8        │             │算子融合      │                  │
│  SmoothQuant│GQA/MQA      │(Kernel      │ HBM3            │
│             │             │ Fusion)     │                  │
│ 剪枝        │Speculative  │             │ 分布式           │
│  SparseGPT  │ Decoding    │CUDA Graph   │  TP              │
│  2:4 Sparse │             │             │  PP              │
│             │Prefix       │内存管理      │                  │
│ 蒸馏        │ Caching     │(PagedAttention)│                │
│             │             │             │                  │
│             │Sliding      │KV Cache压缩  │                  │
│             │ Window Attn │             │                  │
└─────────────┴─────────────┴─────────────┴──────────────────┘

组合策略:
低延迟场景: FlashAttention + FP8量化 + Speculative Decoding + CUDA Graph
高吞吐场景: Continuous Batching + PagedAttention + GQA + INT4量化
资源受限: INT4/GGUF量化 + llama.cpp + CPU推理
```

---

# 第五阶段: AI软件测试方法论与自动化（Week 13-14）

---

## Week 13: AI系统测试方法论

### AI系统 vs 传统软件测试

| 维度 | 传统软件测试 | AI系统测试 |
|------|------------|-----------|
| 确定性 | 相同输入→相同输出 | 可能有随机性(sampling) |
| 正确性 | 明确对错(断言) | 概率性正确(质量度量) |
| 测试oracle | 有明确预期结果 | 无明确预期(参考模型对比) |
| 覆盖率 | 代码覆盖率 | 代码覆盖率+场景覆盖 |
| 数据依赖 | 代码决定行为 | 模型+数据决定行为 |
| 精度测试 | 不适用 | 核心测试类型 |
| 性能维度 | 延迟/吞吐/CPU/内存 | +GPU利用率/显存/TTFT/TPOT |
| 回归测试 | 代码变更触发 | +模型变更/量化触发 |

### LLM推理功能测试用例设计

```python
# ---- 完整的LLM推理功能测试用例 ----
import pytest

# 测试类别1: 基本功能
BASIC_TESTS = [
    # (名称, 输入, 验证方法)
    ("空输入", "", "返回非空或错误"),
    ("简单问答", "What is 1+1?", "包含'2'"),
    ("长输入", "a " * 2000, "不崩溃"),
    ("Unicode", "你好世界 🌍", "正常返回"),
    ("代码生成", "Write a Python hello world", "包含'print'"),
    ("多语言", "Translate 'hello' to French", "包含'bonjour'"),
]

# 测试类别2: 采样参数
SAMPLING_TESTS = [
    {"temperature": 0.0, "expect": "确定性输出(多次相同)"},
    {"temperature": 0.5, "expect": "中等随机性"},
    {"temperature": 1.0, "expect": "高随机性"},
    {"temperature": 2.0, "expect": "非常随机或报错"},
    {"top_p": 0.1, "expect": "非常集中的输出"},
    {"top_p": 0.9, "expect": "较分散的输出"},
    {"top_k": 1, "expect": "等价于greedy"},
    {"top_k": 50, "expect": "正常采样"},
    {"max_tokens": 1, "expect": "只输出1个token"},
    {"max_tokens": 0, "expect": "错误或空输出"},
    {"max_tokens": 4096, "expect": "正常(受模型限制)"},
]

# 测试类别3: 边界条件
EDGE_CASE_TESTS = [
    "空字符串",
    "只有空格",
    "只有换行符",
    "非常长的输入(接近max_model_len)",
    "包含特殊token(<eos>, <pad>等)",
    "JSON/XML格式输入",
    "包含SQL注入尝试",
    "重复字符(aaaa...)",
    "混合语言(中英混合)",
]

# 测试类别4: 错误处理
ERROR_TESTS = [
    "无效的model名称",
    "temperature超出范围(负数, >2)",
    "无效的top_p(0, >1)",
    "请求body格式错误",
    "缺少必要字段",
    "并发发送大量请求(超过max_num_seqs)",
]
```

### 性能测试方案设计

```python
"""
LLM推理性能测试方案
"""
from dataclasses import dataclass
from typing import List
import asyncio
import aiohttp
import time
import json
import statistics
import numpy as np

@dataclass
class TestScenario:
    """测试场景定义"""
    name: str
    num_requests: int
    concurrency: int           # 并发数
    input_len: int             # 输入token数(约)
    output_len: int            # 期望输出token数
    duration_seconds: int = 0  # 持续时间(0=按请求数)

# 标准测试场景
SCENARIOS = [
    # 不同输入长度
    TestScenario("短输入", 50, 10, 128, 100),
    TestScenario("中等输入", 50, 10, 512, 100),
    TestScenario("长输入", 50, 10, 2048, 100),

    # 不同并发数
    TestScenario("低并发", 30, 1, 256, 100),
    TestScenario("中并发", 50, 10, 256, 100),
    TestScenario("高并发", 100, 50, 256, 100),
    TestScenario("极高并发", 200, 100, 256, 100),

    # 不同输出长度
    TestScenario("短输出", 50, 10, 256, 10),
    TestScenario("长输出", 50, 10, 256, 500),
]


class PerformanceTester:
    """性能测试执行器"""

    def __init__(self, base_url: str, model: str):
        self.base_url = base_url
        self.model = model

    def generate_prompt(self, target_tokens: int) -> str:
        """生成指定长度的prompt"""
        # 简单方法: 每个英文单词约1.3个token
        words_needed = int(target_tokens / 1.3)
        base = "Please provide a detailed explanation of the following topic. "
        return base + "word " * words_needed

    async def send_single_request(self, session, prompt, max_tokens):
        """发送单个请求并收集指标"""
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": 0.0,
            "stream": True,
        }

        metrics = {"ttft": 0, "total_time": 0, "tokens": 0, "success": False}
        start = time.perf_counter()
        first_token_time = None

        try:
            async with session.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload, timeout=aiohttp.ClientTimeout(total=300)
            ) as resp:
                if resp.status != 200:
                    return metrics

                async for line in resp.content:
                    line = line.decode('utf-8').strip()
                    if line.startswith('data: ') and line != 'data: [DONE]':
                        try:
                            data = json.loads(line[6:])
                            delta = data['choices'][0].get('delta', {})
                            if 'content' in delta and delta['content']:
                                if first_token_time is None:
                                    first_token_time = time.perf_counter()
                                    metrics["ttft"] = first_token_time - start
                                metrics["tokens"] += 1
                        except json.JSONDecodeError:
                            pass

            metrics["total_time"] = time.perf_counter() - start
            metrics["success"] = True
        except Exception as e:
            metrics["total_time"] = time.perf_counter() - start

        return metrics

    async def run_scenario(self, scenario: TestScenario):
        """执行单个测试场景"""
        print(f"\n{'='*50}")
        print(f"场景: {scenario.name}")
        print(f"  并发: {scenario.concurrency}, 请求数: {scenario.num_requests}")
        print(f"  输入~{scenario.input_len}tok, 输出~{scenario.output_len}tok")

        prompt = self.generate_prompt(scenario.input_len)
        all_metrics = []
        semaphore = asyncio.Semaphore(scenario.concurrency)

        async def bounded_request(session):
            async with semaphore:
                return await self.send_single_request(
                    session, prompt, scenario.output_len
                )

        start = time.perf_counter()
        async with aiohttp.ClientSession() as session:
            tasks = [bounded_request(session) for _ in range(scenario.num_requests)]
            all_metrics = await asyncio.gather(*tasks)
        wall_time = time.perf_counter() - start

        # 分析结果
        successful = [m for m in all_metrics if m["success"]]
        if not successful:
            print("  所有请求失败!")
            return

        ttfts = sorted([m["ttft"] for m in successful if m["ttft"] > 0])
        total_tokens = sum(m["tokens"] for m in successful)

        def pct(data, p):
            if not data: return 0
            return data[min(int(len(data) * p / 100), len(data) - 1)]

        print(f"  成功率: {len(successful)}/{len(all_metrics)}")
        print(f"  总耗时: {wall_time:.2f}s")
        print(f"  TTFT:  P50={pct(ttfts,50)*1000:.0f}ms  "
              f"P90={pct(ttfts,90)*1000:.0f}ms  P99={pct(ttfts,99)*1000:.0f}ms")
        print(f"  吞吐量: {total_tokens/wall_time:.1f} tokens/s, "
              f"{len(successful)/wall_time:.1f} req/s")

    def run_all_scenarios(self, scenarios: List[TestScenario] = None):
        """执行所有测试场景"""
        scenarios = scenarios or SCENARIOS
        for scenario in scenarios:
            asyncio.run(self.run_scenario(scenario))
```

### 稳定性测试

```python
"""GPU显存泄漏检测脚本"""
import subprocess
import time
import json
import requests
from datetime import datetime

def get_gpu_memory():
    """获取GPU显存使用情况"""
    result = subprocess.run(
        ['nvidia-smi', '--query-gpu=memory.used,memory.total,utilization.gpu',
         '--format=csv,nounits,noheader'],
        capture_output=True, text=True
    )
    values = result.stdout.strip().split(',')
    return {
        "used_mb": int(values[0].strip()),
        "total_mb": int(values[1].strip()),
        "gpu_util_pct": int(values[2].strip()),
    }

def memory_leak_detector(
    base_url: str,
    model: str,
    duration_hours: float = 1.0,
    interval_seconds: int = 30,
    request_batch_size: int = 5,
):
    """
    GPU显存泄漏检测
    持续发送请求并监控显存变化
    """
    print(f"开始显存泄漏检测 (持续{duration_hours}小时)")
    end_time = time.time() + duration_hours * 3600
    memory_samples = []

    # 初始显存
    initial_mem = get_gpu_memory()
    print(f"初始显存: {initial_mem['used_mb']}MB / {initial_mem['total_mb']}MB")

    while time.time() < end_time:
        # 发送一批请求
        for _ in range(request_batch_size):
            try:
                requests.post(f"{base_url}/v1/chat/completions", json={
                    "model": model,
                    "messages": [{"role": "user", "content": "Hello, what is AI?"}],
                    "max_tokens": 50,
                }, timeout=30)
            except:
                pass

        # 采集显存
        mem = get_gpu_memory()
        sample = {
            "timestamp": datetime.now().isoformat(),
            "used_mb": mem["used_mb"],
            "gpu_util_pct": mem["gpu_util_pct"],
            "delta_mb": mem["used_mb"] - initial_mem["used_mb"],
        }
        memory_samples.append(sample)
        print(f"[{sample['timestamp']}] 显存: {mem['used_mb']}MB "
              f"(+{sample['delta_mb']}MB), GPU: {mem['gpu_util_pct']}%")

        time.sleep(interval_seconds)

    # 分析
    deltas = [s["delta_mb"] for s in memory_samples]
    print(f"\n{'='*50}")
    print(f"显存泄漏分析:")
    print(f"  初始: {initial_mem['used_mb']}MB")
    print(f"  最终: {memory_samples[-1]['used_mb']}MB")
    print(f"  增长: {deltas[-1]}MB")
    print(f"  最大增长: {max(deltas)}MB")

    # 简单线性回归检测趋势
    if len(deltas) > 10:
        x = list(range(len(deltas)))
        slope = np.polyfit(x, deltas, 1)[0]
        if slope > 1.0:  # 每个采样周期增长超过1MB
            print(f"  ⚠ 可能存在显存泄漏! 增长斜率: {slope:.2f}MB/sample")
        else:
            print(f"  ✓ 显存稳定, 增长斜率: {slope:.2f}MB/sample")
```

---

## Week 14: 自动化测试框架实战

### 完整测试框架架构

```python
"""
AI推理引擎测试框架 - 核心架构
"""
# ---- framework/test_runner.py ----
import time
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, field, asdict
from pathlib import Path

@dataclass
class TestCase:
    """测试用例"""
    id: str
    name: str
    category: str           # functional/performance/accuracy/stability
    description: str = ""
    input_data: Dict = field(default_factory=dict)
    expected: Dict = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)

@dataclass
class TestResult:
    """测试结果"""
    test_id: str
    test_name: str
    status: str           # passed/failed/error/skipped
    duration: float = 0.0
    message: str = ""
    details: Dict = field(default_factory=dict)

class TestRunner:
    """测试执行器"""

    def __init__(self, engine_adapter, config: Dict = None):
        self.engine = engine_adapter
        self.config = config or {}
        self.results: List[TestResult] = []

    def run_test(self, test_case: TestCase) -> TestResult:
        """执行单个测试"""
        start = time.perf_counter()
        try:
            # 根据类别选择测试方法
            if test_case.category == "functional":
                result = self._run_functional_test(test_case)
            elif test_case.category == "performance":
                result = self._run_performance_test(test_case)
            elif test_case.category == "accuracy":
                result = self._run_accuracy_test(test_case)
            else:
                result = TestResult(
                    test_id=test_case.id,
                    test_name=test_case.name,
                    status="skipped",
                    message=f"未知测试类别: {test_case.category}"
                )
        except Exception as e:
            result = TestResult(
                test_id=test_case.id,
                test_name=test_case.name,
                status="error",
                message=str(e)
            )

        result.duration = time.perf_counter() - start
        self.results.append(result)
        return result

    def _run_functional_test(self, tc: TestCase) -> TestResult:
        """执行功能测试"""
        from framework.api_client import APIClient
        request = tc.input_data
        response = self.engine.generate(request)

        # 验证
        checks_passed = True
        messages = []

        if "min_tokens" in tc.expected:
            if response.completion_tokens < tc.expected["min_tokens"]:
                checks_passed = False
                messages.append(f"Token数不足: {response.completion_tokens} < {tc.expected['min_tokens']}")

        if "max_tokens" in tc.expected:
            if response.completion_tokens > tc.expected["max_tokens"]:
                checks_passed = False
                messages.append(f"Token数超限: {response.completion_tokens} > {tc.expected['max_tokens']}")

        if "contains" in tc.expected:
            for keyword in tc.expected["contains"]:
                if keyword.lower() not in response.text.lower():
                    checks_passed = False
                    messages.append(f"输出未包含: '{keyword}'")

        if "max_latency" in tc.expected:
            if response.total_time > tc.expected["max_latency"]:
                checks_passed = False
                messages.append(f"延迟超限: {response.total_time:.2f}s > {tc.expected['max_latency']}s")

        return TestResult(
            test_id=tc.id,
            test_name=tc.name,
            status="passed" if checks_passed else "failed",
            message="; ".join(messages) if messages else "All checks passed",
            details={"response_text": response.text[:200], "tokens": response.completion_tokens}
        )

    def _run_performance_test(self, tc: TestCase) -> TestResult:
        """执行性能测试"""
        # 简化版性能测试
        iterations = tc.input_data.get("iterations", 10)
        times = []
        for _ in range(iterations):
            resp = self.engine.generate(tc.input_data.get("request", {}))
            times.append(resp.total_time)

        times.sort()
        p50 = times[len(times)//2]
        p99 = times[int(len(times)*0.99)]

        passed = True
        if "p50_threshold" in tc.expected and p50 > tc.expected["p50_threshold"]:
            passed = False
        if "p99_threshold" in tc.expected and p99 > tc.expected["p99_threshold"]:
            passed = False

        return TestResult(
            test_id=tc.id, test_name=tc.name,
            status="passed" if passed else "failed",
            details={"p50": p50, "p99": p99, "mean": sum(times)/len(times)}
        )

    def _run_accuracy_test(self, tc: TestCase) -> TestResult:
        """执行精度测试"""
        # 对比参考输出
        resp = self.engine.generate(tc.input_data.get("request", {}))
        reference = tc.expected.get("reference_output", "")

        # 简单的字符串相似度
        from difflib import SequenceMatcher
        similarity = SequenceMatcher(None, resp.text, reference).ratio()
        threshold = tc.expected.get("similarity_threshold", 0.8)

        return TestResult(
            test_id=tc.id, test_name=tc.name,
            status="passed" if similarity >= threshold else "failed",
            details={"similarity": similarity, "threshold": threshold}
        )

    def generate_report(self, output_path: str = "test_report.json"):
        """生成测试报告"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.status == "passed")
        failed = sum(1 for r in self.results if r.status == "failed")
        errors = sum(1 for r in self.results if r.status == "error")

        report = {
            "summary": {
                "total": total,
                "passed": passed,
                "failed": failed,
                "errors": errors,
                "pass_rate": f"{passed/total*100:.1f}%" if total > 0 else "N/A",
                "total_duration": sum(r.duration for r in self.results),
            },
            "results": [asdict(r) for r in self.results],
        }

        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"\n测试报告: {output_path}")
        print(f"  总计: {total}, 通过: {passed}, 失败: {failed}, 错误: {errors}")
        print(f"  通过率: {report['summary']['pass_rate']}")

        return report
```

---

# 第六阶段: 综合实战 + 面试准备（Week 15-16）

---

## 面试题库（含详细答案）

### 一、Python编程

**Q1: Python的GIL是什么？对多线程有什么影响？**

GIL (Global Interpreter Lock) 是CPython解释器中的一个互斥锁，确保同一时刻只有一个线程执行Python字节码。

| 影响 | 说明 |
|------|------|
| CPU密集型多线程 | 无法利用多核，甚至因为锁竞争更慢 |
| IO密集型多线程 | 有效，线程等待IO时释放GIL |
| 多进程 | 不受GIL影响，每个进程有独立的GIL |
| C扩展 | 可以手动释放GIL实现真正并行 |

解决方案:
- CPU密集型 → `multiprocessing` 或 C扩展 (NumPy/Cython)
- IO密集型 → `threading` 或 `asyncio`
- Python 3.13+ 实验性的 free-threaded mode (无GIL)

**Q2: pytest中fixture的scope有哪些？**

| Scope | 生命周期 | 典型用途 |
|-------|---------|---------|
| `function` (默认) | 每个测试函数 | 独立状态 |
| `class` | 每个测试类 | 类内共享setup |
| `module` | 每个.py文件 | DB连接等 |
| `package` | 每个测试包 | 包级资源 |
| `session` | 整个测试会话 | 全局资源(服务启动) |

---

### 二、GPU与CUDA

**Q3: GPU和CPU架构的主要区别？为什么GPU适合深度学习？**

CPU: 少量强核心(4-128)，复杂控制逻辑，大缓存，优化单线程延迟
GPU: 大量弱核心(数千)，简单控制，小缓存，高带宽，优化并行吞吐

GPU适合深度学习因为:
1. 矩阵运算是高度并行的(SIMD)
2. Tensor Core专门优化矩阵乘加
3. HBM提供TB/s级别带宽
4. 深度学习的计算模式适合GPU的SIMT架构

**Q4: 什么是Warp？Warp Divergence是什么？**

Warp: GPU最小调度单位，32个线程，执行相同指令(SIMT)

Warp Divergence: Warp内线程遇到条件分支走不同路径时，GPU必须串行执行两个分支，未执行分支的线程空闲等待。

优化: 让同一Warp内线程尽量走相同分支路径。

**Q5: Tensor Core vs CUDA Core？**

| 特性 | CUDA Core | Tensor Core |
|------|-----------|-------------|
| 运算 | 标量(a*b+c) | 矩阵(D=A*B+C, 4x4) |
| 每周期 | 1 FMA | 64+ FMA |
| 精度 | FP32/FP64 | FP16/BF16/TF32/FP8/INT8 |
| 加速 | 基线 | 矩阵运算8-16x |
| 用途 | 通用计算 | GEMM、深度学习 |

---

### 三、LLM推理基础

**Q6: 解释Prefill和Decode阶段**

| 维度 | Prefill | Decode |
|------|---------|--------|
| 处理内容 | 整个输入prompt | 每次1个新token |
| 计算模式 | 并行处理所有token | 串行自回归生成 |
| 瓶颈 | Compute-bound(大矩阵乘) | Memory-bound(读KV Cache) |
| GPU利用率 | 高 | 低(计算量小) |
| 决定指标 | TTFT | TPOT |
| KV Cache | 生成并存储 | 读取并追加 |

Decode为什么是Memory-bound:
- 每步只计算1个token的QKV，计算量极小
- 但需要读取整个KV Cache做Attention
- GPU算力远超所需计算量，瓶颈在内存带宽

**Q7: 什么是KV Cache？为什么需要它？**

KV Cache缓存Attention层中已计算的Key和Value张量。

不用Cache: 生成第n个token需重新计算前n-1个token的K/V → O(n^2)总计算量
用Cache: 只计算新token的K/V，追加到缓存 → O(n)总计算量

KV Cache大小公式:
```
KV Cache = 2 * layers * kv_heads * head_dim * seq_len * batch * bytes
```

7B模型(FP16, 2048 tokens) ≈ 1GB/序列

**Q8: TTFT、TPOT和Throughput**

| 指标 | 含义 | 影响因素 | 优化方向 |
|------|------|---------|---------|
| TTFT | 首token延迟 | 输入长度、模型大小、Prefill效率 | Chunked Prefill、更快的Prefill |
| TPOT | 每token生成时间 | KV Cache大小、内存带宽 | 量化、GQA、更高带宽GPU |
| Throughput | 系统tokens/s | 批处理效率、GPU利用率 | Continuous Batching、更大batch |

---

### 四、推理引擎

**Q9: PagedAttention的原理**

传统问题: KV Cache预分配连续内存 → 碎片化(~60-80%浪费)

PagedAttention方案:
1. KV Cache分为固定大小Block(类似OS内存页)
2. Block Table(类似页表)维护逻辑→物理映射
3. 物理Block不需要连续，按需分配/释放
4. 支持Block共享(Prefix Caching)

效果: 内存利用率从20-40%提升到接近100%

**Q10: Continuous Batching vs Static Batching**

Static: 批次级调度，短请求等长请求，GPU空闲
Continuous: 迭代级调度，完成即替换，GPU利用率高

Continuous Batching带来2-8x吞吐量提升。

**Q11: vLLM vs TensorRT-LLM如何选择？**

快速原型/研究 → vLLM (简单易用)
生产极致性能 → TensorRT-LLM (NVIDIA深度优化)
需要最新模型 → vLLM (社区更新快)
非NVIDIA硬件 → 其他框架

---

### 五、推理优化

**Q12: FlashAttention原理**

核心: IO-Aware的分块(Tiling)计算

标准Attention需要实例化n*n矩阵(O(n^2)内存)并多次读写HBM。
FlashAttention将Q/K/V分成小块加载到SRAM，在SRAM中计算局部Attention，用Online Softmax合并结果，只写最终输出到HBM。

结果: O(n)内存，2-4x速度提升，精确计算(非近似)。

**Q13: AWQ vs GPTQ**

| 维度 | GPTQ | AWQ |
|------|------|-----|
| 原理 | Hessian矩阵逐列量化+误差补偿 | 激活感知权重缩放保护重要通道 |
| 速度 | 慢 | 快 |
| 精度 | 好 | 略好(低bit更明显) |
| 泛化 | 依赖校准数据 | 更鲁棒 |

**Q14: Speculative Decoding**

小Draft Model快速猜测多个token → 大Target Model一次forward pass并行验证 → 接受/拒绝

为什么无损: 数学证明最终分布等同于直接用Target Model采样
加速比: 1/(1-acceptance_rate)，通常1.5-3x

**Q15: Tensor Parallelism vs Pipeline Parallelism**

| 特性 | TP | PP |
|------|----|----|
| 切分 | 权重矩阵(层内) | 层(层间) |
| 通信 | All-Reduce(每层) | 点对点(层边界) |
| 频率 | 高 | 低 |
| 带宽要求 | NVLink | PCIe可 |
| 场景 | 节点内 | 跨节点 |

---

### 六、测试与QA

**Q16: 如何测试LLM推理引擎的正确性？**

分层测试:
1. **算子级**: 对比PyTorch原始输出，数值精度验证
2. **模型级**: 对比HuggingFace输出，Perplexity评估
3. **API级**: OpenAI兼容性，参数功能，流式正确性
4. **系统级**: 并发正确性，长时间运行正确性

非确定性处理: 固定种子验证一致性，或统计方法验证分布

**Q17: 如何设计LLM推理性能测试方案？**

1. 定义指标和SLA (TTFT P99 < 500ms等)
2. 设计场景 (不同输入长度/并发/请求模式)
3. 准备数据 (ShareGPT或合成数据)
4. 执行测试 (充分预热30s+，每场景5min+)
5. 分析结果 (P50/P90/P99延迟，吞吐量曲线，GPU利用率)

**Q18: 如何测试量化模型的精度？**

1. Perplexity: WikiText-2/C4数据集，对比原始vs量化模型
2. 任务级: MMLU/HumanEval/GSM8K等基准测试
3. 输出对比: ROUGE/BLEU分数
4. 人工评估: 采样评估关键任务

**Q19: AI测试 vs 传统测试**

| 维度 | 传统 | AI |
|------|------|-----|
| 确定性 | 确定 | 可能随机 |
| 正确性 | 明确对错 | 概率性 |
| Oracle | 有预期结果 | 参考模型对比 |
| 性能指标 | 延迟/吞吐 | +GPU/显存/TTFT/TPOT |
| 回归 | 代码变更 | +模型变更/量化 |

**Q20: 从零搭建LLM推理测试体系**

1. 需求分析(1周): 明确架构、SLA、范围
2. 策略制定(1周): 分层策略、工具选型
3. 基础设施(2周): GPU环境、CI/CD、监控
4. 测试开发(4周): 功能/性能/精度/稳定性测试
5. 持续优化: CI集成、回归测试、覆盖率提升

---

### 七、Linux与工程

**Q21: 推理服务性能问题排查**

```bash
# 1. 检查GPU状态
nvidia-smi                    # GPU利用率/显存
nvidia-smi dmon -s u          # 持续监控

# 2. 检查系统资源
top -p <pid>                  # CPU使用
free -h                       # 系统内存
iostat -x 1                   # 磁盘IO

# 3. 应用级检查
curl localhost:8000/metrics   # Prometheus指标
grep ERROR /var/log/app.log   # 错误日志

# 4. 定位瓶颈
# GPU利用率低 → batch太小/数据传输瓶颈
# GPU利用率高但吞吐低 → 计算效率问题
# 显存不足 → KV Cache配置/模型太大
# CPU瓶颈 → Tokenization/预处理
```

---

## 核心概念速查表

| 概念 | 一句话解释 |
|------|-----------|
| KV Cache | 缓存已计算的Key/Value，避免自回归解码时重复计算 |
| PagedAttention | 将KV Cache分页管理，解决内存碎片和浪费问题 |
| FlashAttention | IO感知的分块Attention计算，减少HBM读写 |
| Continuous Batching | 迭代级调度，请求完成即刻替换，提高GPU利用率 |
| Speculative Decoding | 小模型猜测+大模型验证，将串行变并行 |
| GPTQ | 基于Hessian矩阵的逐层权重量化方法 |
| AWQ | 根据激活值重要性，通过缩放保护关键权重通道 |
| Tensor Parallelism | 将权重矩阵切分到多GPU，适合节点内 |
| Pipeline Parallelism | 将不同层分配到不同GPU，适合跨节点 |
| GQA | 介于MHA和MQA之间，多个Query Head共享一组KV Head |
| TTFT | 首token延迟，反映Prefill性能 |
| TPOT | 每token生成时间，反映Decode性能 |
| Prefill | 并行处理输入prompt的阶段，计算密集型 |
| Decode | 逐token生成的阶段，内存密集型 |
| Tensor Core | GPU专用矩阵运算单元，比CUDA Core快数倍 |
| Roofline Model | 用算术强度判断性能瓶颈是计算还是内存 |
| Warp | GPU最小调度单位，32个线程执行相同指令 |
| Online Softmax | 分块计算Softmax的算法，FlashAttention的关键 |
| Prefix Caching | 相同前缀的请求共享KV Cache，减少重复计算 |
| 2:4 Sparsity | NVIDIA Ampere支持的结构化稀疏，4个权重中保留2个 |

---

## 学习资源汇总

### 必读论文
1. "Attention Is All You Need" — Transformer架构
2. "Efficient Memory Management for LLM Serving with PagedAttention" — vLLM
3. "FlashAttention: Fast and Memory-Efficient Exact Attention" — FlashAttention
4. "Fast Inference from Transformers via Speculative Decoding" — Speculative Decoding
5. "GPTQ: Accurate Post-Training Quantization" — GPTQ量化
6. "AWQ: Activation-aware Weight Quantization" — AWQ量化
7. "Orca: A Distributed Serving System" — Continuous Batching
8. "GQA: Training Generalized Multi-Query Transformer Models" — GQA

### 推荐书籍
- 《Fluent Python》— Python进阶
- 《C++ Primer》— C++基础
- 《Programming Massively Parallel Processors》— CUDA编程
- 《Python Testing with pytest》— 测试

### 在线课程
- 吴恩达 ML/DL Specialization (Coursera)
- NVIDIA Deep Learning Institute
- Hugging Face NLP Course
- FastAI Course

### 重要GitHub仓库
- vLLM: https://github.com/vllm-project/vllm
- TensorRT-LLM: https://github.com/NVIDIA/TensorRT-LLM
- llama.cpp: https://github.com/ggerganov/llama.cpp
- SGLang: https://github.com/sgl-project/sglang

### 技术博客
- Jay Alammar's Blog (Transformer可视化)
- Lil'Log (ML概念讲解)
- NVIDIA Developer Blog
- vLLM Blog

---

## 每周学习时间总结

| 周次 | 工作日(h/天) | 周末(h/天) | 周总计(h) |
|------|------------|-----------|----------|
| Week 1-12 | 2.5 | 5 | 22.5 |
| Week 13-14 | 2.5 | 5 | 22.5 |
| Week 15-16 | 3 | 5 | 25 |
| **总计** | | | **~370小时** |

---

> **核心优先级**:
> 1. **最高**: LLM推理基础(KV Cache, Prefill/Decode) + vLLM(PagedAttention, Continuous Batching) + 推理优化(FlashAttention, 量化, Speculative Decoding)
> 2. **高**: Python进阶 + GPU/CUDA基础 + 测试方法论
> 3. **中**: C/C++ + TensorRT-LLM + 分布式推理
> 4. **加分**: 完整项目作品 + CUDA编程实战