import pandas as pd

# 1.load your file
df=pd.read_csv(r"C:\users\DELL\Documents\raw_data.csv")

#2. FIX THE MISSING DATA
df['Price']=df['Price'].fillna(0)

#3. Create the total
total_value = df['Price'].sum()

#4. simple printing(No fancy quotes or f-strings)
print("--- OFFICE REPORT ---")
print(df)
print("TOTAL REVENUE:")
print(total_value)
df.to_excel("Office_Report.xlsx",index=False)
