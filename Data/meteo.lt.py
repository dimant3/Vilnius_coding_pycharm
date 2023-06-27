import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# define website
url = "http://www.meteo.lt/lt/miestas?placeCode=Vilnius"

# response from the website
response = requests.get(url)  # pasiima visa informacija is URL

# create a bs4(beautifulsoup4) object (musu objektas) to parse (analizuoti) the HTML content
soup = BeautifulSoup(response.content, 'html.parser')  # soup kad galetume pasiimt produktu info

# find all weather information in the class content city
week_days = soup.find_all('span', class_='date')

temperatures = soup.find_all('span', class_='big up-from-zero')[::2]

night_temp = [temperature.get_text() for temperature in temperatures]

week_day = [day.get_text() for day in week_days]

temp_list = []
for temperature in temperatures:
    temp_text = temperature.get_text().replace('°C', '')
    temp_value = int(temp_text[:-1])
    temp_list.append(temp_value)


min_length = min(len(week_day), len(temp_list))


reorder_weekdays = week_day[:min_length]
reorder_temp = temp_list[:min_length]

week_day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

data = {
    'weekday': reorder_weekdays,
    'temperature': reorder_temp
}


df = pd.DataFrame(data)
df_sorted = df.sort_values(by=['weekday'], key=lambda x: pd.Categorical(x, categories=week_day_order, ordered=True))

plt.figure(figsize=(12,5))
plt.bar(df_sorted['weekday'], df_sorted['temperature'])

plt.xlabel('savaites diena')
plt.ylabel('temperatura')
plt.title('Oru prognoze Vilniuje')
plt.show()
print(df)





