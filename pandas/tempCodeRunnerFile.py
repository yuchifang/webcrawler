p.random.randint(1, 50, 11)
# print(info_nums)
info_nums['num_bins'] = pd.cut(x=info_nums['num'], bins=[1, 25, 50])
print(info_nums)
print("----------")
print(info_nums['num_bins'])
print("******")
print(info_nums['num_bins'].unique())