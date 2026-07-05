import pandas as pd
import os

# Check if the file exists and its location
file_name = "Unemployment in India.csv"
if os.path.exists(file_name):
    print("File exists")
    df = pd.read_csv(file_name)
    print(df.info())
    print(df.head())
else:
    print("File not found")



# Code output
File exists
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 7 columns):
 #   Column                                    Non-Null Count  Dtype  
---  ------                                    --------------  -----  
 0   Region                                    740 non-null    object 
 1    Date                                     740 non-null    object 
 2    Frequency                                740 non-null    object 
 3    Estimated Unemployment Rate (%)          740 non-null    float64
 4    Estimated Employed                       740 non-null    float64
 5    Estimated Labour Participation Rate (%)  740 non-null    float64
 6   Area                                      740 non-null    object 
dtypes: float64(3), object(4)
memory usage: 42.1+ KB
None
           Region         Date  Frequency   Estimated Unemployment Rate (%)   Estimated Employed   Estimated Labour Participation Rate (%)   Area
0  Andhra Pradesh   31-05-2019    Monthly                              3.65           11999139.0                                     43.24  Rural
1  Andhra Pradesh   30-06-2019    Monthly                              3.05           11755881.0                                     42.05  Rural
2  Andhra Pradesh   31-07-2019    Monthly                              3.75           12086707.0                                     43.50  Rural
3  Andhra Pradesh   31-08-2019    Monthly                              3.32           12285693.0                                     43.97  Rural
4  Andhra Pradesh   30-09-2019    Monthly                              5.17           12256762.0                                     44.68  Rural
