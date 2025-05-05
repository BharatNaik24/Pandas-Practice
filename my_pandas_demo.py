import pandas as pd

# mydataset = {
#     'cars': ['BMV', "VOLVO", "FORD"],
#     'passings':[3,5,7]
# }

# myVar = pd.DataFrame(mydataset)
# print(myVar)


# print(pd.__version__)

# a = [2,4,0,8,1,9,9,6]
# myVar = pd.Series(a)
# print(myVar)

# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)

# print(myvar["y"], 'THis is single line call')


# import pandas as pd

# calories = {
#   'day1':420,
#   'day2':380,
#   'day3':390
# }

# myVar = pd.Series(calories)
# print(myVar)

import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data,index = ["day1", "day2", "day3"])

# print(myvar.loc['day1'])

# df = pd.read_csv('newFile.txt')
# print(df.to_string())

# df = pd.read_csv('newFile.txt')
# print(df.to_string())
# df.dropna(inplace= True)
# df.fillna(130, inplace=True)
# print(df.to_string())


# df = pd.read_csv('demFile.txt')

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# df.dropna(subset=['Date'], inplace=True)
# print(df.duplicated())
# df.drop_duplicates(inplace=True)
# print(df.duplicated())


# --------------------
# Advanced Pandas Practice
# --------------------


# 1. DataFrame Properties: .shape, .columns, .index, .dtypes

import pandas as pd

df = pd.DataFrame(
    {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35], "Score": [85, 90, 95]}
)

# print("Shape:", df.shape)
# print("Columns:", df.columns)
# print("Index:", df.index)
# print("Data Types:\n", df.dtypes)

# 2. Accessing Data: loc[], iloc[], and Direct Access

# Direct column access
print(df["Name"])

# loc[] - label-based
print(df.loc[0])  # first row

# iloc[] - position-based
print(df.iloc[1])  # second row


# 3. Filtering and Conditional Selection

# Get rows where Age > 25
print(df[df["Age"] > 25])

# Filter by multiple conditions
print(df[(df["Age"] > 25) & (df["Score"] > 90)])


# 4. Data Manipulation: sort_values(), groupby(), merge(), concat()

# sort_values
# print(df.sort_values("Score", ascending=False))

# # groupby
# group_df = df.groupby("Age").mean()
# print(group_df)

# # merge
# df1 = pd.DataFrame({"ID": [1, 2], "Name": ["A", "B"]})
# df2 = pd.DataFrame({"ID": [1, 2], "Score": [90, 80]})
# merged = pd.merge(df1, df2, on="ID")
# print(merged)

# # concat
# df3 = pd.concat([df1, df2], axis=1)
# print(df3)


#  5. apply() and lambda

df["Adjusted Score"] = df["Score"].apply(lambda x: x + 5)
print(df)

# 6. Aggregation: mean(), sum(), count(), describe()

print("Mean Score:", df["Score"].mean())
print("Total Score:", df["Score"].sum())
print("Count of Rows:", df.count())
print("Describe:\n", df.describe())


# # Reading
# df = pd.read_csv("sample.csv")
# # df = pd.read_excel('sample.xlsx')

# # Writing
# df.to_csv("output.csv", index=False)
# # df.to_excel('output.xlsx', index=False)


import matplotlib.pyplot as plt

df.plot(x="Name", y="Score", kind="bar", color="skyblue", title="Score by Name")
plt.show()
