> 职位描述
Responsibilities:
• Improve software product specifications for Artificial Intelligence/Deep Learning product software from quality assurance perspective.
• Define software testing strategy, test plan and develop white-box, API & system-level tests for various software components/systems.
• Perform tests/scripts to validate software functionality, compatibility, and performance etc.
• Identify issues through testing & profiling of the target software components or complex systems.
• Collect and organize testing results and review with development teams, marketing team, architect teams, etc.
• Improve and enhance software QA strategies, processes, tools.
 
Qualifications:
• Bachelor’s degree or above, in computer science, software engineering, computer engineering
• 5+ years of professional experience in software testing & automation development.
• Proficient in C/C++/Python programming languages, and familiar Linux commands.
• Familiar with mainstream LLM inference engines (such as vLLM,tensorRT), and understand the basic principles of common inference
optimization techniques, such as FlashAttention, PageAttention, Continuous Batching, Speculative Decoding, etc.
• Have knowledge of AI model inference optimization experience, and be familiar with common acceleration techniques, such as pruning,
quantization (AWQ, GPTQ, etc.), distributed inference, etc.
• Familiar with the GPU hardware architectures. Those with CUDA development and optimization experience will be preferred.[10:44 AM]职位描
述
Responsibilities:
• Improve software product specifications for Artificial Intelligence/Deep Learning product software from quality assurance perspective.
• Define software testing strategy, test plan and develop white-box, API & system-level tests for various software components/systems.
• Perform tests/scripts to validate software functionality, compatibility, and performance etc.
• Identify issues through testing & profiling of the target software components or complex systems.
• Collect and organize testing results and review with development teams, marketing team, architect teams, etc.
• Improve and enhance software QA strategies, processes, tools.

Qualifications:
• Bachelor’s degree or above, in computer science, software engineering, computer engineering
• 5+ years of professional experience in software testing & automation development.
• Proficient in C/C++/Python programming languages, and familiar Linux commands.
• Familiar with mainstream LLM inference engines (such as vLLM,tensorRT), and understand the basic principles of common inference
optimization techniques, such as FlashAttention, PageAttention, Continuous Batching, Speculative Decoding, etc.
• Have knowledge of AI model inference optimization experience, and be familiar with common acceleration techniques, such as pruning,
quantization (AWQ, GPTQ, etc.), distributed inference, etc.
• Familiar with the GPU hardware architectures. Those with CUDA development and optimization experience will be preferred.帮我列出学习计
划，具体到每天几个小时，细致的学习点，我没有ai相关的知识

AI/Deep Learning QA 工程师学习计划

│ 假设你有编程基础（C/C++/Python），但零 AI 背景。计划共 16 周，每天 3-4 小时（工作日），周末可选加练。

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

第一阶段：AI/深度学习基础（第 1-3 周）

第 1 周：机器学习核心概念（每天 3 小时）

天     时长  学习内容
Day 1  3h    什么是机器学习、监督/无监督/强化学习分类；损失函数、梯度下降概念
Day 2  3h    线性回归、逻辑回归原理；用 Python + scikit-learn 跑通第一个模型
Day 3  3h    过拟合/欠拟合、正则化、交叉验证；训练集/验证集/测试集划分
Day 4  3h    神经网络基础：感知机、激活函数（ReLU/Sigmoid/Softmax）、前向传播
Day 5  3h    反向传播算法原理；用 NumPy 手写一个两层神经网络

资源： Andrew Ng《Machine Learning》课程（Coursera）前 4 周内容 / 3Blue1Brown 神经网络系列视频

第 2 周：深度学习基础（每天 3 小时）

天     时长  学习内容
Day 1  3h    PyTorch 安装与基础：Tensor 操作、自动求导（autograd）
Day 2  3h    用 PyTorch 搭建全连接网络，完成 MNIST 手写数字识别
Day 3  3h    CNN 卷积神经网络：卷积层、池化层、特征图概念
Day 4  3h    RNN/LSTM 基础概念；序列数据处理的直觉理解
Day 5  3h    模型训练流程：数据加载(DataLoader)、训练循环、模型保存/加载

资源： PyTorch 官方教程（pytorch.org/tutorials）、李宏毅深度学习课程

第 3 周：NLP 与 Transformer 架构（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  NLP 基础：分词(Tokenization)、词嵌入(Word Embedding)、Word2Vec
Day 2  3.5h  Attention 注意力机制原理：Query/Key/Value、注意力权重计算
Day 3  3.5h  Transformer 架构精读：Multi-Head Attention、位置编码、Layer Norm、FFN
Day 4  3.5h  阅读论文"Attention Is All You Need"；对照代码理解 Encoder-Decoder 结构
Day 5  3.5h  BERT vs GPT 区别；自回归生成（Autoregressive）原理；Token 生成过程

资源： Jay Alammar 的图解 Transformer 博客、Andrej Karpathy 的 "Let's build GPT" 视频

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

第二阶段：大语言模型（LLM）原理（第 4-6 周）

第 4 周：LLM 基础（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  GPT 系列演进：GPT-1/2/3/4 架构差异；参数量与能力关系
Day 2  3.5h  LLaMA / Mistral / Qwen 等开源模型结构；HuggingFace 模型下载与加载
Day 3  3.5h  Tokenizer 深入：BPE/SentencePiece/tiktoken；词表大小对性能的影响
Day 4  3.5h  推理过程详解：Prefill 阶段 vs Decode 阶段；KV Cache 原理与作用
Day 5  3.5h  采样策略：Temperature、Top-K、Top-P；用 HuggingFace transformers 库做推理

资源： HuggingFace NLP Course、各模型论文的摘要与架构图

第 5 周：LLM 推理优化技术（一）（每天 4 小时）⭐ 重点

天     时长  学习内容
Day 1  4h    KV Cache 深入：为什么需要缓存、内存占用计算、缓存淘汰策略
Day 2  4h    FlashAttention：标准 Attention 的内存瓶颈；IO-aware 算法；tiling 技术；FlashAttention v1/v2 区别
Day 3  4h    PagedAttention：虚拟内存思想在 KV Cache 管理中的应用；内存碎片问题的解决
Day 4  4h    Continuous Batching（连续批处理）：静态 batching vs 动态 batching；iteration-level scheduling
Day 5  4h    Speculative Decoding（投机解码）：draft model + verify 的流程；加速原理；接受/拒绝策略

资源： FlashAttention 论文、vLLM 论文（PagedAttention）、各技术的博客解读

第 6 周：LLM 推理优化技术（二）（每天 4 小时）⭐ 重点

天     时长  学习内容
Day 1  4h    量化基础：FP32/FP16/BF16/INT8/INT4 数据类型；量化的精度-速度权衡
Day 2  4h    量化方法详解：PTQ vs QAT；AWQ（Activation-aware Weight Quantization）原理
Day 3  4h    GPTQ 量化：逐层量化策略、Hessian 矩阵近似；AWQ vs GPTQ 对比
Day 4  4h    模型剪枝（Pruning）：非结构化剪枝 vs 结构化剪枝；稀疏性与加速的关系
Day 5  4h    分布式推理：Tensor Parallelism vs Pipeline Parallelism；多 GPU 推理的通信开销

资源： AWQ/GPTQ 论文、NVIDIA 量化白皮书、分布式计算相关博客

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

第三阶段：GPU 与 CUDA（第 7-9 周）

第 7 周：GPU 硬件架构（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  GPU vs CPU 架构对比；SIMT 执行模型；SM（Streaming Multiprocessor）结构
Day 2  3.5h  GPU 内存层次：全局内存(Global)、共享内存(Shared)、寄存器(Register)、L1/L2 Cache
Day 3  3.5h  内存带宽与计算强度（Arithmetic Intensity）；Roofline Model 性能分析
Day 4  3.5h  NVIDIA GPU 架构演进：Volta → Turing → Ampere → Hopper；Tensor Core 的作用
Day 5  3.5h  nvidia-smi 命令详解；GPU 利用率、显存占用、功耗监控

资源： NVIDIA CUDA C Programming Guide 前几章、GPU 架构白皮书

第 8 周：CUDA 编程入门（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  CUDA 编程模型：Grid/Block/Thread 层次；kernel 函数语法
Day 2  3.5h  编写第一个 CUDA 程序：向量加法；编译与运行（nvcc）
Day 3  3.5h  内存管理：cudaMalloc/cudaMemcpy/cudaFree；Host 与 Device 数据传输
Day 4  3.5h  共享内存使用：矩阵乘法优化实例；bank conflict 概念
Day 5  3.5h  线程同步：__syncthreads()；Warp 概念与 Warp Divergence

资源： NVIDIA CUDA Samples、"Professional CUDA C Programming" 书

第 9 周：CUDA 性能优化与工具（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  性能优化：内存合并访问(Coalesced Access)、occupancy 优化
Day 2  3.5h  CUDA 流(Streams) 与异步执行；多流并发的时间线分析
Day 3  3.5h  Nsight Systems 使用：Timeline 视图、GPU kernel 分析
Day 4  3.5h  Nsight Compute 使用：单个 kernel 的详细性能指标、瓶颈定位
Day 5  3.5h  cuBLAS/cuDNN 库概览；GEMM 操作在深度学习中的重要性

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

第四阶段：推理引擎实战（第 10-12 周）

第 10 周：vLLM 深入（每天 4 小时）⭐ 重点

天     时长  学习内容
Day 1  4h    vLLM 安装与快速使用；离线推理 vs API Server 模式
Day 2  4h    vLLM 架构源码阅读：Scheduler、BlockManager、Worker 模块
Day 3  4h    PagedAttention 在 vLLM 中的具体实现；Block 分配与回收逻辑
Day 4  4h    vLLM 性能测试：throughput/latency 测量；不同参数（tp, batch_size）对比
Day 5  4h    vLLM 支持的量化格式（AWQ/GPTQ/FP8）；加载量化模型实践

资源： vLLM GitHub 仓库、vLLM 官方文档

第 11 周：TensorRT / TensorRT-LLM（每天 4 小时）⭐ 重点

天     时长  学习内容
Day 1  4h    TensorRT 基础：模型优化流程（Parse → Optimize → Build Engine → Runtime）
Day 2  4h    TensorRT 优化原理：层融合(Layer Fusion)、精度校准(Calibration)、kernel 自动调优
Day 3  4h    TensorRT-LLM 安装与使用；将 HuggingFace 模型转换为 TRT-LLM 格式
Day 4  4h    TensorRT-LLM 特性：In-flight Batching、Paged KV Cache、量化支持
Day 5  4h    vLLM vs TensorRT-LLM 性能对比测试；不同场景下的选择策略

资源： NVIDIA TensorRT-LLM GitHub、NVIDIA 官方文档和博客

第 12 周：其他推理框架与对比（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  llama.cpp：CPU 推理、GGUF 格式、量化方案（Q4_0/Q4_K_M 等）
Day 2  3.5h  ONNX Runtime：模型导出与优化；跨平台推理方案
Day 3  3.5h  Triton Inference Server：模型部署、动态 batching、模型仓库
Day 4  3.5h  各框架横向对比：功能矩阵、性能基准、适用场景
Day 5  3.5h  OpenAI 兼容 API 规范；推理服务的 HTTP/gRPC 接口测试

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

第五阶段：软件测试与 QA（第 13-15 周）

第 13 周：AI 系统测试策略（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  测试金字塔在 AI 系统中的应用：单元测试 → 集成测试 → 系统测试
Day 2  3.5h  白盒测试：代码覆盖率（行/分支/路径）、C/C++ 用 gcov/lcov、Python 用 pytest-cov
Day 3  3.5h  API 测试：REST API 测试（requests/pytest）；OpenAI API 兼容接口的测试用例设计
Day 4  3.5h  性能测试：延迟(latency)、吞吐(throughput)、TTFT、TPS 等关键指标定义与测量
Day 5  3.5h  兼容性测试：不同 GPU 型号、不同 CUDA 版本、不同模型格式的兼容矩阵

第 14 周：测试自动化框架（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  pytest 高级用法：fixture、参数化、marker、conftest.py
Day 2  3.5h  CI/CD 流水线：GitHub Actions / Jenkins 集成自动化测试
Day 3  3.5h  性能基准测试框架：编写可重复的 benchmark 脚本；结果可视化
Day 4  3.5h  模型精度验证：Perplexity 评估、MMLU/HumanEval 等常见 benchmark
Day 5  3.5h  Docker 容器化测试环境；GPU 容器（NVIDIA Container Toolkit）

第 15 周：Profiling 与问题排查（每天 3.5 小时）

天     时长  学习内容
Day 1  3.5h  Python Profiling：cProfile、py-spy、line_profiler 性能分析
Day 2  3.5h  GPU Profiling：用 Nsight Systems 分析推理引擎的 GPU 时间线
Day 3  3.5h  内存分析：GPU 显存泄漏排查、torch.cuda.memory_summary()
Day 4  3.5h  常见问题模式：OOM 排查、推理变慢根因分析、精度异常定位
Day 5  3.5h  测试报告编写：问题分类、复现步骤、环境信息收集的最佳实践

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

第六阶段：综合实战（第 16 周）

第 16 周：端到端项目（每天 4 小时）

天     时长  学习内容
Day 1  4h    搭建完整测试环境：vLLM + TensorRT-LLM 部署 LLaMA 模型
Day 2  4h    编写自动化测试套件：功能测试（API 正确性）、精度测试（对比 HuggingFace 基线）
Day 3  4h    性能基准测试：不同量化方案(FP16/AWQ/GPTQ)的 latency/throughput 对比
Day 4  4h    分布式推理测试：多 GPU Tensor Parallel 部署与验证；故障注入测试
Day 5  4h    整理输出：测试报告、性能对比图表、个人技术博客/笔记沉淀

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

时间总览

阶段                    周数          总学时  核心能力
AI/深度学习基础         第 1-3 周     ~48h    神经网络、Transformer、注意力机制
LLM 原理与优化          第 4-6 周     ~58h    KV Cache、FlashAttention、PagedAttention、量化、剪枝
GPU 与 CUDA             第 7-9 周     ~52h    GPU 架构、CUDA 编程、性能分析工具
推理引擎实战            第 10-12 周   ~57h    vLLM、TensorRT-LLM 源码与实操
测试与 QA               第 13-15 周   ~52h    测试策略、自动化、Profiling
综合实战                第 16 周      ~20h    端到端项目整合
合计                    16 周         ~287h

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

关键学习建议

  • 第 5-6 周是重中之重 — 职位描述中明确要求的 FlashAttention / PagedAttention / Continuous Batching / Speculative Decoding / AWQ / GPTQ，
  必须做到能用自己的话解释原理
  • 动手 > 看书 — 每学一个概念，立刻写代码验证或跑实验，纯看理论记不住
  • 做笔记用 "费曼法" — 用最简单的语言解释每个技术点，检验是否真正理解
  • GitHub 上建一个学习仓库 — 把每周的实验代码、测试脚本、笔记都上传，面试时可以展示
  • 如果只有 CPU — 可以用 Google Colab 免费 GPU 或者租用云 GPU（AutoDL 等平台，几元/小时）


