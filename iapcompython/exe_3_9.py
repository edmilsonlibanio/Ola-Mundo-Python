dia = int(input('Informe a quantidade de dias: '))
horas = int(input('Informe a quantidade de horas: '))
# Escreve um programa que leia a quantidade de dias, horas, minutos e segundos fornecidos pelo usuário. Ao final calcular o total em segundos.

minutos = int(input('Informe a quantidade de minutos: '))
segundos = int(input('Informe a quantidade de segundos: '))
diacalculo = dia * 24 * 60 * 60
horascalculo = horas * 60 * 60
minutoscalculo = minutos * 60
totalsegundos = diacalculo + horascalculo + minutoscalculo + segundos
print(f'{dia} dia corresponde a {diacalculo} segundos.')
print(f'{horas} horas correspondem a {horascalculo} segundos.')
print(f'{minutos} minutos correspondem a {minutoscalculo} segundos.')
print(f'{segundos} segundos correspondem a {segundos} segundos.')
print(f'Todos os valores inseridos totalizam {totalsegundos:.0f} segundos.')
