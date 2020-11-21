import random
import pandas as pd 

# lat range: 18.40 to 18.70
# long range: 73.75 to 74.05

lst_lat = [random.uniform(18.40, 18.70).__round__(5) for _ in range(1000)]
lst_long = [random.uniform(73.75, 74.05).__round__(5) for _ in range(1000)]

df = pd.DataFrame(lst_lat)
df['longitude'] = lst_long
df.columns = ['latitude', 'longitude']
print(df.head())

# df.to_csv('dummie_data.csv', index=False)
