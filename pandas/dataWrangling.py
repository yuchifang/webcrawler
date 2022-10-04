import pandas as pd
name = ["Dan","Jack","Cindy","Daniel","Kripp"]
occupation = ["enginner","chef","PM","RD","sales"]

# 建立 dict
job_dict = {"name": name,
                  "occupation": occupation
}

# 建立第一個 data frame
job_df = pd.DataFrame(job_dict)

name = ["Dan","Jack","Cindy","Daniel","Kripp","Alan","Leo"]
age = ["10", "20", "30", "40", "45","50","15"]

# 建立 dict
age_dict = {"name": name,
            "age": age
            }

# 建立第二個 data frame
age_df = pd.DataFrame(age_dict)

# 連接
age_job_merged = pd.merge(job_df, age_df)
print(age_job_merged)
print("---------------------")
data = job_df.merge(age_df)
print(data)