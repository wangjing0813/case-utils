import asyncio
from pathlib import Path
from utils import read_csv_async, filter_invalid

def load_and_clean(csv_path: str | Path):
    """同步包装：返回已过滤的 DataFrame"""
    async def _inner():
        df = await read_csv_async(csv_path)
        return filter_invalid(df)
    return asyncio.run(_inner())
