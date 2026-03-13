import pytest, asyncio
import pandas as pd
from pathlib import Path
from case_utils.utils import read_csv_async, async_filter_invalid


@pytest.mark.asyncio
async def test_read_and_filter(tmp_path):
    # 创建临时 CSV
    csv = tmp_path / "sample.csv"
    csv.write_text(
        "id,timestamp,value,extra\\n"
        "1,2024-01-01 12:00:00,42,foo\\n"
        "2,2024-01-02 08:00:00,105,bar\\n"
        "3,invalid,23,baz\\n"
        "4,2024-01-04 15:20:00,78,qux\\n"
    )
    df_raw = await read_csv_async(csv)
    print("\n=== df_raw 內容 ===")
    print(df_raw.head())
    print(df_raw.columns.tolist())
    df_clean = await async_filter_invalid(df_raw)
    assert len(df_clean) == 2
    assert set(df_clean["id"]) == {1, 4}
