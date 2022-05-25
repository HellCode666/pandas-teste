import pandas as pd

# df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
#                    'B': [1, 2, 3, 4, 5, 6, 7, 8],
#                    'C': 'True False True False True False True False'.split(),
#                    'D': [8, 7, 6, 5, 4, 3, 2, 1],
#                    'E': [10, 10, 10, 10, 10, 10, 10, 10]})

df = pd.read_excel('./export_dataframe.xlsx') 

a = df.loc[df['C'] == True]
b = df.loc[df['C'] == False]


a['F'] = a['B'] + a['D']
b['F'] = b['B'] + b['E']

df5 = pd.concat([a, b])
sorted_df=df5.sort_index()

print(sorted_df)

# df.to_excel (r'.\export_dataframe.xlsx', index = False, header=True)

sorted_df.to_excel (r'.\export_dataframe2.xlsx', index = False, header=True)