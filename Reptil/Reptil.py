class Reptil():

    @property
    def nome(self):
        return self.__nome
    @property
    def cor(self):
        return self.__cor
    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @cor.setter
    def cor(self, value):
        self.__cor = value

    @idade.setter
    def idade(self, value):
        self.__idade = value

    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.idade = idade
        self.cor = cor

    def tomar_sol(self):
        return '{} esta tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)
