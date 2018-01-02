from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo("rosa", 6, "ford", 10)
print(caminhao_rosa)
print(type(caminhao_rosa))

print("\n")

print("CAMINHAO ROSA")
print("Cor:", caminhao_rosa.cor)
print("Marca:", caminhao_rosa.marca)
print("Rodas:", caminhao_rosa.rodas)
print("Tanque:", caminhao_rosa.tanque)

print("\n")

print("CARRO AZUL")
carro_azul = Carro("azul", "bmw", 30)

print("Cor:", carro_azul.cor)
print("Marca:", carro_azul.marca)
print("Rodas:", carro_azul.rodas)
print("Tanque:", carro_azul.tanque)
carro_azul.abastecer(35)
print("Tanque:", carro_azul.tanque)

caminhao_rosa.abastecer(100)
print("Tanque:", caminhao_rosa.tanque)