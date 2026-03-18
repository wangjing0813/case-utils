# monitor.py
"""
每 5 分钟记录一次系统 CPU、Memory、磁盘 I/O（如果有磁盘统计）到 logs/monitor.log。
依赖：psutil（>=5.9）
"""

import pathlib
import time
from datetime import datetime

import psutil

# --------------------- 配置 ---------------------
INTERVAL = 5 * 60                       # 5 分钟（秒）
LOG_FILE = pathlib.Path.cwd() / "logs" / "monitor.log"
# ------------------------------------------------

def _ensure_log_dir() -> None:
    """确保 logs/ 目录已创建。"""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def _collect() -> str:
    """
    采集一次系统指标，返回 CSV 行内容：
    timestamp,cpu_percent,mem_percent,read_bytes,write_bytes
    """
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=None)          # 立即返回当前 CPU 百分比
    mem = psutil.virtual_memory().percent           # 物理内存占用百分比
    # 磁盘 I/O：自系统启动累计的读写字节数
    io = psutil.disk_io_counters()
    read_b, write_b = io.read_bytes, io.write_bytes
    return f"{ts},{cpu:.1f},{mem:.1f},{read_b},{write_b}\n"

def monitor_loop() -> None:
    """无限循环，每 INTERVAL 秒写入一次记录。"""
    _ensure_log_dir()
    print(f"[monitor] 开始记录 → {LOG_FILE}")
    try:
        while True:
            line = _collect()
            # Python 3.11+ 支持直接 append（若低于 3.11 请改为 open(..., "a")）
            with LOG_FILE.open("a", encoding="utf-8") as f:
                f.write(line)
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\n[monitor] 手动停止。")
    except Exception as exc:
        print(f"\n[monitor] 异常退出: {exc}")

if __name__ == "__main__":
    monitor_loop()
