import pandas as pd
import requests

URL = 'https://pynative.com/wp-content/uploads/2019/01/Automobile_data.csv'
FILE_PATH = './V12/automobile_data.csv'

res = requests.get(URL)

fl = open(FILE_PATH, 'wb')
fl.write(res.content)
fl.close()

df = pd.read_csv(FILE_PATH)
df.head()

# 1. Among the first 10 entries in the data file, determine the company and the price of the most expensive car.
df_top_ten = df[:10]
df_top_ten = df_top_ten[df_top_ten['price'] == df_top_ten['price'].max()]
print(df_top_ten.head())
print('\n')

# 2. Among all BMWs, count the models with 4 and with 6 cylinders.
df_bmw = df[df['company'] == 'bmw']
df_bmw_counts = df_bmw['num-of-cylinders'].value_counts()
print(df_bmw_counts)
