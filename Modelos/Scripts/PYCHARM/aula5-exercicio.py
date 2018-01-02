'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''
print('Programinha de controle de festinhas 1.0')
print('########################################')

numero_de_convidados = input('Coloque o numero de convidados: ')
lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados):
    nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('Serão', numero_de_convidados, 'convidados')

print('\nLISTA DE CONVIDADOS')
for convidado in lista_de_convidados:
    print(convidado)