from Reptil import Reptil


class Cobra(Reptil):

    @property
    def veneno(self):
        return self.__veneno

    @veneno.setter
    def veneno(self, value):
        self.__veneno = value

    @property
    def acao(self):
        return self.__acao

    @acao.setter
    def acao(self, value):
        self.__acao = value

    def __init__(self, nome, cor, idade, veneno, acao = True):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.veneno = veneno
        self.acao = acao

    def rastejar(self):
        if self.acao:
            return '{} esta rastejando'.format(self.nome)
        else:
            return '{} esta parada'.format(self.nome)

    def trocar_pele(self):
        return '{} esta trocando de pele'.format(self.nome)
