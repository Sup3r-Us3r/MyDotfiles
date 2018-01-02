import requests
import json
import time
import datetime

requisicao = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
#print(requisicao.text)



while True:
    requisicao = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
    cotacao = json.loads(requisicao.text)

    print("")
    print("### COTAÇÃO ### ", datetime.datetime.now())
    print("Dolar:", cotacao["valores"]["USD"]["valor"])
    print("Euro:", cotacao["valores"]["EUR"]["valor"])
    print("Biticoin:", cotacao["valores"]["BTC"]["valor"])
    time.sleep(2)