#!/usr/bin/env python3
#coding: utf-8

import requests
import json

def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?t=" + titulo + "&type=movie")
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro na conexão")
        return None

def nomedofilme():
    opcao = input("Nome do filme: ")
    filme = requisicao(opcao)
    if filme["Response"] == "False":
        print("Filme não encontrado")
    else:
        printar_detalhes(filme)


def printar_detalhes(filme):
    print(filme)
    print("\n\n\n")
    print("Title:", filme["Title"])
    print("Year:", filme["Year"])
    print("Rated:", filme["Rated"])
    print("Released:", filme["Released"])
    print("Runtime:", filme["Runtime"])
    print("Genero:", filme["Genre"])
    print("Director:", filme["Director"])
    print("Actors:", filme["Actors"])
    print("Plot:", filme["Plot"])
    print("Language:", filme["Language"])
    print("Country:", filme["Country"])
    print("Awards", filme["Awards"])
    print("Metascore:", filme["Metascore"])
    print("imdbRating:", filme["imdbRating"])
    print("imdbVotes:", filme["imdbVotes"])
    print("imdbID:", filme["imdbID"])
    print("Type:", filme["Type"])
    print("Poster", filme["Poster"])
    print("")


nomedofilme()