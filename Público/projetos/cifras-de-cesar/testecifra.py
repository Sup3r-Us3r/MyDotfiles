#!/usr/bin/env python2
# -*- coding:UTF-8 -*-

import os

abc = "abcdefghijklmnopqrstuvwxyz "


def Apresentacao():
	print("""
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar.

\033[31m1\033[1;m) Encode - Cifra de César
\033[31m2\033[1;m) Decode - Cifra de César
""")
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		main()
	elif opcao1 == "2":
		main2()

def cifrar(palavras, chave):

	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def decifrar(palavras, chave):

	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def main():
	c = str(raw_input('\033[32mTexo a ser cifrado\033[1;m: ')).lower()
	n = int(raw_input('\033[32mChave numérica\033[1;m: '))
	print cifrar(c, n)
	print('')

def main2():
	cc = str(raw_input('\033[32mTexo decifrado\033[1;m: ')).lower()
	cn = int(raw_input('\033[32mChave numérica\033[1;m: '))
	print decifrar(cc, cn)
	print('')

if __name__ == '__main__':
	main()

Apresentacao()