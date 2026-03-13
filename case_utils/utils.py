# case_utils/utils.py
import aiofiles
import pandas as pd
from io import StringIO
from pathlib import Path
from typing import Any

# -------------------------------------------------
# 1️⃣ 非同步讀取 CSV（支援字面 \\n）
# -------------------------------------------------
async def read_csv_async(path: Path | str, **kwargs: Any) -> pd.DataFrame:
    """
    讀取 CSV，支援：
      • 真正的換行 (\n、\r\n)
      • 測試中寫入的字面 \"\\n\"（兩個字符）

    會把文字正規化後交給 pandas 解析。
    """
    path = Path(path)

    # 讀取檔案內容（全部字串）
    async with aiofiles.open(path, mode="r", encoding="utf-8") as f:
        raw = await f.read()

    # 統一換行符
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    if "\\n" in raw:                # 把字面 \n 轉成真正的換行
        raw = raw.replace("\\n", "\n")

    # 切分成行，去除空行，重新拼接
    lines = [ln for ln in raw.split("\n") if ln.strip() != ""]
    cleaned_text = "\n".join(lines) + "\n"

    # 用 pandas 解析（使用默认 C 引擎，避免 lineterminator 問題）
    return pd.read_csv(
        StringIO(cleaned_text),
        sep=",",
        engine="c",               # 預設的 C 引擎最穩定
        **kwargs
    )

# -------------------------------------------------
# 2️⃣ 非同步版 filter_invalid
# -------------------------------------------------
async def async_filter_invalid(df: pd.DataFrame) -> pd.DataFrame:
    """
    檢查必須欄位、過濾非法行，返回已重置索引的 DataFrame。
    規則：
      - id 必須是正整數
      - timestamp 必須能被 pandas 解析為 datetime
      - value 必須在 [0, 100] 之間（含端點）
    """
    required_cols = {"id", "timestamp", "value"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # 1️⃣ id 正整數
    mask_id = pd.to_numeric(df["id"], errors="coerce").astype("Int64") > 0

    # 2️⃣ timestamp 必須是有效日期時間
    mask_ts = pd.to_datetime(df["timestamp"], errors="coerce").notna()

    # 3️⃣ value 必須在 0~100 之間
    mask_val = pd.to_numeric(df["value"], errors="coerce").between(0, 100, inclusive="both")

    # 合併所有掩碼
    valid_mask = mask_id & mask_ts & mask_val

    # 返回過濾後、索引已重置的 DataFrame
    return df.loc[valid_mask].reset_index(drop=True)