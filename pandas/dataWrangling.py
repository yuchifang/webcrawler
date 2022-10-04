# import pandas as pd
# name = ["Dan","Jack","Cindy","Daniel","Kripp"]
# occupation = ["enginner","chef","PM","RD","sales"]

# # 建立 dict
# job_dict = {"name": name,
#                   "occupation": occupation
# }

# # 建立第一個 data frame
# job_df = pd.DataFrame(job_dict)

# name = ["Dan","Jack","Cindy","Daniel","Kripp","Alan","Leo"]
# age = ["10", "20", "30", "40", "45","50","15"]

# # 建立 dict
# age_dict = {"name": name,
#             "age": age
#             }

# # 建立第二個 data frame
# age_df = pd.DataFrame(age_dict)

# # 連接
# age_job_merged = pd.merge(job_df, age_df)
# print(age_job_merged)
# print("---------------------")
# data = pd.merge(job_df, age_df,left_on="occupation",right_index=True)
# print(data)
import pandas as pd
listOne = range(3)
listTwo = ["A","B","C"]
df1 = pd.DataFrame({"data2":listOne,"name":listTwo})
# print(df1)
listT = range(5)
listF = ["A","B","C","D","C"]
df2 = pd.DataFrame({"data1":listT,"name":listF})
# print(df2)
df3 = pd.merge(df1,df2,left_on="data2",right_index=True)
print("df3",df3)