from Reptil import Reptil


class Jacare(Reptil):

    @property
    def num_dentes(self):
        return self.__num_dentes

    @num_dentes.setter
    def num_dentes(self, value):
        self.__num_dentes = value

    def __init__(self, nome, cor, idade, num_dentes):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.num_dentes = num_dentes

    def atacar(self):
        if self.num_dentes > 10:
            return '{} esta atacando!!!!'.format(self.nome)
        else:
            return '{} nao vai atacar, fica tranquilo'.format(self.nome)

    def dormir(self):
        return '{} esta dormindo zzz'.format(self.nome)
