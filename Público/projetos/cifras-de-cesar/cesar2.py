#!/usr/bin/env python3.5
# -*- coding:UTF-8 -*-

abc = "abcdefghijklmnopqrstuvwxyz"

def decifrar(palavras, chave):

	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def teste():
	cc = str(input('\033[32mTexto para decifrar\033[1;m: ')).lower()
	cn = int(input('\033[32mChave numérica\033[1;m: '))
	print (decifrar(cc, cn))
	print('')

if __name__ == '__main__':
	teste()