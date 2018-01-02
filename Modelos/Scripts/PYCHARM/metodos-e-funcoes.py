#Def = Definir uma função

#def soma(numero1, numero2):
#    resposta = numero1 + numero2
#    return resposta

#retorno = soma(12.35, 30.70)
#print(retorno)

#################################

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
print(tem_sete_itens("Oi pessoal"))

if tem_sete_itens("1234567"):
    print("Realmente tem 7 itens")