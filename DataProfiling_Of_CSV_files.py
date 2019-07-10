# For Data Profile
#importing the necessary packages
import pandas as pd
import pandas_profiling
df = pd.read_csv('/Users/xyxz/abc/zip_code_database.csv',encoding = "ISO-8859-1")
pandas_profiling.ProfileReport(df)
profile = df.profile_report(title='Zip Code Data Profiling Report')
profile.to_file(output_file="Zip_Code_Data_Profiling.html")
