# Escreva um programa que converta uma temperatura digitada e graus Celsius para Fahrenheit.

celsius = int(input('Informe uma temperatura em graus Celsius: '))
conversao = celsius * 1.8 + 32
print(f'{celsius} graus Celsius corresponde a {conversao:.0f} graus Fahrenheit.')
