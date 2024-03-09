
import pandas as pd
import datacompy
def compare_files(f1,f2):
    df1 = pd.read_excel(f1)
    df2 = pd.read_excel(f2)


    comparison = datacompy.Compare(df1,df2,join_columns=["FIRST"])
    print(comparison.report())



# Replace 'file1.xlsx' and 'file2.xlsx' with the actual file paths you want to compare
compare_files("C:\\Users\\admin\\Documents\\Book1.xlsx", "C:\\Users\\admin\\Documents\\Book2.xlsx")

