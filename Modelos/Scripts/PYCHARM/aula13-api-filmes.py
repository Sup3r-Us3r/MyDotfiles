import requests
import json

def requisicao(titulo):

    try:
        req = requests.get("http://www.omdbapi.com/?t=" + titulo + "&type=movie")
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro na conexao")
        return None

def printar_detalhes(filme):
    print(filme)
    print("\n\n\n")
    print("Genero:", filme["Genre"])
    print("Titulo:", filme["Title"])
    print("Ano:", filme["Year"])
    print("Diretor:", filme["Director"])
    print("Atores:", filme["Actors"])
    print("Nota:", filme["imdbRating"])
    print("Premios", filme["Awards"])
    print("Poster", filme["Poster"])
    print("")

sair = False
while not sair:
    opcao = input("Escreva um nome de um filme ou SAIR para fechar: ")
    if opcao == "SAIR":
        sair = True
        print("Saindo")
    else:
        filme = requisicao(opcao)
        if filme["Response"] == "False":
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)

'''

req = None

print(req.text)

dicionario = json.loads(req.text)

print(dicionario)
print("")
print("Titulo:", dicionario["Title"])
print("Ano:", dicionario["Year"])
print("Diretor:", dicionario["Director"])
print("Atores:", dicionario["Actors"])
print("Nota:", dicionario["imdbRating"])

'''