# utils.py
import aiofiles
import pandas as pd
from io import StringIO
from pathlib import Path
from typing import Any

async def read_csv_async(path: Path | str, **kwargs: Any) -> pd.DataFrame:
    """
    异步读取 CSV 并返回 pandas.DataFrame。

    Parameters
    ----------
    path : Path | str
        CSV 文件的路径（可以是相对路径或绝对路径）。
    **kwargs :
        直接转发给 pandas.read_csv，例如 sep=",", dtype=... 等。

    Returns
    -------
    pandas.DataFrame
    """
    # 统一为 Path 对象，便于后续操作
    path = Path(path)

    # 读取文件内容（全部读入内存，适合中小型 CSV）
    async with aiofiles.open(path, mode="r", encoding="utf-8") as f:
        raw_text = await f.read()

    # 用 StringIO 把字符串包装成类文件对象，让 pandas 正常解析
    df = pd.read_csv(StringIO(raw_text), **kwargs)
    return df


def filter_invalid(df: pd.DataFrame) -> pd.DataFrame:
    """
    根据业务规则过滤行：
      - 必须包含列 id、timestamp、value
      - id 为正整数
      - timestamp 能被解析为 datetime
      - value 必须在 [0, 100] 区间（含端点）

    参数
    ----
    df : pd.DataFrame
        待过滤的数据帧。

    返回
    ----
    pd.DataFrame
        已剔除非法记录、并已重置索引的 DataFrame。
    """
    required_cols = {"id", "timestamp", "value"}
    missing = required_cols - set(df.columns)  #在required_cols中，但不在set(df.columns)
    ###df是pandas.DataFrame，df.columns返回的是一个 Index 对象 ，它本质上是列名的有序集合（类似列表），但支持集合运算前要先转成 set，df.columns
    # 示例输出：Index(['id', 'timestamp', 'value', 'extra_info'], dtype='object')
    ###
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # 1️⃣ id 必须是正整数
    mask_id = pd.to_numeric(df["id"], errors="coerce").astype("Int64") > 0

    # 2️⃣ timestamp 必须能解析为 datetime
    mask_ts = pd.to_datetime(df["timestamp"], errors="coerce").notna()

    # 3️⃣ value 必须在 0~100 之间（含端点）
    mask_val = pd.to_numeric(df["value"], errors="coerce").between(0, 100, inclusive="both")

    # 综合所有掩码
    valid_mask = mask_id & mask_ts & mask_val
    return df.loc[valid_mask].reset_index(drop=True)
