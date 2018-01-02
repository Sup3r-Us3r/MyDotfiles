# "r" de regular "e" de expression | ex: regular expression for cellphone
import re
import requests

requisicao = requests.get("http://lacoxinha.com.br/contato")

string_de_teste = "O gato, a gata, os gatinhos, os gatoes, o gat"
string_de_teste2 = "bsbsbss-yoyuds@dsds.com.br"

'''
padrao = re.search(r"gat\w", string_de_teste) # "r" de RAW string | o ponto "." equivale a qualquer caracter | o \w é um caracter do tipo word
#print(r"Oi pessoal\nSegunda linha")

'''

#padrao = re.findall(r"gat\w+ e *", string_de_teste) #Quando se usa "findall" não usa o "group"
#padrao = re.findall(r"[gat]+\w+", string_de_teste)
padrao = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", requisicao.text)

if padrao:
#    print(padrao.group())
    print(padrao)
else:
    print("Padrao nao encontrado")

#Site para teste = regex101.com

#sintax para testar em emails pelo site mesmo: [\w\.-]+@[\w-]+\.[\w\.-]+
