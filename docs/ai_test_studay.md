# AI/Deep Learning QA Engineer 16周学习计划

> **目标岗位**: AI/Deep Learning Software QA Engineer
> **当前背景**: 1年Java测试开发经验、2年Python经验、4年Linux经验
> **学习周期**: 16周（约4个月）
> **每日学习时间建议**: 工作日 2-3小时，周末 4-6小时

---

## 总体学习路线图

| 阶段 | 周数 | 主题 | 目标 |
|------|------|------|------|
| 第一阶段 | Week 1-3 | Python进阶 + C/C++基础 | 编程能力达标 |
| 第二阶段 | Week 4-6 | 深度学习基础 + GPU/CUDA基础 | 建立AI理论基础 |
| 第三阶段 | Week 7-9 | LLM推理引擎(vLLM/TensorRT) | 掌握核心工具 |
| 第四阶段 | Week 10-12 | 推理优化技术 | 掌握优化原理与实践 |
| 第五阶段 | Week 13-14 | AI软件测试方法论与自动化 | 测试能力提升 |
| 第六阶段 | Week 15-16 | 综合实战 + 面试准备 | 查漏补缺、面试冲刺 |

---

## 第一阶段: Python进阶 + C/C++基础（Week 1-3）

### Week 1: Python进阶（每天2.5小时）

#### Day 1（周一）：Python高级数据结构与性能优化（2.5h）
- **知识点**:
  - `collections` 模块: `defaultdict`, `Counter`, `deque`, `namedtuple`
  - 生成器(generator)与迭代器(iterator)深入理解
  - 列表推导式 vs 生成器表达式的内存差异
- **学习资源**:
  - 《Fluent Python》第2-4章
  - Real Python: https://realpython.com/python-generators/
- **练习**:
  - 用生成器实现一个大文件逐行读取并统计词频的工具
  - 对比 `list` vs `generator` 处理100万条数据的内存占用（用 `sys.getsizeof` 和 `memory_profiler`）
- **重点掌握**: 生成器的惰性求值机制，`yield` vs `return`

#### Day 2（周二）：Python装饰器与上下文管理器（2.5h）
- **知识点**:
  - 装饰器原理（闭包 -> 装饰器 -> 带参装饰器）
  - `functools.wraps` 的作用
  - `contextmanager` 装饰器与 `__enter__`/`__exit__`
  - 类装饰器
- **学习资源**:
  - 《Fluent Python》第7、9章
  - Real Python Decorators: https://realpython.com/primer-on-python-decorators/
- **练习**:
  - 实现一个 `@timer` 装饰器，记录函数执行时间
  - 实现一个 `@retry(max_retries=3)` 带参数的装饰器
  - 用 `contextmanager` 实现一个数据库连接管理器
- **重点掌握**: 装饰器的本质是高阶函数，闭包的变量捕获

#### Day 3（周三）：Python并发编程（2.5h）
- **知识点**:
  - GIL（全局解释器锁）的原理与影响
  - `threading` vs `multiprocessing` vs `asyncio` 的适用场景
  - `concurrent.futures` 模块: `ThreadPoolExecutor`, `ProcessPoolExecutor`
  - `asyncio` 基础: `async/await`, `event loop`
- **学习资源**:
  - 《Fluent Python》第19-21章
  - Python官方文档 asyncio 部分
- **练习**:
  - 用 `ThreadPoolExecutor` 实现并发下载10个网页
  - 用 `multiprocessing` 实现CPU密集型任务（如计算大量素数）的并行化
  - 用 `asyncio` 实现异步HTTP请求
- **重点掌握**: GIL对多线程的限制，IO密集型用线程/协程，CPU密集型用多进程

#### Day 4（周四）：Python类型注解与单元测试（2.5h）
- **知识点**:
  - Type Hints: `typing` 模块, `Optional`, `Union`, `List`, `Dict`, `TypeVar`
  - `pytest` 框架: fixtures, parametrize, markers, conftest.py
  - `pytest-cov` 覆盖率统计
  - `unittest.mock`: `Mock`, `patch`, `MagicMock`
- **学习资源**:
  - pytest官方文档: https://docs.pytest.org/
  - 《Python Testing with pytest》
- **练习**:
  - 为一个简单的计算器类编写完整的pytest测试用例（包含参数化测试）
  - 使用 `mock.patch` 模拟外部API调用的测试
  - 达到90%以上代码覆盖率
- **重点掌握**: pytest fixture的scope, parametrize的用法, mock的使用场景

#### Day 5（周五）：Python包管理与项目工程化（2.5h）
- **知识点**:
  - `pip`, `venv`, `conda` 环境管理
  - `setup.py` / `pyproject.toml` 项目配置
  - `logging` 模块配置与最佳实践
  - 代码质量工具: `pylint`, `flake8`, `black`, `mypy`
- **学习资源**:
  - Python Packaging User Guide: https://packaging.python.org/
  - Real Python Logging: https://realpython.com/python-logging/
- **练习**:
  - 创建一个完整的Python项目结构，包含 `pyproject.toml`, 测试目录, CI配置
  - 配置 `logging` 实现分级日志输出（console + file）
  - 用 `mypy` 对代码进行类型检查
- **重点掌握**: 虚拟环境隔离，日志分级（DEBUG/INFO/WARNING/ERROR/CRITICAL）

#### Day 6-7（周末）：NumPy与性能分析（每天5h）
- **知识点**:
  - NumPy 数组操作: 创建、索引、切片、广播(broadcasting)
  - NumPy 向量化运算 vs Python循环的性能差异
  - `cProfile`, `line_profiler`, `memory_profiler` 性能分析工具
  - Python调用C扩展(`ctypes`, `cffi`)初步了解
- **学习资源**:
  - NumPy官方教程: https://numpy.org/doc/stable/user/quickstart.html
  - 《Python High Performance》相关章节
- **练习**:
  - 实现矩阵乘法的三种方式（纯Python循环、NumPy、NumPy优化），对比性能
  - 用 `cProfile` 分析一段代码的性能瓶颈并优化
  - 用NumPy实现一个简单的图像处理程序（灰度转换、模糊滤波）
- **重点掌握**: NumPy广播机制，向量化思维，性能分析工具链

---

### Week 2: C/C++基础（每天2.5小时）

#### Day 1（周一）：C语言基础（2.5h）
- **知识点**:
  - 数据类型、变量、运算符
  - 控制流: `if/else`, `for`, `while`, `switch`
  - 函数定义与调用
  - 编译过程: 预处理 -> 编译 -> 汇编 -> 链接
  - `gcc` 编译器基本使用: `-o`, `-g`, `-O2`, `-Wall`
- **学习资源**:
  - 《C Primer Plus》第1-6章（快速浏览，有编程基础）
  - CS50 C语言部分: https://cs50.harvard.edu/x/
- **练习**:
  - 在Linux下用gcc编译运行Hello World
  - 实现冒泡排序、二分查找
  - 编译时分别使用 `-O0` 和 `-O2`，对比执行速度
- **重点掌握**: 编译流程，gcc常用选项

#### Day 2（周二）：指针与内存管理（2.5h）
- **知识点**:
  - 指针基础: 定义、取地址(&)、解引用(*)
  - 指针与数组的关系
  - 动态内存分配: `malloc`, `calloc`, `realloc`, `free`
  - 内存泄漏、野指针、悬空指针
  - `valgrind` 内存检查工具
- **学习资源**:
  - 《C Primer Plus》第10-12章
  - Valgrind Quick Start: https://valgrind.org/docs/manual/quick-start.html
- **练习**:
  - 实现一个动态数组（可自动扩容）
  - 故意制造内存泄漏，用 `valgrind` 检测并修复
  - 实现一个简单的链表（插入、删除、遍历）
- **重点掌握**: 指针的本质是地址，malloc/free配对使用，valgrind的使用

#### Day 3（周三）：C语言文件操作与预处理器（2.5h）
- **知识点**:
  - 文件I/O: `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`
  - 预处理器: `#define`, `#include`, `#ifdef`, `#ifndef`
  - 头文件保护（include guard）
  - 多文件编译与Makefile基础
- **学习资源**:
  - 《C Primer Plus》第13-16章
  - GNU Make Manual: https://www.gnu.org/software/make/manual/
- **练习**:
  - 实现一个文件复制程序
  - 编写一个多文件C项目（main.c + utils.c + utils.h），用Makefile编译
  - 用宏定义实现一个简单的日志系统（带文件名、行号）
- **重点掌握**: 多文件项目组织，Makefile基本语法

#### Day 4（周四）：C++基础 - 面向对象（2.5h）
- **知识点**:
  - C++与C的区别
  - 类与对象: 构造函数、析构函数、成员函数
  - 访问控制: `public`, `private`, `protected`
  - 继承与多态: 虚函数、纯虚函数
  - `std::string`, `std::vector` 基本使用
- **学习资源**:
  - 《C++ Primer》第1-7章（快速浏览）
  - LearnCpp: https://www.learncpp.com/
- **练习**:
  - 用C++实现一个Shape基类，派生Circle和Rectangle，用虚函数实现多态
  - 使用 `std::vector` 和 `std::string` 重写之前的排序程序
- **重点掌握**: 构造/析构函数调用时机，虚函数表(vtable)原理

#### Day 5（周五）：C++模板与STL（2.5h）
- **知识点**:
  - 函数模板与类模板
  - STL容器: `vector`, `map`, `unordered_map`, `set`, `queue`, `stack`
  - STL算法: `sort`, `find`, `transform`, `accumulate`
  - 迭代器(iterator)
  - 智能指针: `unique_ptr`, `shared_ptr`, `weak_ptr`
- **学习资源**:
  - 《C++ Primer》第9-11章、第16章
  - CPP Reference: https://en.cppreference.com/
- **练习**:
  - 实现一个模板函数 `findMax<T>`
  - 用STL容器和算法实现一个简单的学生成绩管理系统
  - 用智能指针重构之前的链表实现，消除手动内存管理
- **重点掌握**: 常用STL容器的时间复杂度，智能指针的使用场景

#### Day 6-7（周末）：C/C++与Python交互 + 编译调试（每天5h）
- **知识点**:
  - `gdb` 调试器使用: 断点、单步、打印变量、调用栈
  - `ctypes` 调用C库
  - `pybind11` 创建Python C++扩展
  - CMake基础
  - `AddressSanitizer` (ASan) 的使用
- **学习资源**:
  - GDB Tutorial: https://sourceware.org/gdb/current/onlinedocs/gdb/
  - pybind11文档: https://pybind11.readthedocs.io/
  - CMake Tutorial: https://cmake.org/cmake/help/latest/guide/tutorial/
- **练习**:
  - 用 `gdb` 调试一个有bug的C程序（segfault）
  - 用 `ctypes` 从Python调用一个C编写的矩阵乘法函数
  - 用 `pybind11` 封装一个C++类供Python使用
  - 编写CMakeLists.txt编译一个多文件C++项目
- **重点掌握**: gdb的核心命令(break, next, step, print, backtrace), pybind11的基本用法

---

### Week 3: Python自动化测试框架深入（每天2.5小时）

#### Day 1（周一）：pytest高级特性（2.5h）
- **知识点**:
  - pytest插件机制: `conftest.py`, hook函数
  - `pytest-xdist` 并行测试
  - `pytest-html` / `allure` 测试报告
  - 自定义marker和fixture
  - 参数化测试的高级用法
- **学习资源**:
  - pytest官方文档 - Plugin章节
  - Allure Report: https://docs.qameta.io/allure/
- **练习**:
  - 搭建一个完整的pytest项目，包含conftest.py层级配置
  - 用 `pytest-xdist` 实现测试并行执行
  - 生成Allure测试报告
- **重点掌握**: conftest.py的作用域，fixture的参数化

#### Day 2（周二）：API测试自动化（2.5h）
- **知识点**:
  - RESTful API测试原理
  - `requests` 库高级用法: session, auth, timeout, retry
  - `pytest` + `requests` API测试框架搭建
  - JSON Schema校验
  - API测试的数据驱动方法
- **学习资源**:
  - Requests文档: https://docs.python-requests.org/
  - jsonschema: https://python-jsonschema.readthedocs.io/
- **练习**:
  - 针对一个公开API（如 JSONPlaceholder）编写完整的API测试套件
  - 实现请求/响应日志记录
  - 实现JSON Schema自动校验
- **重点掌握**: API测试的断言设计，数据驱动测试模式

#### Day 3（周三）：性能测试基础（2.5h）
- **知识点**:
  - 性能测试概念: 吞吐量、延迟、P50/P90/P99
  - `locust` 负载测试框架
  - `benchmark` 模块使用
  - 性能测试报告分析
- **学习资源**:
  - Locust文档: https://docs.locust.io/
  - 性能测试最佳实践文章
- **练习**:
  - 用 `locust` 对一个Web服务进行压力测试
  - 收集并分析延迟分布（P50/P90/P99）
  - 编写性能基准测试（benchmark）
- **重点掌握**: 延迟百分位的含义，吞吐量与延迟的关系

#### Day 4（周四）：CI/CD与测试集成（2.5h）
- **知识点**:
  - GitHub Actions / GitLab CI 基础
  - Docker基础: Dockerfile, docker-compose
  - 测试环境容器化
  - 测试流水线设计: lint -> unit test -> integration test -> report
- **学习资源**:
  - GitHub Actions文档: https://docs.github.com/en/actions
  - Docker入门: https://docs.docker.com/get-started/
- **练习**:
  - 编写一个 `.github/workflows/test.yml` 实现自动化测试
  - 用Docker容器化一个测试环境
  - 设计一个完整的CI测试流水线
- **重点掌握**: CI/CD流水线设计，Docker基本命令

#### Day 5（周五）：测试策略与方法论（2.5h）
- **知识点**:
  - 测试金字塔: 单元测试 -> 集成测试 -> 端到端测试
  - 白盒测试技术: 语句覆盖、分支覆盖、路径覆盖
  - 黑盒测试技术: 等价类划分、边界值分析、决策表
  - 测试计划编写模板
  - 缺陷管理流程
- **学习资源**:
  - 《Software Testing: A Craftsman's Approach》
  - ISTQB Foundation Level教材
- **练习**:
  - 为一个假想的AI推理服务编写测试计划文档
  - 用白盒测试技术分析一段代码的测试用例设计
  - 设计等价类和边界值测试用例
- **重点掌握**: 测试金字塔的资源分配，白盒测试的覆盖准则

#### Day 6-7（周末）：综合项目 - 自动化测试框架（每天5h）
- **知识点**:
  - 综合运用本阶段所学
  - 测试框架设计模式: Page Object, Data-Driven, Keyword-Driven
  - 测试数据管理
  - 测试报告定制
- **练习（大项目）**:
  - 搭建一个完整的API自动化测试框架，包含:
    - 配置管理（多环境）
    - 测试数据管理（YAML/JSON）
    - 请求封装（带重试、日志）
    - 断言封装
    - Allure报告集成
    - CI集成
  - 将代码推送到GitHub
- **重点掌握**: 测试框架的分层设计

---

## 第二阶段: 深度学习基础 + GPU/CUDA基础（Week 4-6）

### Week 4: 深度学习基础（每天2.5小时）

#### Day 1（周一）：机器学习基础概念（2.5h）
- **知识点**:
  - 监督学习 vs 无监督学习 vs 强化学习
  - 训练(Training) vs 推理(Inference) 的区别
  - 损失函数、梯度下降、反向传播基本概念
  - 过拟合与正则化
  - 评估指标: accuracy, precision, recall, F1
- **学习资源**:
  - 吴恩达 Machine Learning Specialization (Coursera) - Week 1-2
  - 3Blue1Brown 神经网络系列视频: https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
- **练习**:
  - 手动推导一个简单线性回归的梯度下降过程
  - 用numpy实现一个2层神经网络（不用框架）
- **重点掌握**: 训练与推理的区别（这是岗位核心），梯度下降的直觉理解

#### Day 2（周二）：PyTorch基础（2.5h）
- **知识点**:
  - Tensor操作: 创建、运算、GPU转移
  - `torch.nn.Module` 定义模型
  - 前向传播与反向传播
  - `DataLoader` 数据加载
  - 模型保存与加载: `state_dict`, `torch.save`, `torch.load`
- **学习资源**:
  - PyTorch官方教程: https://pytorch.org/tutorials/beginner/basics/intro.html
  - 《Deep Learning with PyTorch》
- **练习**:
  - 用PyTorch训练一个MNIST手写数字分类器
  - 保存模型并重新加载进行推理
  - 对比CPU和GPU上的Tensor运算速度
- **重点掌握**: Tensor的device管理(CPU/GPU)，模型的save/load

#### Day 3（周三）：神经网络架构（2.5h）
- **知识点**:
  - CNN（卷积神经网络）基本结构
  - RNN/LSTM 基本原理
  - Transformer架构:
    - Self-Attention机制
    - Multi-Head Attention
    - Positional Encoding
    - Feed-Forward Network
    - Layer Normalization
  - Encoder-Decoder结构
- **学习资源**:
  - "Attention Is All You Need" 论文
  - Jay Alammar's Blog: https://jalammar.github.io/illustrated-transformer/
  - 李宏毅 Transformer 讲解视频
- **练习**:
  - 手动计算一个2x2的Self-Attention例子（Q,K,V矩阵运算）
  - 画出Transformer的完整架构图（手绘或工具）
- **重点掌握**: Self-Attention的计算过程（Q×K^T/√d → Softmax → ×V），这是后续所有优化技术的基础

#### Day 4（周四）：大语言模型(LLM)基础（2.5h）
- **知识点**:
  - GPT系列模型架构（Decoder-Only Transformer）
  - Tokenization: BPE, SentencePiece, WordPiece
  - LLM推理过程:
    - Prefill阶段 vs Decode阶段
    - KV Cache机制
    - 自回归生成(Autoregressive Generation)
  - 模型参数量与显存计算
  - 常见开源LLM: LLaMA, Mistral, Qwen, ChatGLM
- **学习资源**:
  - "GPT in 60 Lines of NumPy": https://jaykmody.com/blog/gpt-from-scratch/
  - Hugging Face Transformers文档
  - Andrej Karpathy "Let's build GPT" 视频
- **练习**:
  - 计算一个7B参数模型的显存需求（FP32, FP16, INT8, INT4）
  - 用Hugging Face加载一个小型LLM并进行推理
  - 理解并手动计算KV Cache的大小
- **重点掌握**:
  - **Prefill vs Decode的区别**（面试高频）
  - **KV Cache原理**（面试必问）
  - 显存计算方法

#### Day 5（周五）：模型格式与部署基础（2.5h）
- **知识点**:
  - 模型格式: PyTorch (.pt/.pth), ONNX, SafeTensors, GGUF
  - ONNX Runtime 推理
  - Hugging Face Model Hub 使用
  - 模型精度: FP32, FP16, BF16, INT8, INT4
  - 精度对模型性能和质量的影响
- **学习资源**:
  - ONNX官方文档: https://onnx.ai/
  - Hugging Face Hub文档
- **练习**:
  - 将一个PyTorch模型导出为ONNX格式
  - 用ONNX Runtime进行推理并与PyTorch结果对比
  - 对比FP32和FP16模型的推理速度与结果精度
- **重点掌握**: 不同模型格式的特点和适用场景，精度类型的区别

#### Day 6-7（周末）：动手实验 - 完整LLM推理流程（每天5h）
- **练习（大项目）**:
  - 在本地/服务器上部署一个开源LLM（如TinyLlama或Qwen-1.8B）
  - 实现完整的推理流程:
    1. 模型加载
    2. Tokenization
    3. 推理（含KV Cache）
    4. 解码输出
  - 监控推理过程中的GPU显存使用
  - 测量推理延迟和吞吐量
  - 编写一个简单的测试脚本验证输出正确性
- **重点掌握**: 端到端LLM推理流程，GPU显存监控方法（`nvidia-smi`, `torch.cuda.memory_allocated()`）

---

### Week 5: GPU架构与CUDA基础（每天2.5小时）

#### Day 1（周一）：GPU硬件架构（2.5h）
- **知识点**:
  - CPU vs GPU 架构对比
  - NVIDIA GPU架构层次:
    - SM (Streaming Multiprocessor)
    - CUDA Core / Tensor Core
    - Warp (32线程)
    - 显存层次: Register → Shared Memory → L1 Cache → L2 Cache → Global Memory (HBM)
  - GPU显存带宽与计算能力（FLOPS）
  - 不同GPU型号对比: A100, H100, A10, RTX 4090
  - PCIe vs NVLink
- **学习资源**:
  - NVIDIA GPU Architecture Whitepaper (Ampere/Hopper)
  - "Programming Massively Parallel Processors" 第1-3章
  - NVIDIA Developer Blog GPU Architecture系列
- **练习**:
  - 画出GPU内存层次结构图
  - 查找并对比A100和H100的关键规格（Tensor Core数量、显存带宽、FLOPS）
  - 计算 Arithmetic Intensity（算术强度）来判断一个操作是计算密集型还是内存密集型
- **重点掌握**:
  - **Tensor Core vs CUDA Core的区别**
  - **显存带宽的概念**（理解Roofline模型）
  - **Memory-bound vs Compute-bound**

#### Day 2（周二）：CUDA编程模型（2.5h）
- **知识点**:
  - CUDA编程模型: Host(CPU) + Device(GPU)
  - CUDA线程层次: Thread → Block → Grid
  - `__global__`, `__device__`, `__host__` 关键字
  - 内存管理: `cudaMalloc`, `cudaFree`, `cudaMemcpy`
  - Kernel启动配置: `<<<grid, block>>>`
  - `nvcc` 编译器
- **学习资源**:
  - NVIDIA CUDA Programming Guide: https://docs.nvidia.com/cuda/cuda-c-programming-guide/
  - CUDA by Example（入门书籍）
- **练习**:
  - 编写一个CUDA向量加法kernel
  - 实验不同block size对性能的影响
  - 用 `nvcc` 编译并运行CUDA程序
- **重点掌握**: 线程层次结构，内存拷贝方向（Host↔Device）

#### Day 3（周三）：CUDA内存优化（2.5h）
- **知识点**:
  - Global Memory合并访问(Coalesced Access)
  - Shared Memory使用与Bank Conflict
  - Constant Memory与Texture Memory
  - Memory Coalescing原则
  - Unified Memory
- **学习资源**:
  - CUDA Best Practices Guide
  - "Programming Massively Parallel Processors" 第5-7章
- **练习**:
  - 实现一个使用Shared Memory的矩阵乘法（Tiled Matrix Multiplication）
  - 对比有无Shared Memory优化的矩阵乘法性能
  - 用 `nsight compute` 分析kernel的内存访问模式
- **重点掌握**: Shared Memory优化矩阵乘法的原理，合并访问的条件

#### Day 4（周四）：CUDA性能分析与调优（2.5h）
- **知识点**:
  - NVIDIA Nsight Systems（系统级性能分析）
  - NVIDIA Nsight Compute（Kernel级性能分析）
  - Occupancy（占用率）概念
  - Warp Divergence
  - CUDA Stream与并发
  - 异步操作与事件计时
- **学习资源**:
  - Nsight Systems User Guide
  - Nsight Compute文档
- **练习**:
  - 用Nsight Systems分析一个CUDA程序的时间线
  - 用Nsight Compute分析一个kernel的性能瓶颈
  - 实现CUDA Stream并发执行多个kernel
- **重点掌握**: Nsight工具的基本使用，如何识别性能瓶颈

#### Day 5（周五）：CUDA在深度学习中的应用（2.5h）
- **知识点**:
  - cuBLAS（矩阵运算库）
  - cuDNN（深度学习加速库）
  - Tensor Core编程（WMMA API）
  - Mixed Precision Training/Inference
  - CUDA与PyTorch的关系
- **学习资源**:
  - cuBLAS文档
  - NVIDIA Mixed Precision Training文档
- **练习**:
  - 用cuBLAS实现矩阵乘法并与手写kernel对比
  - 了解PyTorch如何调用CUDA kernel（查看PyTorch源码中的CUDA部分）
  - 实验 `torch.cuda.amp` 混合精度推理
- **重点掌握**: Tensor Core如何加速矩阵运算，混合精度的原理

#### Day 6-7（周末）：GPU性能测试实战（每天5h）
- **练习（大项目）**:
  - 编写一套GPU性能测试工具:
    1. GPU信息采集脚本（显存大小、计算能力、驱动版本等）
    2. 显存带宽测试（Host→Device, Device→Host, Device→Device）
    3. 矩阵乘法性能基准测试（不同大小、不同精度）
    4. GPU利用率监控脚本（调用 `nvidia-smi`）
  - 使用 `pynvml` 或 `nvidia-smi` Python接口采集GPU指标
  - 输出结构化测试报告
- **重点掌握**: GPU性能指标的含义和采集方法

---

### Week 6: 深度学习推理流程深入（每天2.5小时）

#### Day 1（周一）：模型推理Pipeline详解（2.5h）
- **知识点**:
  - 推理Pipeline的完整流程:
    1. 模型加载（权重加载到GPU）
    2. 输入预处理（Tokenization）
    3. 前向推理（Forward Pass）
    4. 后处理（Sampling/Beam Search）
    5. 输出解码（Detokenization）
  - Greedy Decoding vs Beam Search vs Sampling (Top-K, Top-P, Temperature)
  - Batch推理 vs 单条推理
- **学习资源**:
  - Hugging Face Generation文档
  - 论文: "A Survey on Efficient Inference for Large Language Models"
- **练习**:
  - 用Hugging Face实现不同解码策略并对比输出
  - 测量不同batch size下的推理吞吐量
- **重点掌握**: 解码策略的差异和适用场景

#### Day 2（周二）：推理性能指标与测量（2.5h）
- **知识点**:
  - LLM推理核心指标:
    - TTFT (Time To First Token) - 首token延迟
    - TPOT (Time Per Output Token) - 每token延迟
    - Throughput (tokens/sec) - 吞吐量
    - Latency (端到端延迟)
  - 性能测量方法与工具
  - 性能基准测试设计
  - SLA (Service Level Agreement) 定义
- **学习资源**:
  - Anyscale Blog "LLM Performance Benchmarking"
  - vLLM Benchmarking文档
- **练习**:
  - 编写一个Python脚本测量LLM推理的TTFT、TPOT、Throughput
  - 设计一套LLM推理性能基准测试方案
- **重点掌握**:
  - **TTFT和TPOT的概念和测量方法**（面试高频）
  - 如何设计有意义的性能基准测试

#### Day 3（周三）：模型推理优化概览（2.5h）
- **知识点**:
  - 推理优化技术分类:
    - 模型级优化: 量化、剪枝、蒸馏
    - 系统级优化: 算子融合、KV Cache优化、内存管理
    - 服务级优化: Batching策略、调度策略、负载均衡
  - 计算图优化: 算子融合(Operator Fusion)、常量折叠
  - 内存优化: 内存复用、梯度检查点
- **学习资源**:
  - 论文: "Efficient Transformers: A Survey"
  - NVIDIA TensorRT Optimization Guide
- **练习**:
  - 绘制推理优化技术的思维导图
  - 分析一个Transformer模型的计算瓶颈（哪些层最耗时）
- **重点掌握**: 优化技术的分层思想，不同级别优化的关系

#### Day 4（周四）：Hugging Face生态系统（2.5h）
- **知识点**:
  - `transformers` 库核心API
  - `accelerate` 库: 多GPU推理
  - `optimum` 库: 推理优化
  - Model Hub, Datasets, Tokenizers
  - Pipeline API 快速使用
- **学习资源**:
  - Hugging Face官方文档和教程
  - Hugging Face Course: https://huggingface.co/course
- **练习**:
  - 用Pipeline API快速实现文本生成、文本分类、问答
  - 用accelerate实现多GPU推理（如果有多卡）
  - 探索optimum的推理优化功能
- **重点掌握**: transformers库的核心API，模型加载的不同方式

#### Day 5（周五）：推理服务化基础（2.5h）
- **知识点**:
  - FastAPI构建推理服务
  - gRPC vs REST API
  - 推理服务的关键设计要素:
    - 请求队列
    - 超时处理
    - 健康检查
    - 优雅关闭
  - OpenAI API兼容接口规范
- **学习资源**:
  - FastAPI文档: https://fastapi.tiangolo.com/
  - OpenAI API文档
- **练习**:
  - 用FastAPI封装一个LLM推理服务，提供OpenAI兼容接口
  - 实现流式响应(Streaming)
  - 编写API测试用例
- **重点掌握**: 推理服务的架构设计，流式响应的实现

#### Day 6-7（周末）：综合实验 - 推理服务搭建与测试（每天5h）
- **练习（大项目）**:
  - 搭建一个完整的LLM推理服务:
    1. 用FastAPI+transformers搭建服务
    2. 实现OpenAI兼容API（`/v1/chat/completions`）
    3. 支持流式和非流式响应
    4. 编写完整的API测试套件（功能测试 + 性能测试）
    5. 用Docker容器化
    6. 测量并记录性能指标
  - 编写测试报告
- **重点掌握**: 端到端的推理服务搭建和测试流程

---

## 第三阶段: LLM推理引擎（Week 7-9）

### Week 7: vLLM深入（每天2.5小时）

#### Day 1（周一）：vLLM架构概览（2.5h）
- **知识点**:
  - vLLM诞生背景与核心创新
  - vLLM整体架构:
    - LLMEngine
    - Scheduler（调度器）
    - Worker
    - ModelRunner
    - CacheEngine
  - 安装与基本使用
  - 支持的模型列表和硬件要求
- **学习资源**:
  - vLLM官方文档: https://docs.vllm.ai/
  - vLLM GitHub仓库: https://github.com/vllm-project/vllm
  - 论文: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
- **练习**:
  - 安装vLLM并运行一个示例模型
  - 阅读vLLM架构图，理解各组件职责
  - 用vLLM的Python API进行离线推理
- **重点掌握**: vLLM的核心创新点（PagedAttention），架构组件关系

#### Day 2（周二）：PagedAttention原理（2.5h）
- **知识点**:
  - 传统KV Cache的问题:
    - 内存碎片化
    - 预分配浪费
    - 无法高效共享
  - PagedAttention核心思想:
    - 将KV Cache分为固定大小的Block
    - 类似操作系统虚拟内存的页表管理
    - Block Table映射
  - 内存利用率提升分析
  - PagedAttention v1 vs v2
- **学习资源**:
  - 论文精读: "Efficient Memory Management for LLM Serving with PagedAttention"
  - vLLM Blog系列文章
  - 知乎/Medium上的PagedAttention详解文章
- **练习**:
  - 手动画出PagedAttention的Block分配过程
  - 计算传统方式 vs PagedAttention的内存利用率差异
  - 阅读vLLM源码中PagedAttention相关代码
- **重点掌握**:
  - **PagedAttention的核心原理**（面试必问）
  - Block的分配与回收机制
  - 与OS虚拟内存管理的类比

#### Day 3（周三）：vLLM调度器与Continuous Batching（2.5h）
- **知识点**:
  - 传统Static Batching的问题
  - Continuous Batching (连续批处理):
    - Iteration-level调度
    - 请求的动态加入和移除
    - Prefill与Decode的混合调度
  - vLLM调度策略:
    - FCFS (First Come First Serve)
    - Preemption（抢占）: Swap vs Recomputation
  - Waiting Queue, Running Queue, Swapped Queue
- **学习资源**:
  - 论文: "Orca: A Distributed Serving System for Transformer-Based Generative Models"
  - vLLM调度器源码: `vllm/core/scheduler.py`
- **练习**:
  - 对比Static Batching和Continuous Batching的吞吐量差异（使用vLLM benchmark）
  - 阅读vLLM调度器源码，理解调度逻辑
  - 模拟一个Continuous Batching的调度过程（纸上推演）
- **重点掌握**:
  - **Continuous Batching的原理和优势**（面试高频）
  - 抢占策略的选择

#### Day 4（周四）：vLLM API与部署（2.5h）
- **知识点**:
  - vLLM离线推理API: `LLM`, `SamplingParams`
  - vLLM在线服务: `vllm serve` 命令
  - OpenAI兼容API使用
  - 关键配置参数:
    - `tensor-parallel-size`
    - `max-model-len`
    - `gpu-memory-utilization`
    - `max-num-seqs`
    - `dtype`
  - 多GPU部署（Tensor Parallelism）
- **学习资源**:
  - vLLM API文档
  - vLLM配置参数详解
- **练习**:
  - 用vLLM部署一个OpenAI兼容的API服务
  - 实验不同配置参数对性能的影响
  - 用curl和Python客户端测试vLLM服务
  - 编写自动化测试脚本验证API功能
- **重点掌握**: 关键配置参数的含义和调优方法

#### Day 5（周五）：vLLM性能测试（2.5h）
- **知识点**:
  - vLLM自带benchmark工具:
    - `benchmark_serving.py`
    - `benchmark_throughput.py`
    - `benchmark_latency.py`
  - 性能测试指标收集与分析
  - vLLM Metrics (Prometheus metrics)
  - 性能对比方法论
- **学习资源**:
  - vLLM benchmarks目录
  - vLLM性能优化文档
- **练习**:
  - 运行vLLM benchmark工具，收集性能数据
  - 对比不同模型、不同配置的性能
  - 监控vLLM的Prometheus指标
  - 编写性能测试报告
- **重点掌握**: 如何系统地测试和分析vLLM性能

#### Day 6-7（周末）：vLLM源码阅读与测试实战（每天5h）
- **练习（大项目）**:
  - 深入阅读vLLM核心源码:
    1. `vllm/engine/llm_engine.py` - 引擎主逻辑
    2. `vllm/core/scheduler.py` - 调度器
    3. `vllm/core/block_manager.py` - Block管理
    4. `vllm/worker/` - Worker执行逻辑
  - 为vLLM编写测试用例:
    - API功能测试
    - 不同采样参数的测试
    - 并发请求测试
    - 长文本推理测试
    - 错误处理测试
  - 记录源码阅读笔记
- **重点掌握**: vLLM的代码组织和核心流程

---

### Week 8: TensorRT与TensorRT-LLM（每天2.5小时）

#### Day 1（周一）：TensorRT基础（2.5h）
- **知识点**:
  - TensorRT是什么: NVIDIA高性能推理优化器和运行时
  - TensorRT工作流程:
    1. 模型导入（ONNX/PyTorch）
    2. 优化（Layer Fusion, Precision Calibration, Kernel Auto-Tuning）
    3. 序列化Engine
    4. 运行时推理
  - TensorRT优化技术:
    - Layer/Tensor Fusion
    - Precision Calibration (FP32→FP16→INT8)
    - Kernel Auto-Tuning
    - Dynamic Shape支持
  - TensorRT vs ONNX Runtime
- **学习资源**:
  - TensorRT官方文档: https://docs.nvidia.com/deeplearning/tensorrt/
  - NVIDIA Developer Blog TensorRT系列
  - TensorRT Quick Start Guide
- **练习**:
  - 安装TensorRT
  - 将一个ONNX模型转换为TensorRT Engine
  - 对比TensorRT和PyTorch的推理速度
- **重点掌握**: TensorRT的优化原理，Layer Fusion的概念

#### Day 2（周二）：TensorRT-LLM架构（2.5h）
- **知识点**:
  - TensorRT-LLM的定位: 专门为LLM优化的推理框架
  - 与原始TensorRT的区别和联系
  - TensorRT-LLM架构:
    - Model Definition (Python API)
    - Build Engine
    - Runtime
  - 支持的模型和功能
  - 与vLLM的对比
- **学习资源**:
  - TensorRT-LLM GitHub: https://github.com/NVIDIA/TensorRT-LLM
  - TensorRT-LLM官方文档
  - NVIDIA GTC演讲视频
- **练习**:
  - 安装TensorRT-LLM
  - 用TensorRT-LLM构建一个LLM推理引擎
  - 了解TensorRT-LLM的模型转换流程
- **重点掌握**: TensorRT-LLM的核心优势和使用流程

#### Day 3（周三）：TensorRT-LLM优化特性（2.5h）
- **知识点**:
  - In-Flight Batching（类似Continuous Batching）
  - KV Cache优化: Paged KV Cache
  - 量化支持: FP8, INT8, INT4 (AWQ, GPTQ)
  - Tensor Parallelism & Pipeline Parallelism
  - Custom Attention Kernels (Flash Attention, XQA)
  - Speculative Decoding支持
- **学习资源**:
  - TensorRT-LLM文档 - Performance Best Practices
  - TensorRT-LLM examples目录
- **练习**:
  - 实验不同量化模式的推理性能
  - 配置Tensor Parallelism进行多GPU推理
  - 对比不同优化选项的效果
- **重点掌握**: TensorRT-LLM的核心优化技术，与vLLM的对比

#### Day 4（周四）：TensorRT-LLM部署与测试（2.5h）
- **知识点**:
  - Triton Inference Server集成
  - TensorRT-LLM服务化部署
  - 性能基准测试方法
  - 模型精度验证
  - 常见问题排查
- **学习资源**:
  - Triton Inference Server文档
  - TensorRT-LLM部署指南
- **练习**:
  - 用Triton部署TensorRT-LLM模型
  - 编写精度验证脚本（与原始模型对比输出）
  - 运行性能基准测试
  - 编写API自动化测试
- **重点掌握**: Triton Inference Server的使用，精度验证方法

#### Day 5（周五）：推理引擎对比分析（2.5h）
- **知识点**:
  - vLLM vs TensorRT-LLM vs llama.cpp vs SGLang 对比:
    - 性能
    - 易用性
    - 功能丰富度
    - 硬件要求
    - 社区活跃度
  - 不同场景下的引擎选择建议
  - 其他推理框架简介: DeepSpeed-MII, text-generation-inference
- **学习资源**:
  - 各框架官方benchmark结果
  - 社区对比文章和博客
- **练习**:
  - 在同一模型上对比vLLM和TensorRT-LLM的性能
  - 编写对比测试报告（延迟、吞吐量、显存使用、功能差异）
  - 总结不同场景的最佳引擎选择
- **重点掌握**: 各引擎的优劣势和适用场景（面试高频）

#### Day 6-7（周末）：推理引擎测试实战（每天5h）
- **练习（大项目）**:
  - 设计并实施一套LLM推理引擎测试方案:
    1. **功能测试**: 基本推理、流式输出、并发请求、边界条件
    2. **性能测试**: TTFT、TPOT、吞吐量、不同并发数
    3. **精度测试**: 输出一致性、量化精度损失
    4. **稳定性测试**: 长时间运行、内存泄漏检测
    5. **兼容性测试**: 不同模型、不同配置
  - 输出完整的测试报告
  - 将测试框架代码整理到GitHub
- **重点掌握**: LLM推理引擎的测试方法论

---

### Week 9: 推理引擎进阶与其他框架（每天2.5小时）

#### Day 1（周一）：SGLang框架（2.5h）
- **知识点**:
  - SGLang的设计理念
  - RadixAttention
  - 结构化生成(Structured Generation)
  - 与vLLM的对比
- **学习资源**:
  - SGLang GitHub: https://github.com/sgl-project/sglang
  - SGLang论文
- **练习**:
  - 安装并运行SGLang
  - 测试结构化生成功能
  - 对比SGLang和vLLM的性能
- **重点掌握**: RadixAttention的核心思想

#### Day 2（周二）：llama.cpp与边缘部署（2.5h）
- **知识点**:
  - llama.cpp的定位: CPU/边缘设备上的LLM推理
  - GGUF格式
  - CPU优化技术: SIMD, AVX2
  - 量化在llama.cpp中的应用
  - Metal/Vulkan GPU后端
- **学习资源**:
  - llama.cpp GitHub: https://github.com/ggerganov/llama.cpp
- **练习**:
  - 编译llama.cpp
  - 用不同量化级别运行模型，对比性能和质量
  - 在CPU上测试推理性能
- **重点掌握**: GGUF量化格式，CPU推理优化

#### Day 3（周三）：推理引擎的测试策略设计（2.5h）
- **知识点**:
  - 推理引擎测试分层:
    - 单元测试（算子正确性）
    - 集成测试（Pipeline完整性）
    - 系统测试（端到端功能）
    - 性能测试（延迟、吞吐量）
    - 压力测试（稳定性）
  - 测试用例设计方法
  - 回归测试策略
  - 精度验证框架设计
- **学习资源**:
  - vLLM/TensorRT-LLM的tests目录结构
  - 测试策略最佳实践文章
- **练习**:
  - 参考vLLM的测试目录结构，设计自己的测试框架
  - 编写推理引擎的测试计划文档
  - 实现精度验证自动化脚本
- **重点掌握**: 推理引擎测试的分层设计，精度验证方法

#### Day 4（周四）：分布式推理基础（2.5h）
- **知识点**:
  - 分布式推理的必要性（模型太大，单卡放不下）
  - Tensor Parallelism (TP):
    - 列并行(Column Parallel)
    - 行并行(Row Parallel)
    - All-Reduce操作
  - Pipeline Parallelism (PP)
  - TP vs PP 的选择
  - NCCL通信库
- **学习资源**:
  - 论文: "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism"
  - NCCL文档
- **练习**:
  - 画出Tensor Parallelism的数据流图
  - 理解All-Reduce操作的过程
  - 在vLLM中配置Tensor Parallelism（如果有多卡）
- **重点掌握**:
  - **Tensor Parallelism的原理**（面试高频）
  - TP和PP的区别和适用场景

#### Day 5（周五）：推理服务的监控与可观测性（2.5h）
- **知识点**:
  - Prometheus + Grafana 监控体系
  - 推理服务关键监控指标:
    - 请求延迟分布
    - 吞吐量
    - GPU利用率/显存使用
    - 队列长度
    - 错误率
  - 日志分析与告警设计
  - 分布式追踪(Tracing)
- **学习资源**:
  - Prometheus文档
  - Grafana文档
- **练习**:
  - 搭建Prometheus + Grafana监控vLLM服务
  - 创建关键指标的Dashboard
  - 设计告警规则
- **重点掌握**: 推理服务的核心监控指标

#### Day 6-7（周末）：综合实战 - 多引擎测试平台（每天5h）
- **练习（大项目）**:
  - 构建一个多引擎LLM推理测试平台:
    1. 支持vLLM、TensorRT-LLM等多种引擎
    2. 统一的测试接口（适配器模式）
    3. 自动化性能基准测试
    4. 精度对比测试
    5. 测试结果可视化
    6. 测试报告自动生成
  - 代码整理并推送到GitHub
- **重点掌握**: 测试平台的架构设计，适配器模式的应用

---

## 第四阶段: 推理优化技术（Week 10-12）

### Week 10: Attention优化（每天2.5小时）

#### Day 1（周一）：标准Attention的计算瓶颈（2.5h）
- **知识点**:
  - 标准Self-Attention的计算复杂度: O(n²)
  - Attention的计算步骤:
    1. Q × K^T → Attention Score (n×n矩阵)
    2. Softmax
    3. Score × V → Output
  - 内存瓶颈: n×n的注意力矩阵
  - IO-Awareness的重要性: GPU的计算速度远快于内存带宽
- **学习资源**:
  - 论文: "Self-Attention Does Not Need O(n²) Memory"
  - GPU内存层次回顾
- **练习**:
  - 手动计算标准Attention对于序列长度n=1024的内存需求
  - 用PyTorch实现标准Attention并Profile其内存使用
  - 对比不同序列长度下Attention的计算时间
- **重点掌握**: 标准Attention的O(n²)复杂度及其实际影响

#### Day 2（周二）：FlashAttention原理（2.5h）
- **知识点**:
  - FlashAttention核心思想: IO-Aware Attention
  - Tiling技术: 分块计算避免实例化完整的n×n矩阵
  - Online Softmax算法
  - 减少HBM读写次数
  - FlashAttention v1 vs v2 vs v3的改进
  - 硬件感知(Hardware-Aware)算法设计
- **学习资源**:
  - 论文: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
  - 论文: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"
  - Tri Dao的演讲视频
- **练习**:
  - 在纸上推导FlashAttention的分块计算过程
  - 安装flash-attn库并对比FlashAttention vs 标准Attention的速度和显存
  - 理解Online Softmax算法
- **重点掌握**:
  - **FlashAttention的核心原理: Tiling + IO-Awareness**（面试必问）
  - 为什么能在不牺牲精度的情况下提升性能
  - SRAM vs HBM的数据移动优化

#### Day 3（周三）：PagedAttention深入（2.5h）
- **知识点**:
  - 回顾PagedAttention基本原理
  - PagedAttention的CUDA Kernel实现思路
  - Block Manager的详细设计:
    - Physical Block vs Logical Block
    - Block分配策略
    - Block共享（Prefix Caching, Beam Search）
  - Copy-on-Write机制
  - PagedAttention与FlashAttention的结合
- **学习资源**:
  - vLLM源码中的attention实现
  - PagedAttention论文细节
- **练习**:
  - 阅读vLLM的block_manager源码
  - 实现一个简化版的Block Manager（Python）
  - 分析PagedAttention在Prefix Caching场景下的优势
- **重点掌握**: Block Manager的设计，Copy-on-Write的原理

#### Day 4（周四）：Multi-Query/Grouped-Query Attention（2.5h）
- **知识点**:
  - Multi-Head Attention (MHA) 回顾
  - Multi-Query Attention (MQA):
    - 所有Head共享一组KV
    - 减少KV Cache大小
  - Grouped-Query Attention (GQA):
    - 介于MHA和MQA之间
    - 多个Head共享一组KV
  - 各LLM使用的Attention类型
  - 对推理性能和模型质量的影响
- **学习资源**:
  - 论文: "Multi-Query Attention is All You Need"
  - 论文: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
- **练习**:
  - 计算MHA, GQA, MQA的KV Cache大小差异（以LLaMA-70B为例）
  - 在代码中实现MHA和GQA，对比KV Cache内存占用
- **重点掌握**:
  - **MHA/GQA/MQA的区别和KV Cache大小计算**（面试高频）
  - 为什么GQA是当前的主流选择

#### Day 5（周五）：Prefix Caching与其他Attention优化（2.5h）
- **知识点**:
  - Prefix Caching (前缀缓存):
    - 原理: 相同前缀的请求共享KV Cache
    - 适用场景: System Prompt, Few-Shot Prompt
    - 在vLLM中的实现
  - Sliding Window Attention
  - Sparse Attention
  - Ring Attention（长序列并行）
- **学习资源**:
  - vLLM Prefix Caching文档
  - 论文: "Ring Attention with Blockwise Transformers for Near-Infinite Context"
- **练习**:
  - 在vLLM中启用Prefix Caching并测试性能提升
  - 分析不同场景下Prefix Caching的收益
  - 对比有无Prefix Caching的TTFT差异
- **重点掌握**: Prefix Caching的原理和适用场景

#### Day 6-7（周末）：Attention优化综合实验（每天5h）
- **练习（大项目）**:
  - 设计一套Attention优化的测试与验证方案:
    1. 标准Attention基准测试
    2. FlashAttention性能对比（不同序列长度）
    3. PagedAttention内存效率对比
    4. Prefix Caching效果验证
    5. 不同Attention变体的精度验证
  - 编写自动化测试脚本
  - 生成可视化对比报告（图表）
  - 撰写测试分析文档
- **重点掌握**: Attention优化技术的测试方法论

---

### Week 11: 量化与剪枝（每天2.5小时）

#### Day 1（周一）：量化基础原理（2.5h）
- **知识点**:
  - 量化的定义: 将高精度数值映射到低精度
  - 数据类型回顾: FP32, FP16, BF16, INT8, INT4, FP8
  - 量化方法分类:
    - Post-Training Quantization (PTQ) vs Quantization-Aware Training (QAT)
    - Symmetric vs Asymmetric量化
    - Per-Tensor vs Per-Channel vs Per-Group量化
  - 量化的数学公式: `q = round(x / scale + zero_point)`
  - 反量化: `x ≈ (q - zero_point) * scale`
- **学习资源**:
  - 论文: "A Survey of Quantization Methods for Efficient Neural Network Inference"
  - NVIDIA Quantization Toolkit文档
  - Hugging Face Quantization文档
- **练习**:
  - 手动实现一个简单的INT8量化和反量化函数
  - 对比不同量化粒度（per-tensor vs per-channel）的精度损失
  - 量化一个小模型并测量精度和速度变化
- **重点掌握**:
  - **PTQ vs QAT的区别**
  - 量化公式和反量化公式
  - Per-Group量化为什么比Per-Tensor精度高

#### Day 2（周二）：GPTQ量化（2.5h）
- **知识点**:
  - GPTQ原理:
    - 基于Hessian矩阵的逐层量化
    - OBQ (Optimal Brain Quantization) 的改进
    - 量化误差的最优补偿
  - GPTQ的优势与限制
  - GPTQ工具使用: `auto-gptq`, `gptq` in transformers
  - 校准数据(Calibration Data)的选择
- **学习资源**:
  - 论文: "GPTQ: Accurate Post-Training Quantization for Generative Pre-Trained Transformers"
  - AutoGPTQ GitHub: https://github.com/AutoGPTQ/AutoGPTQ
- **练习**:
  - 用AutoGPTQ量化一个开源LLM (如Llama-2-7B)
  - 对比FP16和GPTQ-INT4的推理速度和输出质量
  - 测试不同校准数据对量化质量的影响
- **重点掌握**:
  - **GPTQ的核心原理**（面试常问）
  - 校准数据的重要性

#### Day 3（周三）：AWQ量化（2.5h）
- **知识点**:
  - AWQ (Activation-Aware Weight Quantization) 原理:
    - 观察: 不是所有权重都同等重要
    - 关键思想: 保护对激活值影响大的"显著"权重通道
    - 通过缩放(Scaling)而非保留来保护显著权重
  - AWQ vs GPTQ对比:
    - 精度
    - 量化速度
    - 推理速度
    - 鲁棒性
  - AWQ工具使用: `autoawq`
- **学习资源**:
  - 论文: "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
  - AutoAWQ GitHub: https://github.com/casper-hansen/AutoAWQ
- **练习**:
  - 用AutoAWQ量化一个模型
  - 对比AWQ和GPTQ在同一模型上的效果
  - 分析AWQ对不同任务（文本生成、问答、编码）的精度影响
- **重点掌握**:
  - **AWQ的核心创新: Activation-aware + Scaling**（面试常问）
  - AWQ vs GPTQ的对比

#### Day 4（周四）：其他量化方法与FP8（2.5h）
- **知识点**:
  - SmoothQuant: W8A8量化（权重和激活都量化）
  - GGUF量化格式 (Q2_K, Q4_K_M, Q5_K_S等)
  - FP8量化:
    - E4M3 vs E5M2格式
    - H100对FP8的原生支持
    - FP8 vs INT8的对比
  - 量化对模型能力的影响评估方法
  - Perplexity作为量化质量指标
- **学习资源**:
  - 论文: "SmoothQuant: Accurate and Efficient Post-Training Quantization for LLMs"
  - NVIDIA FP8文档
- **练习**:
  - 了解不同GGUF量化级别的精度损失
  - 计算Perplexity评估量化模型质量
  - 总结各量化方法的对比表格
- **重点掌握**: 量化方法选择的决策依据，Perplexity评估

#### Day 5（周五）：模型剪枝与知识蒸馏（2.5h）
- **知识点**:
  - 模型剪枝:
    - 非结构化剪枝 (Unstructured Pruning): 移除单个权重
    - 结构化剪枝 (Structured Pruning): 移除整个通道/层
    - SparseGPT: LLM专用剪枝方法
    - N:M稀疏性 (如2:4 Sparsity, NVIDIA Ampere支持)
  - 知识蒸馏:
    - Teacher-Student框架
    - 在LLM中的应用
  - 剪枝 vs 量化的对比与结合
- **学习资源**:
  - 论文: "SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot"
  - NVIDIA 2:4 Sparsity文档
- **练习**:
  - 用PyTorch实现简单的非结构化剪枝
  - 了解2:4 Sparsity在NVIDIA GPU上的加速效果
  - 实验剪枝+量化的联合应用
- **重点掌握**: 结构化 vs 非结构化剪枝的区别，2:4 Sparsity的概念

#### Day 6-7（周末）：量化测试实战（每天5h）
- **练习（大项目）**:
  - 构建一个量化效果评估框架:
    1. 支持多种量化方法（GPTQ, AWQ, GGUF）
    2. 自动化量化流程
    3. 精度评估（Perplexity, 任务准确率）
    4. 性能评估（推理速度, 显存占用）
    5. 质量评估（输出对比, 人工评分框架）
    6. 生成对比报告（表格 + 图表）
  - 选择一个模型，执行完整的量化评估流程
  - 撰写量化评估报告
- **重点掌握**: 量化评估的完整方法论

---

### Week 12: Speculative Decoding与高级优化（每天2.5小时）

#### Day 1（周一）：Speculative Decoding原理（2.5h）
- **知识点**:
  - 自回归解码的瓶颈: 串行生成，GPU利用率低
  - Speculative Decoding核心思想:
    - Draft Model (小模型) 快速生成候选token
    - Target Model (大模型) 并行验证
    - 接受/拒绝采样
  - 加速原理: 将串行解码转化为并行验证
  - Speculative Decoding的无损性（数学证明）
  - Draft Model的选择策略
- **学习资源**:
  - 论文: "Fast Inference from Transformers via Speculative Decoding"
  - 论文: "Accelerating Large Language Model Decoding with Speculative Sampling"
  - vLLM Speculative Decoding文档
- **练习**:
  - 理解并手动模拟Speculative Decoding的流程
  - 计算不同acceptance rate下的加速比
  - 在vLLM中启用Speculative Decoding并测试效果
- **重点掌握**:
  - **Speculative Decoding的原理**（面试高频）
  - 为什么是无损的
  - acceptance rate对加速效果的影响

#### Day 2（周二）：Speculative Decoding变体（2.5h）
- **知识点**:
  - Draft Model方式:
    - 小模型作为Draft
    - Self-Speculative (模型自身的早期层作为Draft)
    - Medusa (多头预测)
    - Eagle
  - Tree-based Speculative Decoding
  - Lookahead Decoding
  - Speculative Decoding在不同场景下的效果
- **学习资源**:
  - 论文: "Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"
  - 论文: "EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty"
- **练习**:
  - 对比不同Speculative Decoding变体的加速效果
  - 分析不同场景（代码生成、翻译、创意写作）下的acceptance rate
  - 在vLLM中测试不同的draft model配置
- **重点掌握**: 不同变体的优劣势，Medusa的多头预测思想

#### Day 3（周三）：算子融合与编译优化（2.5h）
- **知识点**:
  - 算子融合 (Operator/Kernel Fusion):
    - 为什么有效: 减少内存读写和kernel启动开销
    - 常见融合模式: QKV融合, Add+LayerNorm融合, GELU融合
  - torch.compile (PyTorch 2.0):
    - TorchDynamo (前端)
    - TorchInductor (后端)
    - 动态Shape支持
  - Triton编程语言（OpenAI Triton，不是Triton Server）
  - CUDA Graph: 减少kernel启动开销
- **学习资源**:
  - PyTorch torch.compile文档
  - Triton语言教程: https://triton-lang.org/
  - NVIDIA CUDA Graph文档
- **练习**:
  - 用 `torch.compile` 加速一个PyTorch模型推理
  - 了解Triton语言编写一个简单的kernel（如vector add）
  - 实验CUDA Graph对推理延迟的影响
- **重点掌握**: 算子融合的原理，torch.compile的使用

#### Day 4（周四）：内存优化与长上下文（2.5h）
- **知识点**:
  - KV Cache压缩技术:
    - KV Cache量化
    - Token eviction策略 (H2O, StreamingLLM)
  - 长上下文推理的挑战:
    - 显存限制
    - Attention的O(n²)问题
  - 解决方案:
    - Ring Attention
    - Chunked Prefill
    - 滑动窗口
  - 显存优化技巧总结
- **学习资源**:
  - 论文: "Efficient Streaming Language Models with Attention Sinks"
  - 论文: "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of LLMs"
- **练习**:
  - 在vLLM中测试不同max-model-len的显存使用
  - 实验Chunked Prefill对TTFT的影响
  - 分析长上下文场景下的性能瓶颈
- **重点掌握**: KV Cache压缩的思路，长上下文推理的挑战和解决方案

#### Day 5（周五）：推理优化技术综合回顾（2.5h）
- **知识点**:
  - 所有优化技术的系统化整理:
    - 模型级: 量化(AWQ/GPTQ/FP8), 剪枝, 蒸馏
    - 算法级: FlashAttention, PagedAttention, Speculative Decoding, GQA
    - 系统级: Continuous Batching, 算子融合, CUDA Graph, 内存管理
    - 硬件级: Tensor Core, NVLink, 分布式
  - 各技术的适用场景与组合策略
  - 优化的trade-off分析
- **练习**:
  - 绘制推理优化技术的完整思维导图
  - 为不同场景（低延迟、高吞吐、资源受限）设计优化方案
  - 编写一份推理优化技术总结文档
- **重点掌握**: 各优化技术的全局理解和组合能力

#### Day 6-7（周末）：推理优化综合测试项目（每天5h）
- **练习（大项目）**:
  - 设计一个完整的推理优化效果测试项目:
    1. 选择一个基准模型（如Llama-2-7B）
    2. 逐一应用不同优化技术并测量效果:
       - Baseline (FP16, 无优化)
       - + FlashAttention
       - + Continuous Batching (vLLM)
       - + Quantization (AWQ/GPTQ)
       - + Speculative Decoding
    3. 记录每个优化步骤的:
       - TTFT, TPOT, Throughput
       - GPU显存使用
       - 输出质量（Perplexity）
    4. 生成可视化对比报告
    5. 撰写优化分析文档
- **重点掌握**: 推理优化技术的量化评估能力

---

## 第五阶段: AI软件测试方法论与自动化（Week 13-14）

### Week 13: AI系统测试方法论（每天2.5小时）

#### Day 1（周一）：AI/ML系统的测试挑战（2.5h）
- **知识点**:
  - AI系统 vs 传统软件系统的测试差异:
    - 非确定性输出
    - 模型行为的"黑盒"特性
    - 数据依赖性
    - 精度vs性能的trade-off
  - AI系统的质量属性:
    - 功能正确性
    - 性能（延迟、吞吐）
    - 鲁棒性
    - 公平性
    - 可解释性
  - AI测试的分层策略
- **学习资源**:
  - 论文: "Machine Learning Testing: Survey, Landscapes and Horizons"
  - Google "ML Test Score" 论文
- **练习**:
  - 分析一个AI推理系统的测试需求
  - 列出AI系统特有的测试类型和方法
  - 设计AI系统测试的质量评估维度
- **重点掌握**: AI系统测试的独特挑战和策略

#### Day 2（周二）：LLM推理的功能测试（2.5h）
- **知识点**:
  - LLM推理功能测试设计:
    - 基本生成能力测试
    - 多轮对话测试
    - 特殊输入测试（空输入、超长输入、特殊字符）
    - 采样参数测试（temperature, top_p, top_k, max_tokens）
    - 停止条件测试（stop tokens, max length）
    - 流式vs非流式输出测试
  - 测试数据设计
  - 断言策略（LLM输出的验证方法）
- **学习资源**:
  - vLLM测试用例参考
  - OpenAI API文档（功能规范参考）
- **练习**:
  - 编写一套完整的LLM推理API功能测试用例（50+）
  - 实现测试数据生成器
  - 设计LLM输出的自动验证方法
- **重点掌握**: LLM推理的功能测试设计，非确定性输出的验证方法

#### Day 3（周三）：性能测试与基准测试设计（2.5h）
- **知识点**:
  - 性能测试设计方法论:
    - 负载模型设计（并发用户、请求速率）
    - 测试数据设计（输入长度分布、输出长度分布）
    - 预热(Warmup)策略
    - 统计显著性
  - 基准测试工具:
    - vLLM benchmarks
    - GenAI-Perf
    - 自定义benchmark脚本
  - 性能回归检测方法
  - 容量规划测试
- **学习资源**:
  - GenAI-Perf文档
  - 性能测试最佳实践
- **练习**:
  - 设计一套LLM推理性能基准测试方案（详细文档）
  - 实现自定义性能测试脚本（支持可配置并发、输入长度、持续时间）
  - 建立性能基准线(Baseline)并设计回归检测阈值
- **重点掌握**: 性能测试的科学方法，统计分析能力

#### Day 4（周四）：兼容性与回归测试（2.5h）
- **知识点**:
  - 兼容性测试维度:
    - 不同GPU型号（A100, H100, RTX 4090等）
    - 不同驱动版本
    - 不同CUDA版本
    - 不同操作系统
    - 不同Python版本
    - 不同模型格式
  - 回归测试策略:
    - 版本升级回归测试
    - 配置变更回归测试
    - 精度回归测试
  - 测试矩阵设计
  - CI/CD中的自动化回归测试
- **学习资源**:
  - 兼容性测试最佳实践
  - NVIDIA GPU兼容性矩阵
- **练习**:
  - 设计一个推理引擎的兼容性测试矩阵
  - 实现自动化回归测试脚本
  - 设计版本升级的回归测试方案
- **重点掌握**: 测试矩阵设计，回归测试的自动化

#### Day 5（周五）：稳定性与可靠性测试（2.5h）
- **知识点**:
  - 稳定性测试类型:
    - 长时间运行测试（Soak Test）
    - 内存泄漏检测
    - GPU显存泄漏检测
    - 错误恢复测试
    - 压力测试（高并发、大输入）
  - 混沌工程(Chaos Engineering)在AI系统中的应用
  - 日志分析与问题定位
  - 根因分析(Root Cause Analysis)方法
- **学习资源**:
  - 混沌工程原则
  - Linux性能分析工具链
- **练习**:
  - 设计并执行一个24小时稳定性测试
  - 编写GPU显存泄漏检测脚本
  - 模拟各种故障场景（OOM, GPU挂起, 网络中断）并验证系统行为
- **重点掌握**: 稳定性测试方法，内存泄漏检测

#### Day 6-7（周末）：AI QA策略文档编写（每天5h）
- **练习（大项目）**:
  - 编写一份完整的AI推理引擎QA策略文档:
    1. 测试目标和范围
    2. 测试分层策略
    3. 各类测试的详细方案:
       - 功能测试方案
       - 性能测试方案
       - 精度验证方案
       - 兼容性测试方案
       - 稳定性测试方案
    4. 测试环境要求
    5. 测试工具和框架
    6. 测试数据管理
    7. 缺陷管理流程
    8. 测试报告模板
  - 这份文档可以作为面试时展示的作品
- **重点掌握**: QA策略文档的完整编写能力

---

### Week 14: 自动化测试框架实战（每天2.5小时）

#### Day 1（周一）：测试框架架构设计（2.5h）
- **知识点**:
  - AI推理测试框架的架构设计:
    - 模块化设计
    - 配置驱动
    - 可扩展性
  - 框架核心组件:
    - Config Manager（配置管理）
    - Engine Adapter（引擎适配器）
    - Test Runner（测试执行器）
    - Data Generator（数据生成器）
    - Result Collector（结果收集器）
    - Report Generator（报告生成器）
  - 设计模式应用: 策略模式、工厂模式、适配器模式
- **练习**:
  - 设计测试框架的类图和模块关系
  - 搭建框架的项目结构
  - 实现Config Manager模块

#### Day 2（周二）：实现Engine Adapter（2.5h）
- **练习**:
  - 实现统一的推理引擎接口（抽象基类）
  - 实现vLLM适配器
  - 实现OpenAI API适配器
  - 实现TensorRT-LLM适配器（如可用）
  - 编写适配器的单元测试
- **重点掌握**: 适配器模式的实际应用

#### Day 3（周三）：实现功能测试模块（2.5h）
- **练习**:
  - 实现测试用例生成器:
    - 基本推理测试用例
    - 边界条件测试用例
    - 参数组合测试用例
  - 实现断言工具:
    - 输出格式验证
    - Token数量验证
    - 响应时间验证
    - 流式输出验证
  - 编写功能测试套件
- **重点掌握**: 测试用例的自动生成，断言设计

#### Day 4（周四）：实现性能测试模块（2.5h）
- **练习**:
  - 实现性能测试Runner:
    - 可配置的并发数和请求速率
    - 预热阶段
    - 实时指标收集（TTFT, TPOT, Throughput）
    - 异步请求发送
  - 实现统计分析模块:
    - P50/P90/P95/P99延迟计算
    - 吞吐量计算
    - 数据可视化（matplotlib/plotly）
  - 编写性能测试配置模板
- **重点掌握**: 高并发测试的实现，统计指标计算

#### Day 5（周五）：实现报告生成与CI集成（2.5h）
- **练习**:
  - 实现测试报告生成器:
    - HTML报告
    - JSON/CSV数据导出
    - 性能趋势图
    - 对比报告
  - CI/CD集成:
    - GitHub Actions配置
    - 自动运行测试
    - 结果归档
  - 编写完整的README文档
- **重点掌握**: 测试报告的自动化生成

#### Day 6-7（周末）：框架完善与代码整理（每天5h）
- **练习**:
  - 完善测试框架:
    1. 添加精度测试模块
    2. 添加稳定性测试模块
    3. 完善错误处理和日志记录
    4. 编写使用文档
    5. 添加示例测试场景
  - 在真实环境中验证框架的可用性
  - 代码审查和重构
  - 推送到GitHub作为面试作品
- **重点掌握**: 代码质量和工程规范

---

## 第六阶段: 综合实战 + 面试准备（Week 15-16）

### Week 15: 综合项目与查漏补缺（每天3小时）

#### Day 1-2: 简历项目整理
- 整理所有项目到GitHub
- 编写项目README和文档
- 准备Demo和演示材料
- 总结项目中的技术亮点

#### Day 3-4: 知识点查漏补缺
- 回顾所有笔记，标记不确定的知识点
- 针对薄弱环节补充学习
- 绘制完整的知识体系图
- 总结核心概念的一句话解释

#### Day 5-7: 模拟面试练习
- 技术问题模拟
- 项目经验阐述练习
- 代码题练习（Python/C++）
- 系统设计题练习

---

### Week 16: 面试冲刺（每天3小时）

#### Day 1-2: 面试题集中复习
- 复习下方所有面试题
- 对照答案查漏补缺
- 准备自我介绍（中英文）
- 准备项目经验描述（STAR法则）

#### Day 3-4: 实战模拟
- 完整模拟面试流程
- 时间控制练习
- 白板编码练习
- 系统设计题练习

#### Day 5-7: 最终准备
- 复习核心知识点
- 调整心态
- 准备面试提问清单
- 最终检查简历和作品

---

## 面试题库（含详细答案）

### 一、Python编程

#### Q1: Python的GIL是什么？对多线程有什么影响？
**答案**:
GIL (Global Interpreter Lock) 是CPython解释器中的一个互斥锁，它确保同一时刻只有一个线程执行Python字节码。

**影响**:
- CPU密集型任务：多线程无法利用多核，因为GIL阻止了真正的并行执行。此时应使用 `multiprocessing`。
- IO密集型任务：线程在等待IO时会释放GIL，所以多线程仍然有效。
- 解决方案：
  - CPU密集型 → `multiprocessing` 或 C扩展
  - IO密集型 → `threading` 或 `asyncio`
  - 使用其他解释器（如Jython, PyPy）

#### Q2: 解释Python的装饰器原理
**答案**:
装饰器本质是一个高阶函数，它接受一个函数作为参数，返回一个新的函数。

```python
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.2f}s")
        return result
    return wrapper

@timer  # 等价于 my_func = timer(my_func)
def my_func():
    pass
```

`@functools.wraps(func)` 的作用是保留原函数的 `__name__`、`__doc__` 等元信息。

#### Q3: `pytest` 中 fixture 的 scope 有哪些？各自的生命周期是什么？
**答案**:
- `function`（默认）：每个测试函数执行前/后创建/销毁
- `class`：每个测试类执行前/后
- `module`：每个测试模块（.py文件）执行前/后
- `package`：每个测试包执行前/后
- `session`：整个测试会话只创建一次

```python
@pytest.fixture(scope="session")
def db_connection():
    conn = create_connection()
    yield conn  # yield之前是setup, 之后是teardown
    conn.close()
```

#### Q4: Python中 `__init__` 和 `__new__` 的区别？
**答案**:
- `__new__`: 类方法，负责创建实例（分配内存），在 `__init__` 之前调用，返回实例对象
- `__init__`: 实例方法，负责初始化实例（设置属性），不返回值

`__new__` 常用于：单例模式、不可变类型的子类化、元编程

```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

### 二、C/C++

#### Q5: C++中智能指针有哪些？各自的使用场景？
**答案**:
- `unique_ptr`: 独占所有权，不可拷贝只能移动。适用于明确单一拥有者的场景。
- `shared_ptr`: 共享所有权，引用计数管理。适用于多个对象共享同一资源。
- `weak_ptr`: 弱引用，不增加引用计数。适用于解决 `shared_ptr` 的循环引用问题。

```cpp
auto up = std::make_unique<int>(42);  // 独占
auto sp = std::make_shared<int>(42);  // 共享, 引用计数=1
std::weak_ptr<int> wp = sp;           // 弱引用, 不影响引用计数
```

#### Q6: 什么是虚函数？虚函数表(vtable)的工作原理？
**答案**:
虚函数允许通过基类指针调用派生类的重写方法（运行时多态）。

**vtable原理**:
- 每个含虚函数的类有一个vtable（虚函数表），存储虚函数指针
- 每个对象有一个vptr（虚表指针），指向类的vtable
- 调用虚函数时，通过 vptr → vtable → 函数指针 找到实际要调用的函数
- 这就是为什么虚函数调用比普通函数调用稍慢（间接寻址）

#### Q7: `malloc/free` 和 `new/delete` 的区别？
**答案**:
| 特性 | malloc/free | new/delete |
|------|-----------|------------|
| 语言 | C函数 | C++运算符 |
| 类型安全 | 返回void*，需强转 | 返回正确类型 |
| 构造/析构 | 不调用 | 自动调用 |
| 错误处理 | 返回NULL | 抛出异常 |
| 大小指定 | 手动指定字节数 | 自动计算 |

---

### 三、GPU与CUDA

#### Q8: GPU和CPU的架构有什么主要区别？为什么GPU适合深度学习？
**答案**:
| 特性 | CPU | GPU |
|------|-----|-----|
| 核心数 | 少量强核心(8-64) | 大量弱核心(数千) |
| 设计目标 | 低延迟 | 高吞吐 |
| 缓存 | 大缓存 | 小缓存 |
| 控制逻辑 | 复杂(分支预测等) | 简单 |
| 适合任务 | 串行、复杂逻辑 | 大规模并行计算 |

GPU适合深度学习因为:
1. 矩阵运算是高度并行的（同一操作应用到大量数据）
2. Tensor Core专门优化矩阵乘加运算
3. 高显存带宽满足数据密集型计算需求

#### Q9: 什么是CUDA中的Warp？Warp Divergence是什么问题？
**答案**:
**Warp**: GPU执行的最小调度单位，包含32个线程，这32个线程同时执行相同的指令（SIMT）。

**Warp Divergence**: 当Warp中的线程遇到条件分支（if/else），不同线程走不同分支时，GPU必须串行执行两个分支（先执行if分支，不满足条件的线程idle；再执行else分支），导致性能下降。

```cuda
// 会导致Warp Divergence
if (threadIdx.x % 2 == 0) {
    // 偶数线程执行
} else {
    // 奇数线程执行
}
```

优化方法：尽量让同一Warp内的线程走相同分支。

#### Q10: 解释GPU的内存层次结构
**答案**:
从快到慢、从小到大:
1. **Register（寄存器）**: 最快，每个线程私有，~1 cycle
2. **Shared Memory**: SM内线程共享，~5 cycles，用户可控，通常48-164KB
3. **L1 Cache**: SM级，与Shared Memory共享物理空间
4. **L2 Cache**: 所有SM共享，~200 cycles
5. **Global Memory (HBM)**: 最大最慢，~400-600 cycles，几十GB

**优化原则**: 尽可能将频繁访问的数据放在更快的内存层级。

#### Q11: 什么是Tensor Core？它与CUDA Core有什么区别？
**答案**:
- **CUDA Core**: 标量运算单元，每个时钟周期执行一个浮点乘加(FMA)
- **Tensor Core**: 矩阵运算单元，每个时钟周期执行一个4×4矩阵乘加(D = A×B + C)

**关键区别**:
- Tensor Core专为矩阵运算设计，比CUDA Core快几倍到十几倍
- Tensor Core支持混合精度（如FP16输入、FP32累加）
- A100: 第3代Tensor Core，支持TF32, FP16, BF16, INT8, INT4
- H100: 第4代Tensor Core，新增FP8支持

深度学习中的矩阵乘法（GEMM）主要由Tensor Core加速。

---

### 四、LLM推理基础

#### Q12: 解释LLM推理中的Prefill和Decode阶段
**答案**:
LLM推理分为两个阶段：

**Prefill阶段（预填充）**:
- 处理整个输入prompt
- 并行计算所有输入token的KV值
- 计算密集型（Compute-bound）
- 生成第一个输出token
- 决定TTFT指标

**Decode阶段（解码）**:
- 逐个生成输出token（自回归）
- 每次只处理一个新token
- 利用KV Cache避免重复计算
- 内存密集型（Memory-bound），因为每个token的计算量小但需要读取大量KV Cache
- 决定TPOT指标

**类比**: Prefill像是"阅读理解"（一次读完），Decode像是"逐字写作"（一个一个写）。

#### Q13: 什么是KV Cache？为什么需要它？
**答案**:
**KV Cache**: 缓存Transformer中Attention层的Key和Value张量，避免在自回归解码时重复计算。

**为什么需要**:
- 在自回归解码中，每生成一个新token都需要与之前所有token做Attention
- 不用Cache：每步需重新计算所有token的K和V，复杂度O(n²)
- 用Cache：只需计算新token的K和V，追加到Cache中，复杂度O(n)

**KV Cache大小计算**:
```
KV Cache Size = 2 × num_layers × num_heads × head_dim × seq_len × batch_size × bytes_per_element
```

以LLaMA-7B (FP16)为例:
- 2 × 32层 × 32头 × 128维 × 2048长度 × 2字节 ≈ 1GB（每条序列）

**KV Cache是LLM推理的主要显存消耗者**，也是各种优化技术（PagedAttention, GQA, 量化等）的重要优化目标。

#### Q14: 解释TTFT、TPOT和Throughput的含义及其重要性
**答案**:
- **TTFT (Time To First Token)**: 从发送请求到收到第一个token的时间
  - 反映Prefill阶段性能
  - 影响用户感知的"响应速度"
  - 主要受输入长度和模型大小影响
  
- **TPOT (Time Per Output Token)**: 生成每个输出token的平均时间
  - 反映Decode阶段性能
  - 影响整体生成速度和用户阅读体验
  - 人类阅读速度约3-4 tokens/s，TPOT < 250ms通常可接受
  
- **Throughput (吞吐量)**: 系统每秒处理的token总数
  - 反映系统的服务能力
  - 在批量处理和多用户场景中更重要
  - 通常以 tokens/s 或 requests/s 衡量

**三者的关系**: 优化TTFT和TPOT通常是为了单个用户体验，优化Throughput是为了系统整体效率。有时需要权衡（如增大batch提高Throughput但可能增加TTFT）。

---

### 五、推理引擎

#### Q15: vLLM的核心创新是什么？解释PagedAttention的原理
**答案**:
**核心创新**: PagedAttention — 受操作系统虚拟内存管理启发的KV Cache管理机制。

**问题背景**:
传统KV Cache管理预分配连续内存空间，导致:
1. **内存碎片化**: 不同请求的KV Cache大小不同，释放后产生碎片
2. **过度预留**: 必须按最大长度预分配，大部分空间浪费
3. **无法共享**: 相同前缀的KV Cache无法在请求间共享

**PagedAttention方案**:
1. 将KV Cache分割为固定大小的Block（类似OS的页）
2. 使用Block Table（类似页表）维护逻辑Block到物理Block的映射
3. 物理Block不需要连续，按需分配和释放
4. 支持Block共享（如相同System Prompt的多个请求共享KV Cache）

**效果**: 将KV Cache的内存利用率从传统方法的20-40%提升到接近100%，从而在同样的GPU显存下可以服务更多并发请求。

#### Q16: 什么是Continuous Batching？与Static Batching有什么区别？
**答案**:

**Static Batching（静态批处理）**:
- 一个batch中的所有请求必须同时开始、同时结束
- 短请求完成后必须等待长请求，GPU空闲浪费
- 新请求必须等当前batch全部完成才能处理

**Continuous Batching（连续批处理）**:
- Iteration-level调度：每次forward pass后重新决定batch组成
- 已完成的请求立即移出，空位让给新请求
- 不同请求可以处于不同阶段（Prefill/Decode混合）

**优势**: 大幅提高GPU利用率和整体吞吐量。论文表明，Continuous Batching可以带来2-8倍的吞吐提升。

**举例**:
```
Static:    [A——][B————][C——]  → B完成前，A和C的GPU空闲
Continuous: [A,B,C] → A完成 → [B,C,D] → C完成 → [B,D,E] → ...
```

#### Q17: vLLM和TensorRT-LLM各自的优缺点是什么？如何选择？
**答案**:

| 特性 | vLLM | TensorRT-LLM |
|------|------|-------------|
| **性能** | 很好 | 通常更好（NVIDIA深度优化） |
| **易用性** | 简单，pip install | 复杂，需要构建Engine |
| **灵活性** | 高，支持模型广泛 | 较低，需要显式支持 |
| **硬件要求** | NVIDIA GPU | NVIDIA GPU（更深度绑定） |
| **社区** | 活跃的开源社区 | NVIDIA官方维护 |
| **部署** | 简单 | 需要Triton等额外组件 |
| **更新速度** | 快（社区驱动） | 相对慢（企业节奏） |

**选择建议**:
- 快速原型/研究：vLLM（简单易用）
- 生产环境极致性能：TensorRT-LLM（深度优化）
- 非NVIDIA硬件：考虑其他框架
- 需要最新模型支持：vLLM（社区更新快）

---

### 六、推理优化技术

#### Q18: 解释FlashAttention的原理和优势
**答案**:
**核心问题**: 标准Attention需要实例化n×n的注意力矩阵，导致大量HBM读写。

**FlashAttention的解决方案**: IO-Aware的分块(Tiling)计算

**原理**:
1. 将Q, K, V矩阵分成小块(tile)
2. 每次只将一小块加载到GPU的SRAM（快速内存）
3. 在SRAM中计算局部Attention
4. 使用Online Softmax算法，在不需要完整注意力矩阵的情况下，正确计算全局Softmax
5. 将结果写回HBM

**优势**:
- **内存效率**: O(n)内存而非O(n²)
- **速度**: 减少HBM读写次数，通常2-4倍加速
- **精确**: 结果与标准Attention完全相同（非近似）

**FlashAttention-2的改进**: 更好的线程块间并行和工作划分。

#### Q19: 解释AWQ和GPTQ量化的原理和区别
**答案**:

**GPTQ**:
- 基于OBQ（Optimal Brain Quantization）的改进
- 逐层量化：对每一层的权重进行量化
- 使用Hessian矩阵的逆来最小化量化误差
- 对已量化的权重误差进行补偿（更新未量化的权重）
- 需要校准数据集

**AWQ (Activation-Aware Weight Quantization)**:
- 核心观察：权重的重要性与输入激活值相关
- 1%的"显著通道"对模型输出影响巨大
- 关键创新：不是直接保留显著权重不量化，而是通过对权重进行缩放(scaling)来保护重要通道
- 缩放系数由激活值分布决定
- 更快的量化速度，更好的泛化性

**对比**:
| 维度 | GPTQ | AWQ |
|------|------|-----|
| 量化速度 | 较慢 | 较快 |
| 精度保持 | 好 | 略好 |
| 校准数据依赖 | 较强 | 较弱 |
| 泛化性 | 一般 | 更好 |
| 原理 | Hessian矩阵优化 | 激活感知缩放 |

#### Q20: 什么是Speculative Decoding？为什么它能加速推理？
**答案**:
**核心思想**: 用一个小的Draft Model快速"猜测"多个token，然后用大的Target Model一次性并行验证。

**流程**:
1. Draft Model（小模型）自回归生成γ个候选token
2. Target Model一次forward pass同时计算这γ+1个位置的概率分布
3. 从左到右逐个验证：如果Draft token的概率符合Target分布则接受，否则拒绝并重新采样
4. 接受的token直接使用，第一个拒绝位置重新采样后的token也作为有效输出

**为什么能加速**:
- 自回归解码是Memory-bound的（GPU计算能力没有充分利用）
- Draft Model生成很快（模型小）
- Target Model验证γ个token的时间 ≈ 生成1个token的时间（额外计算可被GPU并行消化）
- 如果接受率高，相当于一步生成多个token

**关键保证**: 数学上可以证明输出分布与直接使用Target Model完全一致（无损加速）。

**加速比**: 取决于acceptance rate α，理论加速比为 1/(1-α)。通常在1.5x-3x之间。

#### Q21: 解释Tensor Parallelism和Pipeline Parallelism
**答案**:

**Tensor Parallelism (TP)**:
- 将单个层的权重矩阵切分到多个GPU
- 每个GPU处理权重的一部分
- 需要All-Reduce通信来汇总结果
- 适合层间通信延迟低的场景（同一节点内）
- 例：4个GPU各持有25%的权重

**Pipeline Parallelism (PP)**:
- 将不同的层分配到不同的GPU
- 形成流水线：GPU1处理第1-8层 → GPU2处理第9-16层 → ...
- 需要点对点通信传递中间激活
- 有Pipeline Bubble（前几个和最后几个micro-batch时GPU空闲）

**选择**:
- 同一节点内（NVLink高带宽）→ 优先TP
- 跨节点（网络带宽有限）→ PP更合适
- 实际中常混合使用：节点内TP + 节点间PP

---

### 七、测试与QA

#### Q22: 如何测试一个LLM推理引擎的正确性？
**答案**:

**分层测试策略**:

1. **算子级测试**:
   - 对比PyTorch原始实现的输出
   - 数值精度验证（absolute/relative error threshold）
   - 边界条件测试

2. **模型级测试**:
   - 对比Hugging Face原始模型输出
   - 设置相同随机种子，验证输出一致性
   - 用Perplexity衡量模型质量

3. **API级测试**:
   - OpenAI API兼容性测试
   - 参数功能测试（temperature, top_p等）
   - 流式输出正确性
   - 错误处理测试

4. **系统级测试**:
   - 并发请求正确性
   - 长时间运行正确性
   - 不同配置下的正确性

**关键验证点**:
- 非确定性输出的验证: 使用种子固定随机性，或统计方法验证分布
- 量化模型: 允许一定的精度损失，设定阈值

#### Q23: 如何设计LLM推理的性能测试方案？
**答案**:

**测试方案设计**:

1. **测试目标定义**:
   - 明确要测量的指标：TTFT, TPOT, Throughput, GPU利用率
   - 定义SLA要求：如TTFT P99 < 500ms

2. **测试场景设计**:
   - 不同输入长度（128, 512, 1024, 2048, 4096 tokens）
   - 不同输出长度
   - 不同并发数（1, 10, 50, 100, 200）
   - 不同请求模式（稳定速率, 突发, 递增）

3. **测试数据准备**:
   - 真实场景的输入分布
   - ShareGPT数据集（常用基准）
   - 合成数据（控制变量）

4. **测试执行**:
   - 充分预热（至少30秒）
   - 每个场景运行足够长时间（至少5分钟）
   - 多次运行取统计值

5. **结果分析**:
   - 延迟分布（P50/P90/P95/P99/P999）
   - 吞吐量随并发数的变化曲线
   - GPU利用率和显存使用
   - 性能拐点分析

#### Q24: 如何测试量化模型的精度？
**答案**:

**多维度评估**:

1. **Perplexity评估**:
   - 使用标准数据集（如WikiText-2, C4）
   - 对比原始模型和量化模型的Perplexity
   - 设定可接受的精度损失阈值（如PPL增加<1%）

2. **任务级评估**:
   - 选择代表性的下游任务
   - 常用benchmark: MMLU, HumanEval, GSM8K, MT-Bench
   - 对比原始模型和量化模型的准确率

3. **输出对比**:
   - 同一输入下，原始模型和量化模型的输出相似度
   - ROUGE/BLEU分数对比
   - 人工评估（采样评估）

4. **边界测试**:
   - 测试量化模型在极端输入下的表现
   - 测试不同长度输入的精度变化
   - 测试不同语言/领域的精度差异

#### Q25: 白盒测试和黑盒测试在AI系统中如何应用？
**答案**:

**白盒测试（需要了解内部实现）**:
- **算子正确性测试**: 了解Attention实现细节，针对性测试
- **代码路径覆盖**: 确保不同条件分支都被测试（如不同batch size、不同序列长度走不同代码路径）
- **内存管理测试**: 了解PagedAttention实现，测试Block分配和回收
- **调度器测试**: 了解Continuous Batching逻辑，测试抢占、排队等
- **数值精度分析**: 了解计算图，定位精度损失的具体位置

**黑盒测试（不需要了解内部实现）**:
- **API功能测试**: 按接口规范测试输入输出
- **性能基准测试**: 只关心外部可观测指标
- **兼容性测试**: 不同环境下的行为一致性
- **端到端测试**: 完整用户场景测试

**AI系统特有**: 
- 模型本身是"黑盒"，但推理系统的代码是可白盒测试的
- 两种方法需要结合使用

---

### 八、综合与系统设计

#### Q26: 如果让你从零搭建一个LLM推理服务的测试体系，你会怎么做？
**答案**:

**步骤**:

1. **需求分析**（第1周）:
   - 明确被测系统的架构和功能
   - 明确质量要求和SLA
   - 确定测试范围和优先级

2. **测试策略制定**（第2周）:
   - 制定分层测试策略
   - 选择测试工具和框架
   - 定义测试入口/出口准则

3. **基础设施搭建**（第3-4周）:
   - 搭建测试环境（GPU服务器、CI/CD）
   - 开发测试框架（适配器模式支持多引擎）
   - 配置监控和报告系统

4. **测试开发**（第5-8周）:
   - 功能测试用例开发
   - 性能测试脚本开发
   - 精度验证工具开发
   - 稳定性测试工具开发

5. **执行与优化**（持续）:
   - 集成到CI/CD流水线
   - 定期执行回归测试
   - 持续优化测试效率和覆盖率

#### Q27: 描述你遇到过的最复杂的bug及其解决过程
**提示**：用STAR法则准备，结合你的实际经验。即使是Java测试平台的经验也可以，重点体现:
- **S**ituation: 背景
- **T**ask: 你的任务
- **A**ction: 你的分析和解决步骤
- **R**esult: 结果和收获

#### Q28: 如何看待AI系统测试与传统软件测试的区别？
**答案**:

**核心区别**:
1. **确定性**: 传统软件输入→输出是确定的；AI系统可能有随机性
2. **正确性定义**: 传统软件有明确的对错；AI系统的"正确"是概率性的
3. **数据依赖**: 传统软件行为由代码决定；AI系统行为同时受模型和数据影响
4. **性能维度**: 除了传统的延迟/吞吐，还有精度、GPU利用率等AI特有指标
5. **回归检测**: 模型更新可能导致行为变化，需要更全面的回归测试

**测试策略调整**:
- 增加统计测试方法（多次运行取统计量）
- 引入AI特有的测试指标（Perplexity, BLEU等）
- 更重视性能和资源测试
- 需要理解底层硬件（GPU）

---

### 九、Linux与工程实践

#### Q29: 常用的Linux性能分析命令有哪些？
**答案**:

```bash
# CPU分析
top / htop                    # 进程级CPU使用率
mpstat -P ALL 1              # 每个CPU核心使用率
perf top                     # 内核级热点分析

# 内存分析
free -h                      # 内存概览
vmstat 1                     # 虚拟内存统计
cat /proc/meminfo            # 详细内存信息

# IO分析
iostat -x 1                  # 磁盘IO统计
iotop                        # 进程级IO

# 网络分析
ss -tunlp                    # 网络连接
iftop                        # 网络流量

# GPU分析
nvidia-smi                   # GPU状态
nvidia-smi dmon              # GPU监控
nvtop                        # GPU版的htop

# 进程分析
strace -p PID                # 系统调用跟踪
lsof -p PID                  # 打开的文件
pmap PID                     # 进程内存映射

# 日志分析
journalctl -u service -f     # 查看服务日志
dmesg | tail                 # 内核日志
grep -rn "ERROR" /var/log/   # 搜索错误日志
```

#### Q30: 如何排查一个推理服务的性能问题？
**答案**:

**排查步骤**:

1. **明确问题**: 延迟高？吞吐低？OOM？
2. **系统级检查**:
   ```bash
   nvidia-smi                    # GPU利用率/显存
   top -p <pid>                  # CPU使用
   free -h                       # 系统内存
   ```
3. **应用级检查**:
   - 查看推理服务日志
   - 检查请求队列长度
   - 检查Prometheus指标
4. **定位瓶颈**:
   - GPU利用率低 → Batch太小/数据传输瓶颈
   - GPU利用率高但吞吐低 → 计算效率问题
   - 显存不足 → KV Cache配置/模型太大
   - CPU瓶颈 → Tokenization/预处理
5. **解决**:
   - 调整Batch配置
   - 优化数据加载
   - 启用量化/优化
   - 硬件升级

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

---

## 学习资源汇总

### 必读论文
1. "Attention Is All You Need" (Transformer)
2. "Efficient Memory Management for LLM Serving with PagedAttention" (vLLM)
3. "FlashAttention: Fast and Memory-Efficient Exact Attention"
4. "Fast Inference from Transformers via Speculative Decoding"
5. "GPTQ: Accurate Post-Training Quantization for Generative Pre-Trained Transformers"
6. "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
7. "Orca: A Distributed Serving System for Transformer-Based Generative Models"

### 推荐书籍
1. 《Fluent Python》 - Python进阶
2. 《C++ Primer》 - C++基础
3. 《Programming Massively Parallel Processors》 - CUDA编程
4. 《Python Testing with pytest》 - 测试

### 在线课程
1. 吴恩达 Machine Learning/Deep Learning Specialization (Coursera)
2. NVIDIA Deep Learning Institute (DLI) 课程
3. Hugging Face NLP Course
4. FastAI Course

### 重要GitHub仓库
1. vLLM: https://github.com/vllm-project/vllm
2. TensorRT-LLM: https://github.com/NVIDIA/TensorRT-LLM
3. llama.cpp: https://github.com/ggerganov/llama.cpp
4. SGLang: https://github.com/sgl-project/sglang
5. AutoGPTQ: https://github.com/AutoGPTQ/AutoGPTQ
6. AutoAWQ: https://github.com/casper-hansen/AutoAWQ

### 技术博客
1. Jay Alammar's Blog (Transformer可视化)
2. Lil'Log (ML概念讲解)
3. NVIDIA Developer Blog
4. vLLM Blog
5. Hugging Face Blog

---

## 每周学习时间总结

| 周次 | 工作日(h/天) | 周末(h/天) | 周总计(h) |
|------|------------|-----------|----------|
| Week 1-12 | 2.5 | 5 | 22.5 |
| Week 13-14 | 2.5 | 5 | 22.5 |
| Week 15-16 | 3 | 5 | 25 |
| **总计** | | | **~370小时** |

---

## 学习建议

1. **每日记录**: 用笔记工具(Notion/Obsidian)记录每天的学习内容和心得
2. **费曼学习法**: 学完一个概念后，尝试用自己的话解释给别人听
3. **动手实践**: 每个知识点都要写代码实践，不要只看不做
4. **GitHub作品集**: 所有项目代码推送到GitHub，面试时可以展示
5. **社区参与**: 关注vLLM/TensorRT-LLM的GitHub Issues和Discussions
6. **定期回顾**: 每周日花1小时回顾本周所学，整理笔记
7. **模拟面试**: 从Week 12开始，每周模拟面试1次
8. **利用现有优势**: 你的Linux经验和测试经验是加分项，面试中要突出

---

> **最后提醒**: 这个学习计划内容量较大，请根据实际情况灵活调整节奏。核心优先级是:
> 1. **最高优先级**: LLM推理基础(KV Cache, Prefill/Decode) + vLLM(PagedAttention, Continuous Batching) + 推理优化(FlashAttention, 量化, Speculative Decoding)
> 2. **高优先级**: Python进阶 + GPU/CUDA基础 + 测试方法论
> 3. **中优先级**: C/C++ + TensorRT-LLM + 分布式推理
> 4. **加分项**: 完整项目作品 + CUDA编程实战

祝学习顺利，面试成功！
