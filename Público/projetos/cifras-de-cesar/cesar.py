#!/usr/bin/env python3.5
# -*- coding:UTF-8 -*-

abc = "abcdefghijklmnopqrstuvwxyz"

def cifrar(palavras, chave):

	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def main():
	c = str(input('\033[32mTexo a ser cifrado\033[1;m: ')).lower()
	n = int(input('\033[32mChave numérica\033[1;m: '))
	print (cifrar(c, n))
	print('')

if __name__ == '__main__':
	main()