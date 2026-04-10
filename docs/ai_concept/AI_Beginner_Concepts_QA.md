# AI Beginner Concepts & Q&A

> A beginner-friendly guide to understand AI/LLM fundamental concepts.
> Written for someone with programming background but no AI/LLM knowledge.

---

# Part 1: Previous Q&A

---

## Q1: What is a "Prompt"?

A **prompt** is simply **the text input you give to a Large Language Model (LLM)**. Think of it as a question or instruction you type into a chatbot.

### The Simplest Analogy

```
You (Human)  -->  "What is the capital of France?"  -->  LLM
                   ^ This is the PROMPT

LLM          -->  "The capital of France is Paris."  -->  You
                   ^ This is the RESPONSE/COMPLETION
```

It's exactly like texting someone a question - your message is the "prompt", their reply is the "completion".

### Types of Prompts

| Type | Example | Use Case |
|------|---------|----------|
| **Question** | "What is deep learning?" | Getting information |
| **Instruction** | "Translate 'hello' to French" | Asking to perform a task |
| **Completion** | "Once upon a time, there was a" | LLM continues the text |
| **Conversation** | Multi-turn chat messages | Chatbot interaction |

### How It Works Under the Hood

From an engineering perspective (which matters for QA role):

```
"What is AI?"
     |
     v
[Tokenizer] -->  [2132, 374, 15592, 30]    <-- tokens (numbers)
                          |
                          v
                    [LLM Model]
                          |
                          v
                  [5765, 13, 2342, ...]      <-- output tokens
                          |
                          v
               [Detokenizer] --> "AI is a field of..."
```

1. **Your text** (prompt) gets split into **tokens** (small pieces, roughly word fragments)
2. The model processes these tokens as **numbers**
3. It generates output tokens **one by one** (autoregressive decoding)

### A Real API Example

When you call an LLM API (like vLLM service), the prompt is just part of the JSON request:

```python
import requests

requests.post("http://localhost:8000/v1/chat/completions", json={
    "model": "Qwen/Qwen2-1.5B-Instruct",
    "messages": [
        # System prompt: sets the LLM's behavior
        {"role": "system", "content": "You are a helpful assistant."},
        # User prompt: your actual question
        {"role": "user", "content": "What is deep learning?"},
    ],
    "max_tokens": 100,       # max output length
    "temperature": 0.7,      # randomness (0=deterministic, 1=creative)
})
```

Here there are actually **two prompts**:
- **System prompt**: Background instructions (like telling the LLM its personality)
- **User prompt**: The actual question

### Why "Prompt" Matters for QA Engineers

Prompt shows up in several performance-critical contexts:

```
User sends prompt (e.g. 500 tokens)
        |
        v
   [Prefill Stage]  <-- processes ALL prompt tokens in parallel
        |               This determines TTFT (Time To First Token)
        |               Longer prompt = slower TTFT
        v
   [Decode Stage]   <-- generates response tokens one by one
        |               This determines TPOT (Time Per Output Token)
        v
   Response returned
```

As a QA engineer, you'll test things like:
- What happens with a **very long prompt**? (memory limits)
- What happens with an **empty prompt**?
- Does **Prefix Caching** work when multiple requests share the same system prompt?

### One-Sentence Summary

> **Prompt = the text you send to an LLM.** Everything the model reads before it starts generating a response.

---

## Q2: Credits, Tokens, Context Window, and Session Memory

### What is a Token?

```
"Hello, how are you?"

Tokenized --> ["Hello", ",", " how", " are", " you", "?"]
           = 6 tokens

Chinese example:
"What is deep learning?"

Tokenized --> ["What", " is", " deep", " learning", "?"]
           = 5 tokens (varies by tokenizer)
```

**Rule of thumb**:
- English: ~1 token = 0.75 words (or ~4 characters)
- Chinese: ~1 token = 1-2 characters
- Code: tends to use more tokens (symbols, indentation)

### What Costs Tokens in a Conversation?

```
You ask: "What is AI?"        -->  ~4 input tokens
I reply: "AI is a field..."   -->  ~50 output tokens
                                   ----------
                                   Total: ~54 tokens consumed

Next message in SAME session:
You ask: "Tell me more"       -->  the ENTIRE conversation history
                                   is sent again as context!

  [system prompt]               ~200 tokens
  [your 1st question]          ~4 tokens
  [my 1st answer]              ~50 tokens
  [your 2nd question]          ~3 tokens     <-- new
  ---------------------------
  Input: ~257 tokens           <-- grows every turn!
  + new output: ~100 tokens
```

**Key insight**: Each message in a session gets **more expensive** because the full conversation history is re-sent as input every time.

### "1M Tokens" = Model's Maximum Context Window

This is the **theoretical maximum** the model architecture can handle:

```
Claude Opus 4.6 Thinking 1M

Maximum context window: 1,000,000 tokens
= ~750,000 English words
= ~1,500 pages of text

This means: input + output combined can be
up to 1M tokens in a single conversation
```

### "Context 139K" = Current Session's Context Usage

This is how much context **this specific session** has consumed:

```
Session starts:     context = ~0K
You send message 1: context = ~2K
I reply:            context = ~10K
You send message 2: context = ~12K   (includes all previous messages)
I reply:            context = ~50K
... many messages later ...
Now:                context = ~139K

|================---------------------------------------|
 ^ 139K used                              1M max       ^
```

### Session Memory - There is NONE Across Sessions

```
Session A (current):
  Y  I know your study plan
  Y  I know the guide I wrote
  Y  I know you asked about prompts

Session B (new session):
  X  I know nothing about you
  X  I don't remember the study guide
  X  I start completely fresh
```

**Why?** Each session is independent. My "memory" is just the conversation context. When the session closes, that context is gone.

**Workaround**: Reference saved files in new sessions:
```
"Read /workspace/git/AI_DL_QA_Engineer_Study_Guide.md
 and help me with Week 4 Day 1"
```

### Quick Reference

| Concept | Meaning |
|---------|---------|
| **Token** | Smallest unit the model processes (~0.75 English words) |
| **1M tokens** | Model's max capacity per conversation |
| **139K context** | How much of that capacity this session has used |
| **Input tokens** | What you send (grows each turn - includes history!) |
| **Output tokens** | What I generate (typically more expensive per token) |
| **Session** | Independent conversation; no memory carries over |

---

# Part 2: Core AI Concepts for Beginners

> Read this from top to bottom. Each concept builds on the previous one.

---

## Concept 1: What is AI, Machine Learning, and Deep Learning?

Think of it as nested circles:

```
+---------------------------------------------------+
|  AI (Artificial Intelligence)                      |
|  = Machines that can do "smart" things             |
|                                                    |
|  +--------------------------------------------+   |
|  |  ML (Machine Learning)                      |   |
|  |  = Machines that LEARN from data            |   |
|  |    (instead of being explicitly programmed) |   |
|  |                                             |   |
|  |  +--------------------------------------+   |   |
|  |  |  DL (Deep Learning)                  |   |   |
|  |  |  = ML using Neural Networks          |   |   |
|  |  |    with many layers ("deep")         |   |   |
|  |  |                                      |   |   |
|  |  |  +-------------------------------+  |   |   |
|  |  |  |  LLM (Large Language Model)   |  |   |   |
|  |  |  |  = DL for understanding and   |  |   |   |
|  |  |  |    generating human language   |  |   |   |
|  |  |  +-------------------------------+  |   |   |
|  |  +--------------------------------------+   |   |
|  +--------------------------------------------+   |
+---------------------------------------------------+
```

**Traditional Programming vs Machine Learning**:

```
Traditional:
  Rules + Data  --> Program --> Output
  "if temperature > 30: print('hot')"

Machine Learning:
  Data + Output --> Training --> Model (learns the rules itself)
  Give it 10000 photos labeled "cat" or "dog" --> it learns to tell them apart
```

---

## Concept 2: What is a Neural Network?

A neural network is inspired by the human brain. It's layers of "neurons" connected together:

```
Input Layer      Hidden Layers       Output Layer
(your data)      (learned features)  (prediction)

  O ---\
        O ---\
  O ---/ \    O ---\
            X      O --> answer
  O ---\ /    O ---/
        O ---/
  O ---/

Each connection has a "weight" (a number).
Training = adjusting these weights to make better predictions.
```

**Real example - Image classification**:

```
Photo of a cat (pixels)
       |
  [Layer 1] detects edges
       |
  [Layer 2] detects shapes (ears, eyes)
       |
  [Layer 3] detects face patterns
       |
  Output: "cat" 95%, "dog" 3%, "bird" 2%
```

**Key terms**:
- **Weight/Parameter**: A number the model learns during training. When we say "7B model", it has 7 billion such numbers.
- **Layer**: One step of processing. "Deep" learning = many layers (GPT-4 has ~120 layers).
- **Forward pass**: Data flows through the network to get a prediction.
- **Backward pass**: Errors flow backward to adjust weights (only during training).

---

## Concept 3: What is a Model?

A **model** is just a **file containing billions of numbers (weights)** that were learned during training.

```
Training (done by OpenAI/Meta/Google, costs millions of $):
  Massive text data (internet) + Huge GPU clusters + Months of compute
      |
      v
  Model file: llama-2-7b.bin  (13 GB for 7B parameters in FP16)
  = 7,000,000,000 learned numbers

Using the model (inference, what YOU do):
  Model file + Your prompt --> GPU computation --> Response
```

**Model sizes and what they mean**:

| Model | Parameters | FP16 Size | Typical GPU Needed |
|-------|-----------|----------|-------------------|
| Small (1-3B) | 1-3 billion | 2-6 GB | Any modern GPU |
| Medium (7B) | 7 billion | 13 GB | RTX 4090 (24GB) |
| Large (13B) | 13 billion | 26 GB | A100 (40/80GB) |
| Very Large (70B) | 70 billion | 140 GB | Multiple A100/H100 |
| GPT-4 class | ~1 trillion? | ~2 TB? | Massive GPU cluster |

**Why does size matter for QA?**
- Bigger model = more GPU memory needed
- Bigger model = slower inference
- Your job: test if the model runs correctly and efficiently on given hardware

---

## Concept 4: Training vs Inference (The Most Important Distinction)

This is THE most critical concept for your QA role:

```
TRAINING (Teaching)                    INFERENCE (Using)
========================              ========================
Goal: Learn the weights               Goal: Generate answers
When: Before deployment               When: After deployment (production)
Who: ML Engineers                      Who: Users / Applications
Cost: Millions of dollars              Cost: Per-query (much cheaper)
Time: Days to months                   Time: Milliseconds to seconds
Hardware: GPU clusters                 Hardware: Single/few GPUs
Precision: High (FP32/BF16)           Precision: Can be lower (FP16/INT8/INT4)

     TRAINING                              INFERENCE
  +-------------+                     +-------------+
  | Text Data   |                     | User Prompt |
  |  (TB)       |                     |   (KB)      |
  +------+------+                     +------+------+
         |                                   |
         v                                   v
  [Forward Pass]                      [Forward Pass ONLY]
         |                                   |
         v                                   v
  [Compute Loss]                      [Generate Token]
         |                                   |
         v                                   |
  [Backward Pass]  <-- NOT in inference!     |
         |                                   |
         v                                   v
  [Update Weights]                    [Return Response]
         |
         v
  [Repeat billions of times]

YOUR JOB AS QA: You mainly test INFERENCE (the right side)
- Does the model respond correctly?
- How fast? (latency)
- How many requests per second? (throughput)
- Does it crash with long inputs?
- Does it use too much GPU memory?
```

---

## Concept 5: What is a Transformer?

The **Transformer** is the architecture behind ALL modern LLMs (GPT, LLaMA, Claude, etc.).

```
Before Transformers (2017):
  Text processed word by word (sequential, slow)
  "The cat sat on the mat"
   1 -> 2 -> 3 -> 4 -> 5 -> 6  (must wait for each step)

Transformers:
  All words processed AT ONCE (parallel, fast)
  "The cat sat on the mat"
   1    2    3    4    5    6   (all processed simultaneously)

The magic: ATTENTION MECHANISM
  Each word can "look at" every other word to understand context
  "The bank by the river" --> "bank" attends to "river" --> means riverbank
  "The bank gave a loan"  --> "bank" attends to "loan"  --> means financial bank
```

**Why should you care?**

Every optimization technique in your study guide is about making Transformers faster:
- **FlashAttention**: Faster attention computation
- **KV Cache**: Avoid recomputing attention for old tokens
- **PagedAttention**: Better memory management for attention cache
- **Quantization**: Smaller numbers = less memory = faster

---

## Concept 6: How Does an LLM Actually Generate Text?

LLMs generate text **one token at a time**, each time predicting the most likely next word:

```
Prompt: "The capital of France is"

Step 1: Model sees "The capital of France is"
        Predicts next token probabilities:
          "Paris"  -> 92%
          "Lyon"   -> 2%
          "a"      -> 1%
          ...
        Picks: "Paris"

Step 2: Model sees "The capital of France is Paris"
        Predicts next:
          "."      -> 75%
          ","      -> 15%
          "!"      -> 5%
          ...
        Picks: "."

Step 3: Model sees "The capital of France is Paris."
        Predicts next:
          "<EOS>"  -> 80%    (End Of Sequence = stop generating)
        Stops.

Final output: "Paris."
```

This is called **autoregressive generation** - each new token depends on ALL previous tokens.

**Why this matters for performance**:
- Each token requires a full forward pass through the model
- Generating 100 tokens = 100 forward passes (sequential, can't be parallelized!)
- This is why LLM inference is slow and why optimizations like Speculative Decoding exist

---

## Concept 7: What is a GPU and Why Does AI Need It?

```
CPU (your laptop):                    GPU (graphics card):
  Few strong workers (4-16 cores)      Thousands of weak workers (thousands of cores)
  Good at complex tasks one at a time  Good at simple tasks all at once

  Analogy:                             Analogy:
  4 expert mathematicians              10,000 elementary school students

  Task: Solve 1 hard equation          Task: Solve 1 hard equation
  CPU wins! (experts are smarter)      GPU loses (students can't do it)

  Task: Add 10,000 pairs of numbers    Task: Add 10,000 pairs of numbers
  CPU: does them 1 by 1 (slow)         GPU: each student does 1 pair (instant!)
```

**AI = lots of matrix math = lots of simple parallel operations = GPU wins**

```
Neural network forward pass:
  Layer 1: multiply 4096x4096 matrix with 4096x1 vector
  Layer 2: same thing
  ... 32-120 layers ...

  Each matrix multiplication = millions of multiply-add operations
  ALL of them can be done in parallel on GPU
```

**Key GPU specs you'll encounter**:

| Spec | What it means | Why it matters |
|------|--------------|---------------|
| **VRAM (e.g. 80GB)** | GPU's memory | Must fit model + KV Cache |
| **FLOPS (e.g. 312 TFLOPS)** | Compute speed | How fast math is done |
| **Memory Bandwidth (e.g. 2TB/s)** | Memory read speed | Bottleneck for LLM decode |
| **Tensor Cores** | Special matrix math units | 8-16x faster for AI workloads |

---

## Concept 8: What is Inference Optimization? (Why Your Job Exists)

Running a model naively is **slow and expensive**. Your job is to test the optimizations:

```
PROBLEM                           SOLUTION                        YOUR TEST
======================           ========================        =================
Model too big for 1 GPU    -->   Quantization (shrink numbers)   Test: accuracy loss?
                                 INT8: 13GB -> 6.5GB
                                 INT4: 13GB -> 3.3GB

Generation is slow         -->   KV Cache (don't recompute)      Test: correctness?
(repeating old computation)

KV Cache wastes memory     -->   PagedAttention (smart memory)   Test: memory usage?
(fragmentation)

Attention is O(n^2)        -->   FlashAttention (block compute)  Test: speed? accuracy?

Tokens generated 1-by-1   -->   Speculative Decoding            Test: output matches?
(serial bottleneck)              (guess multiple, verify once)

Short requests wait for    -->   Continuous Batching             Test: throughput?
long requests                    (dynamic scheduling)

Single GPU not enough      -->   Tensor Parallelism              Test: multi-GPU correct?
                                 (split model across GPUs)
```

**This table is essentially your entire job description as a QA engineer.**

---

## Concept 9: Key Numbers Every AI QA Engineer Should Know

```
1 token          ~= 0.75 English words or ~1.5 Chinese characters
1B parameters    ~= 2 GB in FP16 (half precision)
7B model         ~= 13 GB VRAM minimum
70B model        ~= 140 GB VRAM (needs multiple GPUs)

A100 GPU         = 80 GB VRAM, $10-15K
H100 GPU         = 80 GB VRAM, $25-40K (2x faster than A100)
RTX 4090         = 24 GB VRAM, $1.5-2K (consumer, good for small models)

Good TTFT        < 500ms (user doesn't feel delay)
Good TPOT        < 50ms per token (~20 tokens/sec, faster than reading)
Human reading    ~= 3-4 tokens/sec

LLM inference    = 70-80% of the cost is reading memory (memory-bound)
Training         = costs 100-10000x more than serving one inference request
```

---

## Concept 10: The Complete Picture - From User to Response

```
USER types: "What is AI?"
  |
  v
[Load Balancer] picks a server
  |
  v
[API Server] receives HTTP request
  |
  v
[Tokenizer] "What is AI?" --> [2132, 374, 15592, 30]
  |
  v
[Scheduler] decides when to process (Continuous Batching)
  |
  v
[PREFILL] process all input tokens in parallel on GPU
  |        - Computes Q, K, V matrices for each token
  |        - Stores K, V in KV Cache
  |        - Uses FlashAttention for efficiency
  |        - Uses PagedAttention for memory management
  |        - TTFT is measured here
  v
[DECODE LOOP] generate tokens one by one
  |  |
  |  +-> Read KV Cache from GPU memory
  |  +-> Compute attention for new token only
  |  +-> Predict next token probabilities
  |  +-> Sample a token (based on temperature/top_p)
  |  +-> Append new K,V to KV Cache
  |  +-> TPOT is measured per iteration
  |  +-> If end token or max_tokens reached: stop
  |  +-> Otherwise: loop back
  |
  v
[Detokenizer] [5765, 13, ...] --> "AI is a field of..."
  |
  v
[API Server] returns JSON response (or SSE stream)
  |
  v
USER sees the answer

WHAT QA TESTS:
  - Every box in this diagram can fail
  - Every arrow is a potential bottleneck
  - Your job: find the failures and bottlenecks
```

---

## Concept 11: Common File Formats You'll See

| Format | Extension | What it is | When you'll see it |
|--------|-----------|------------|-------------------|
| **PyTorch** | .pt, .pth, .bin | Raw model weights | Most common, Hugging Face default |
| **SafeTensors** | .safetensors | Safer model format | Replacing .bin (no code execution risk) |
| **ONNX** | .onnx | Cross-platform format | TensorRT conversion, ONNX Runtime |
| **GGUF** | .gguf | Quantized for CPU/edge | llama.cpp, local deployment |
| **TensorRT Engine** | .engine, .plan | NVIDIA optimized | TensorRT-LLM production |

---

## Concept 12: Glossary of Terms You'll Encounter Daily

| Term | Plain English |
|------|--------------|
| **Model** | A file with billions of learned numbers |
| **Parameter / Weight** | One learned number in the model |
| **Token** | A piece of text (~0.75 words) that the model processes |
| **Prompt** | Your input text to the model |
| **Completion** | The model's generated output |
| **Inference** | Using the model to generate a response |
| **Training** | Teaching the model (adjusting weights with data) |
| **Fine-tuning** | Further training a pre-trained model on specific data |
| **GPU** | Graphics card that runs AI computations in parallel |
| **VRAM** | GPU's memory (must fit model + working data) |
| **CUDA** | NVIDIA's programming platform for GPU computing |
| **Tensor** | A multi-dimensional array of numbers (the basic data unit) |
| **Batch** | Processing multiple requests at once for efficiency |
| **Latency** | Time to get a response (lower = better) |
| **Throughput** | Requests or tokens processed per second (higher = better) |
| **TTFT** | Time To First Token - how fast first word appears |
| **TPOT** | Time Per Output Token - speed of generation |
| **KV Cache** | Cached computation to avoid repeating work |
| **Quantization** | Shrinking model numbers (FP16->INT8) to save memory |
| **Attention** | The mechanism that lets model understand word relationships |
| **Transformer** | The neural network architecture all modern LLMs use |
| **Autoregressive** | Generating one token at a time, each depending on previous |
| **Prefill** | Processing your prompt (parallel, fast per token) |
| **Decode** | Generating response (serial, one token at a time) |
| **Hugging Face** | The "GitHub of AI models" - where models are shared |
| **vLLM** | Popular open-source LLM serving engine |
| **TensorRT** | NVIDIA's inference optimization toolkit |
| **ONNX** | Open format for exchanging models between frameworks |
| **SLA** | Service Level Agreement - performance promises (e.g. P99 < 1s) |
| **P99 latency** | 99% of requests complete within this time |
| **OOM** | Out Of Memory - GPU ran out of VRAM |
| **FP16/BF16/INT8** | Number precision formats (smaller = less memory, less accuracy) |

---

## How to Read Your Study Guide Efficiently

Now that you understand these concepts, here's the recommended order:

```
Step 1: READ THIS FILE FIRST (you're here!)
        Understand the big picture before diving into details.

Step 2: Week 4 Day 1 (ML basics) + Day 4 (LLM basics)
        These build directly on what you just learned.

Step 3: Week 4 Day 3 (Transformer architecture)
        Now you're ready to understand the math behind attention.

Step 4: Week 7 (vLLM)
        Connect theory to real engineering tools.

Step 5: Week 10-12 (Optimizations)
        Understand WHY each optimization exists (refer back here).

Step 6: Everything else fills in the gaps.
```

---

> **Remember**: In new sessions, reference these files:
> - `/workspace/git/AI_Beginner_Concepts_QA.md` (this file - beginner concepts)
> - `/workspace/git/AI_DL_QA_Engineer_Study_Guide.md` (full 16-week study guide)
