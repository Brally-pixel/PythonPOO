from Reptil import Reptil


class Camaleao(Reptil):

    @property
    def inseto_favorito(self):
        return self.__inseto_favorito

    @inseto_favorito.setter
    def inseto_favorito(self, value):
        self.__inseto_favorito = value

    def __init__(self, nome, cor, idade, inseto_favorito):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} esta mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} esta comendo um inseto'.format(self.nome)
