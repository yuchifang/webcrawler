import pandas as pd
# todo version 1.5.0

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen = [59, 9, 19, 14, 6, 77]

ironmen_dict = {
                "groups": groups,
                "ironmen": ironmen
}

# 建立 data frame
ironmen_df = pd.DataFrame(ironmen_dict)

print(ironmen_df.count()) # 計算總鐵人數
print("---") # 分隔線
print(ironmen_df.mean()) # 計算平均鐵人數
print("---") # 分隔線
print(ironmen_df.std()) # 計算中位數
print("---") # 分隔線
print(ironmen_df.describe()) # 描述統計