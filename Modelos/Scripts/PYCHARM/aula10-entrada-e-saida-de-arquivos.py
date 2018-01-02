#!/usr/bin/env python3.5

#Quando eu abro no modo "w" é write modo de escrita 
#Modulo "r" é read ler | "r+"" lê e escreve
#Modulo "a" é modo de escrita so que append ou seja ele sempre vai jogar as coisas no final do arquivo
#Modulo "b" para abrir outras coisas 
#Modulo "rb" ler algo como imagem

#arquivo = open("arquivo.txt", "a") 
#arquivo = open("arquivo.txt", "r") 

#type(print(arquivo))

#arquivo.write("E ai pessoal, firmao?")

#for i in range(0, 10000):
#	arquivo.write("bbbbb "+str(i)+"\n")

#print(arquivo.read())

#for linha in arquivo:
#	print(linha)


arquivo = open("spypass.png", "rb") 
print(arquivo.read())