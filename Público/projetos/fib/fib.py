#!/usr/bin/env python3.5
#coding: utf-8

import argparse
import sys
 
def fib(n):
    """
    Função usada para calcular o enésimo termo
    da sequência de fibonacci
    """
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
 
    return a
 
def main():
    """
    Função principal do programa
    """
    #Primeiro nós criamos o objeto que irá lidar com argumentos
    parser = argparse.ArgumentParser(description="Exemplo de Argparse")
 
    #Truquezinho
    #Truque didático para colocar argumentos que executará o código de acordo com o trecho da aula
    part = 3
 
    if part == 1:
        part1(parser)
    elif part == 2:
        part2(parser)
    elif part == 3:
        part3(parser)
    else:
        part4(parser)
 
def part1(parser):
    """
    Função da primeira parte da aula
    """
    #Depois podemos colocar os argumentos
    parser.add_argument("num", help="Número da sequência de Fibonacci que se deseja obter", type = int)
    #Primeiro argumento = Nome do argumento
    #Argumento opcional help = Descrição do argumento
    #Argumento opcional type = Garante que o argumento recebido será daquele tipo
 
    #Depois nós pegamos os argumentos colocados na linha de comando
    args = parser.parse_args()
 
    #Obtemos o resultado
    resultado = fib(args.num)
 
    #E o imprimimos na tela
    print("O", args.num, "da sequência de fibonacci é", resultado)
 
 
def part2(parser):
    """
    Função da segunda parte da aula
    """
    #Depois podemos colocar os argumentos
    parser.add_argument("num", help="Número da sequência de Fibonacci que se deseja obter", type = int)
 
    #Podemos colocar também o argumento opcional output
    parser.add_argument("-o","--output",help="Manda a saída do programa para um arquivo separado", action="store_true")
    #Primeiro argumento = Nome resumido da flag/argumento opcional
    #Segundo argumento = Nome completo da flag/argumento opcional
    #Action = Ação a ser executado se esse argumento aparecer, no caso store_true vai colocar
    #o valor booleano true no argumento output
 
    #Depois nós pegamos os argumentos colocados na linha de comando
    args = parser.parse_args()
 
    #Obtemos o resultado
    resultado = fib(args.num)
 
    #E o imprimimos na tela
    if args.output:
        arq = open("fib.txt", 'w')
        sys.stdout = arq
 
    print("O", args.num, "da sequência de fibonacci é", resultado)
 
def part3(parser):
    """
    Função da terceira parte da aula
    """
    #Depois podemos colocar os argumentos
    parser.add_argument("num", help="Número da sequência de Fibonacci que se deseja obter", type = int)
 
    #Podemos colocar também o argumento opcional output
    parser.add_argument("-o","--output",help="Manda a saída do programa para um arquivo separado", action="store_true")
 
    #Adicionar grupo mutuamente exclusivo
    grupo = parser.add_mutually_exclusive_group()
 
    #Adicionamos um modo de saída do tipo verbose ou quiet ao grupo
    #logo o usuário é obrigado a escolher um mode específico de saída
    grupo.add_argument("-v", "--verbose", help = "Imprime a saída no modo verbose", action="store_true")
    grupo.add_argument("-q", "--quiet", help = "Imprime a saída no modo quiet", action="store_true")
 
 
    #Depois nós pegamos os argumentos colocados na linha de comando
    args = parser.parse_args()
 
    #Obtemos o resultado
    resultado = fib(args.num)
 
    #E o imprimimos na tela
    if args.output:
        arq = open("fib.txt", 'w')
        sys.stdout = arq
 
    #Escolhemos também o modo de saída
    if args.verbose:
        print("O", args.num, "da sequência de fibonacci é", resultado)
    elif args.quiet:
        print(resultado)
    else:
        print("Fib("+str(args.num)+") =", resultado)
 
def part4(parser):
    """
    Função da quarta parte da aula
    """
    #Depois podemos colocar os argumentos
    parser.add_argument("num", help="Número da sequência de Fibonacci que se deseja obter", type = int)
 
    #Podemos colocar também o argumento opcional output, só que agora especificaremos um local de saída
    parser.add_argument("-o","--output",help="Manda a saída do programa para um arquivo especificado", action="store")
 
    #Adicionar grupo mutuamente exclusivo
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument("-v", "--verbose", help = "Imprime a saída no modo verbose", action="store_true")
    grupo.add_argument("-q", "--quiet", help = "Imprime a saída no modo quiet", action="store_true")
 
 
    #Depois nós pegamos os argumentos colocados na linha de comando
    args = parser.parse_args()
 
    #Obtemos o resultado
    resultado = fib(args.num)
 
    #E o imprimimos na tela
    if args.output != None:
        arq = open(args.output, 'w')
        sys.stdout = arq
 
    #Escolhemos também o modo de saída
    if args.verbose:
        print("O", args.num, "da sequência de fibonacci é", resultado)
    elif args.quiet:
        print(resultado)
    else:
        print("Fib("+str(args.num)+") =", resultado)
 
 
if __name__ == '__main__':
    main()
