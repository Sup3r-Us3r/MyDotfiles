'''
EXERCICIO: Escreva uma funcao que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa colecao
faça outra funcao que retorna o menor numero dessa coleçao
'''

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([1,-2,1.2,87.2,1289,-7,0]))

