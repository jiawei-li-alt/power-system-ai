import numpy as np
import pandas as pd
from pathlib import Path


# 生成 7 天的数据，每小时一个数据点
hours = 7 * 24

# 创建时间序列
time = pd.date_range(
    start="2026-09-01 00:00",
    periods=hours,
    freq="h"
)

# 设置随机种子，保证每次运行结果一致
np.random.seed(42)

# 模拟一天内的用电规律
hour_of_day = np.arange(hours) % 24

# 基础负荷
base_load = 500

# 模拟每天周期性的负荷变化
daily_pattern = 100 * np.sin(
    2 * np.pi * (hour_of_day - 7) / 24
)

# 添加一些随机波动
noise = np.random.normal(
    loc=0,
    scale=20,
    size=hours
)

# 得到最终模拟负荷
load = base_load + daily_pattern + noise

# 创建表格
data = pd.DataFrame({
    "time": time,
    "load": load
})

# 找到项目根目录
project_root = Path(__file__).resolve().parent.parent

# 创建 data 文件夹
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)

# 保存成 CSV 文件
output_file = data_dir / "load_data.csv"
data.to_csv(output_file, index=False)

print("模拟负荷数据生成成功！")
print(f"文件保存位置：{output_file}")
print(data.head())
