#Try = tentar | Ou seja ele vai tentar fazer algo, não quer dzer que ele vai conseguir
#Except = exeção

from time import sleep

#try:
#    a = 1200 / 0
#    dadakd()
#    a = 2/0
#    open("ARQUIVODOIDOO.TXT")


#except:
#    print("Divisao por zero, não da para fazer")

#except ZeroDivisionError:
#    print("Divisão por zero não tem como fazer")

#except NameError:
#    print("Você digitou alguma coisa errada")

#except Exception as erro:
#    print("Aconteceu algum erro:", erro)


#print("aaaaa")


def AbrirArquivo():
    try:
        arquivo = open("arquivodoido.txt")
        return True
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        return False

while not AbrirArquivo():
    print("Tentando abrir o arquivo")
    sleep(5)

print("Consegui abrir o arquivo")
