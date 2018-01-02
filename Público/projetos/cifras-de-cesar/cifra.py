#!/usr/bin/env python2
# -*- coding:UTF-8 -*-

abc = "abcdefghijklmnopqrstuvwxyz "

def Apresentacao():
	print("""
TESTE
""")
	opcao1 = raw_input("Opcao: ")
	if opcao1 == "1":
		ChamarBloco1()
	elif opcao1 == "2":
		ChamarBloco2()

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


def ChamarBloco1():
	c = str(raw_input('\033[32mTexo a ser cifrado\033[1;m: ')).lower()
	n = int(raw_input('\033[32mChave numérica\033[1;m: '))
	print cifrar(c, n)
	print('')

def ChamarBloco2():
	cc = str(raw_input('\033[32mTexo decifrado\033[1;m: ')).lower()
	cn = int(raw_input('\033[32mChave numérica\033[1;m: '))
	print decifrar(cc, cn)
	print('')


#if __name__ == '__main__':
#	main()

Apresentacao()