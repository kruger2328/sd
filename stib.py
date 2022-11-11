# file_name =  "C:\\Users\\mubin\\pythonexperiments\\hii.xls"
# sheet =  file_name
# import pandas as pd
# df = pd.read_excel(io=file_name, sheet_name=sheet)
# print(df.head(5))  # print first 5 rows of the dataframe

import pandas as pd

df = pd.read_excel(r'C:\\Users\\mubin\\pythonexperiments\\hii.xls')
print(df)
print(df.drop_duplicates("WELL NUMBER"))
print(df)