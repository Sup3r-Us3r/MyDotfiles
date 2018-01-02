#!/usr/bin/env python3.5
#coding: utf-8

#Para criar uma lista basta abrir um colchete []

frase = "Oi, tudo bem?"
print(frase[1])

frase = "Oi, Tudo Bem?"
lista_nomes = ["Magno", "Tutor", "Sup3r", "Sup3r", "Toor"]
#print(type(lista_nomes))


print(lista_nomes[0])
print(frase[0:9])
print(frase[0:13:2])
#
print(lista_nomes[0:2])
print(lista_nomes[-1])
print(lista_nomes[-1:-5:-1])
print(frase[::-1])

#lista_nomes.append("Us3r") #O APPEND sempre insere no ultmo lugar da lista
#lista_nomes.append("Teste")
#lista_nomes.append("Fim")

#lista_nomes.remove("Toor")
#lista_nomes.clear()
#lista_nomes.insert(1, "Testando")

#lista_nomes[0] = "Castrivania"

#contador_sup3r = lista_nomes.count("Sup3r")

#print(lista_nomes)
#print(contador_sup3r)

#print(len(frase)) #Quantos caracteres tem

#print(lista_nomes.pop()) #Contao ultimo caracter
#print(lista_nomes) #Se eu imprimir o lista_nomes.pop ele ira pegar o ultimo da lista imprimir e retirar ele da lista também


#print(frase.lower()) #Transforma tudo em minusculo
#print("\n")
#print(frase.upper()) #Transforma tudo em maiusculo

#frase_separada = frase.split(",") #Transforma tudo em uma lista (muito util)
#print(frase_separada)
#print("\n")
#print(frase_separada[0])


#frase_nova = frase + " Como vai você?"
#print(frase_nova)