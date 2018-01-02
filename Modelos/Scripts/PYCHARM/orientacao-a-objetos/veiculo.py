class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):    #self quer dizer que ele passa ele mesmo ali dentro
        self.cor = cor    #Quando eu iniciar esse objeto "cor" ele vai pegar a cor que eu especifiquei e vai jogar dentro do objeto self.cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros
