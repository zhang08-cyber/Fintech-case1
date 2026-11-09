# -*- coding: utf-8 -*-
"""
案例1：A股个股数据清洗与可视化（贵州茅台）
广东金融学院 · 金融科技专业
"""

import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. 拉取茅台 2023 年日K线（前复权）
# =========================
df = ak.stock_zh_a_hist(
    symbol="600519",
    period="daily",
    start_date="20230101",
    end_date="20231231",
    adjust="qfq"
)

print("数据拉取成功，行数：", len(df))

# =========================
# 2. 数据清洗
# =========================
df["日期"] = pd.to_datetime(df["日期"])
df.sort_values("日期", inplace=True)
df.reset_index(drop=True, inplace=True)
df.dropna(subset=["开盘", "收盘", "最高", "最低"], inplace=True)

# =========================
# 3. 计算指标
# =========================
df["MA5"] = df["收盘"].rolling(5).mean()
df["MA21"] = df["收盘"].rolling(21).mean()
df["MA13"] = df["收盘"].rolling(13).mean()
# =========================
# 4. 画图
# =========================
plt.figure(figsize=(12, 6))
plt.plot(df["日期"], df["收盘"], label="收盘价", linewidth=1.5)
plt.plot(df["日期"], df["MA5"], label="MA5", linewidth=1.2)
plt.plot(df["日期"], df["MA21"], label="MA21", linewidth=1.2)
plt.plot(df["日期"], df["MA13"], label="MA13", linewidth=1.2)


plt.title("贵州茅台 2023 年日线 + MA5 / MA21")
plt.xlabel("日期")
plt.ylabel("价格（元）")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# =========================
# 5. 保存 CSV（作品集用）
# =========================
df.to_csv("maotai_2023.csv", index=False, encoding="utf-8-sig")
print("✅ maotai_2023.csv 已保存")