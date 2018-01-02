#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Cifra de César com lista.

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nome = list(input('Digite o nome: '))
salto = int(input('Valor do salto: '))
cont = 0
lista = []
cifra = []

while cont < salto: #Insere o valor 0, na posição 0 da lista alfabeto.
	cont += 1
	alfabeto.insert(0,0)
for i in range(len(nome)): #Compara os caracteres inserido com a lista alfabeto atualizada com o salto e armazena o valor na lista.
	for j in range(len(alfabeto)):
		if nome[i] == alfabeto[j]:
			lista.append(j)
while cont != 0: #Remove os valores 0 inseridos para poder imprimir a cifra.
	cont -= 1
	alfabeto.remove(0)
for n in range(len(lista)):
	for m in range(len(alfabeto)):
		if lista[n] > 25: #Se o valor armazenado na lista for maior que 25 ele simplesmente não e identificado, assim a lista se "repete".
			lista[n] -= 25
		elif lista[n] == m:
			cifra.append(alfabeto[m])
print("".join(cifra))
