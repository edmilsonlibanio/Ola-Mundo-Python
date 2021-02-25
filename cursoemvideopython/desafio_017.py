# Desafio nº 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catoposto = float(input('Informe a medida do cateto oposto do triângulo retângulo: '))
catadjacente = float(input('Informe a medida do cateto adjacente do triângulo retângulo: '))
hipotenusa = hypot (catoposto, catadjacente)
print('Um triângulo retângulo com cateto adjacente medindo {} e cateto oposto medindo {}, tem em sua hipotenusa o valor de {:.2f}.'.format(catadjacente, catoposto, hipotenusa))
