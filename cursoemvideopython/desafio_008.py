# Desafio nº 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

distancia = float(input('Insira um número em metros: '))
centimetros = distancia*100
milimetros = distancia*1000
print('A medida de {:.0f} metros corresponde a: \n{:.0f} centímetros  \n{:.0f} milímetros!'.format(distancia, centimetros, milimetros))
