import requests

s_city = 'Moscow,RU'

a = requests.get('http://api.openweathermap.org/data/2.5/weather',
                 params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': '6f17ebece6fd923a20d57f4f51c622ce'})

data = a.json()

print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Видимость:", data['visibility'])
print('Скорость ветра:', data['wind']['speed'])

a = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                 params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': '6f17ebece6fd923a20d57f4f51c622ce'})
data = a.json()

print("\nПрогноз погоды на неделю:")
for i in data['list']:
    print(f"Дата < {i['dt_txt']} > ", "Температура < {0:+3.0f} > ".format(i['main']['temp']),
          f"Погодные условия < {i['weather'][0]['description']} >",
          f"Видимость: < {i['visibility']} >", f"Скорость ветра: < {i['wind']['speed']} >",
          "____________________________",  sep='\n')
