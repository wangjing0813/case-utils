import time, asyncio

def sync():
    print('sync start')
    time.sleep(2)            # 这里阻塞 2 秒
    print('sync end')

async def async_():
    print('async start')
    await asyncio.sleep(2)   # 这里不阻塞，事件循环可以执行其它任务
    print('async end')

# 运行两次：
start = time.time(); sync();   print('elapsed sync', time.time() - start)
start = time.time(); asyncio.run(async_()); print('elapsed async', time.time() - start)
