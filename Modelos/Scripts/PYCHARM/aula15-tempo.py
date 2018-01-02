#Site = openweathermap.org
#72bb8d39e3e50233a1dbc19b03e6cc6a

import requests
import json

cidade = input("Escreva o nome da sua cidade: ")
requisicao = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid=72bb8d39e3e50233a1dbc19b03e6cc6a")

tempo = json.loads(requisicao.text)

print("Condicao do tempo:", tempo["weather"][0]["main"])
print("Temperatura:", float(tempo["main"]["temp"]) - 273.15)