import asyncio
import aiofiles # type: ignore
async def async_read_file(path):
    async with aiofiles.open(path,mode="r", encoding="utf-8") as f:
        return await f.read()
async def main():
    task1 = asyncio.create_task(async_read_file("./data/sample.csv")) 
    task2 = asyncio.create_task(async_read_file("./data/sample2.csv"))   
    await asyncio.gather(task1,task2)
    results = await asyncio.gather(task1, task2)

    # ③ results[0] 是 sample.csv 的内容，results[1] 是 sample2.csv 的内容
    txt1, txt2 = results

    # ④ 打印或进一步处理
    print("=== sample.csv 内容 ===")
    print(txt1[:200])               # 为防止太长，仅打印前 200 字符
    print("\n=== sample2.csv 内容 ===")
    print(txt2[:200])

if __name__ == "__main__":
    # 直接用 asyncio.run（Python >=3.7）启动事件循环
    asyncio.run(main())