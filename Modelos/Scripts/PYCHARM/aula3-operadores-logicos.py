#Um = só é para atribuição de variaveis ou seja é para pegar um valor só e jogar dentro da variavel
#Dois == é para você pegar um valor e comparar com o outro
#Comparações: == != > < >= <= and or
# IF = SE | ELSE = SENÃO | ELIF = SENÃO SE
# not = Ele vai negar tudo que for True ele vai transformar em False e tudo que for False ele vau transformar em True

#var_verdade = True #Boolean ou booleano
#var_falso = False

#print(type(var_verdade), type(var_falso))
#print(var_falso, "&",var_verdade)

#if var_verdade == True:
#    print("var_verdade é verdadeiro")

#if 2 > 1:
#    print("2 é menor do que um")

#a = 50
#b = 30

#if a > b and "abacaxi" == "abacaxi":
#    print(a, "é maior do que", b, "e", "abacaxi é igual a abacaxi")
#else:
#    print("Não funfo o if :|")


#if ((a>b) and ("abacaxi" == "abacaxi")) or 2 == 1:
#    print("Tudo verdade")
#else:
#    print("Não foi dessa vez")

########
# MENU #
########

#MANEIRA ERRADA DE SE CRIAR UM MENU
#print("Opções:\n 1 = Escreve Magno\n 2 = Escreve Tutor\n 3 = Escreve Toor\n 4 = Volte ao menu")
#opcao = input("Escolha uma opção: ")
#if opcao == "1":
#    print("Magno")
#if opcao == "2":
#    print("Tutor")
#if opcao == "3":
#    print("Toor")
#if opcao == "4":
#    print("Ok mano")

#MANEIRA CERTA DE SE CRIAR UM MENU

#print("Opções:\n 1 = Escreve Magno\n 2 = Escreve Tutor\n 3 = Escreve Toor\n 4 = Volte ao menu")
#opcao = input("Escolha uma opção: ")
#if opcao == "1":
#    print("Magno")
#elif opcao == "2":
#    print("Tutor")
#elif opcao == "3":
#    print("Toor")
#elif opcao == "4":
#    print("Ok mano")
#else:
#    print("Opção invalida")

#print(not True)
#print(not False)

#idadade = 50
#if not idadade == 50:
#    print("Você não tem 50 anos")
#else:
#    print("Você tem 50 anos")

#if True:
#    print("Você entrou no if")
#else:
#    print("Você entrou no else")

###########
#EXERCICIO#
###########
'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos
pesar mais ou igual  60 kilos
e medir mais ou igual 1,70 metros
'''

idade = input("Qual sua idade: ")
peso = input("Qual seu peso: ")
altura = input("Qual sua altura: ")
print("\n")
print("Será que você está apta a entrar no exercito ?\nSua idade é:", idade,"\nSeu peso é:", peso, "\nE sua altura é de:", altura)
print("\n")

if idade >= "18" and peso >= "60" and altura >= "1.70":
    print("Parabéns você está pronto para ir para o exercito.")
else:
    print("Não foi dessa vez, mais não desista quem busca sempre alcança.")


