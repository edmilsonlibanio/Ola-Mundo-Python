# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Informe o valor do salário: R$ '))
aumento = float(input('Informe o percentual de aumento do salário: '))
calculo = salario * aumento / 100
salariofinal = salario + calculo
print(f'O salário de R$ {salario:.2f} reais acrescido de um aumento de {aumento:.0f}% terá como novo valor a quantia de R$ {salariofinal:.2f} reais.')
