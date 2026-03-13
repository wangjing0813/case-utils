import pandas as pd
from typing import Any
import asyncio

async def async_filter_invalid(df: pd.DataFrame) -> pd.DataFrame:
    """异步包装，只是返回协程，内部仍使用同步 Pandas 检查。"""
    # 这里不做真正的异步 I/O，只是让调用者在 async 流程中使用
    required = {"id", "timestamp", "value"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # 同步的业务规则（可以放进线程池 async‑ify，但目前足够）
    mask = (
        pd.to_numeric(df["id"], errors="coerce").astype("Int64") > 0 &
        pd.to_datetime(df["timestamp"], errors="coerce").notna() &
        pd.to_numeric(df["value"], errors="coerce").between(0, 100, inclusive="both")
    )
    return df.loc[mask].reset_index(drop=True)
