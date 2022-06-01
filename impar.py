# Módulos
from random import choice

# Tamanho
tamanho = 8

lista = list()

# Lista
numeros = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25)

sorteados = set()

while len(sorteados) < tamanho:
    sorteados.add(choice(numeros))
    """ OBS: O set não permite valores repetidos. """
    lista.sort()
    """ OBS: O sort() ordena a lista. """
print(sorteados)
""" OBS: O print() imprime o resultado. """
