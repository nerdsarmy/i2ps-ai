from __future__ import annotations

import os
import platform
import shutil


def gib(value: int) -> float:
    return value / (1024 ** 3)


print("I2PS AI system inventory")
print("------------------------")
print("OS:", platform.platform())
print("Machine:", platform.machine())
print("Processor:", platform.processor() or "unknown")
print("CPU count:", os.cpu_count())

try:
    import psutil

    mem = psutil.virtual_memory()
    print(f"RAM: {gib(mem.total):.1f} GiB")
except Exception:
    print("RAM: install psutil for automatic detection")

disk = shutil.disk_usage("/")
print(f"Disk total: {gib(disk.total):.1f} GiB")
print(f"Disk free:  {gib(disk.free):.1f} GiB")

for command in ("nvidia-smi", "rocminfo"):
    if shutil.which(command):
        print(f"{command}: available")
