#!/usr/bin/env python3.6
# -*- coding: utf8 -*- 

print('''
MD5 SHA1 SHA224 SHA256 SHA384 SHA512


[+] Quebra de Hash's

''')
import hashlib
import argparse


argumentos = argparse.ArgumentParser()
argumentos.add_argument('--tipo', action = 'store', dest = 'tipo', required = True, help = '''
1 = MD5
2 = SHA1
3 = SHA224
4 = SHA256
5 = SHA384
6 = SHA512
''')
argumentos.add_argument('--hash', action = 'store', dest = 'hash', required = True, help = 'Hash que você deseja quebrar')
argumentos.add_argument('--wlist', action = 'store', dest = 'wordlist', required = True, help = 'Caminho da Wordlist (Ex.: C:\wordlist.txt )')
arg = argumentos.parse_args()


text = open(arg.wordlist)
busca = str(arg.hash).lower()
opcode = 0
temp = ''

hashFunc = None
if arg.tipo == '1':
    hashFunc = hashlib.md5
elif arg.tipo == '2':
    hashFunc = hashlib.sha1
elif arg.tipo == '3':
    hashFunc = hashlib.sha224
elif arg.tipo == '4':
    hashFunc = hashlib.sha256
elif arg.tipo == '5':
    hashFunc = hashlib.sha384
elif arg.tipo == '6':
    hashFunc = hashlib.sha512


for x in text:
    temp = hashFunc(x.rstrip().encode('utf-8')).hexdigest()
    if busca == temp:
        print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
            hash = busca, text = x, xD = ('-'*30)))
        opcode = 1
        break
text.close()
if opcode == 0:
    print('Valor não encontrado, tente com uma wordlist mais completa ;)')
else:
    print('Finalizado')
