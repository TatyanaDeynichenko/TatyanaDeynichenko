print('Hello World!')
import requests

url = 'https://www.vbr.ru/banki/kurs-valut/cbrf/'
response = requests.get(url)
print(response)