#For = Para cada objeto dentro de uma coleção você executa tal coisa | In = Dentro
#While = Significa enquanto

#nomes = ["Magno", "Tutor", "Sup3r", "Us3r"]
#print(nomes[0])

#Para cada nome dentro de nomes me mostre um nome
#for nome in nomes:
#    print(nome)


#lista_de_numeros = range(5, 10)
#lista_de_numeros2 = range(0, 100, 2)

#for item in lista_de_numeros:
#    print(item)

#for item in lista_de_numeros2:
#    print(item)


#for item in range(0, 20, 2):
#    print(item)

#for item in range(4):
#    print(nomes[item])

#for i in nomes:
#    print(i)

#for i in range(len(nomes)):
#    print(nomes[i])
#    nomes.append("OII")
#print(nomes)

#palavra = "Magno Tutor"
#for letra in palavra:
#    print(letra)

#i = 0 #Nesse momento i = 0
#i = i + 10 # i = 0 e vai somar 10 e jogar novamente na variavel i
#esse i do meio é o i que vale 0
#i = i + 10
#ou desse jeito
#i += 1

#print(i)

#while i < 10:
#    print("i ainda é menor que 10: ", i)
#    i = i + 1 #Somei mais 1 no i

#print("Acabou o while", i)
#while = true se cair no false ele acaba o while

#while True:
#    print("Loop infinito: ", i)
#    i = i + 1

lista_frutas = ["Maça", "Pera", "Uva", "Abacaxi", "Goiaba"]
contator = 0
for fruta in lista_frutas:
    contator += 1
print(contator) #Jeito complexo de se fazer :P

print("\n")
print(len(lista_frutas)) #Jeito fácil

###break = parar

numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1