#!/usr/bin/env python3.5
#coding: utf-8

import getpass
import hashlib #O modulo md5 e considerado obsoleto na versao 2.6
import os


def bloco_iniciar():

	print("Entre com a senha") 
	p = True
	q = False

	while p != q:
		p = getpass.getpass()
		p = hashlib.md5(p)
		p = p.hexdigest()
		q = "e10adc3949ba59abbe56e057f20f883e" #MD5 de '123456'
		os.system("clear")
		if p != q:
			print("Incorreto")
	print("Bem vindo!")
	input()

bloco_iniciar()



'''
#!/bin/env python2

import getpass
import hashlib #O modulo md5 e considerado obsoleto na versao 2.6
import os


def bloco_iniciar():

	print("Entre com a senha") 
	p = True
	q = False

	while p != q:
		p = getpass.getpass()
		p = hashlib.md5(p)
		p = p.hexdigest()
		q = "e10adc3949ba59abbe56e057f20f883e" #MD5 de '123456'
		os.system("clear")
		if p != q:
			print("Incorreto")
	print("Bem vindo!")
	raw_input()

bloco_iniciar()
'''