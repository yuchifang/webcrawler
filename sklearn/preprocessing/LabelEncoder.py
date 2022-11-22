from sklearn import preprocessing
le = preprocessing.LabelEncoder()
print(le.fit_transform(["A","B","B","C","D","C"]))