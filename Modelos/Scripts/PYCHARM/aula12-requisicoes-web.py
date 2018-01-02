#Request = requisição

import requests

requisicao = None
texto = None

cabecalho = {"User-agent": "Linux Arch", "Referer": "https://sup3r-us3r.github.io",}

meus_cookies = {"Ultima visita": "12-12-2020"}

dados = {"username": "super",
         "password": "toor"}

try:
    requisicao = requests.post("http://putsreq.com/0t124G2oZaUAjZsDMrnu", headers=cabecalho,
                              cookies=meus_cookies, data=dados)
    texto = requisicao.text
    #requisicao = requests.post("https://solyd.com.br")
    #requisicao = requests.delete("https://solyd.com.br")

except Exception as e:
    print("Requisicão deu erro", e)

#print(requisicao.status_code)

print(texto)

