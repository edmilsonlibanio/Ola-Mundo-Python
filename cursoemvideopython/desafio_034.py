# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais o aumento é de 15%.

nome = str(input('Informe o seu nome: '))
salario = float(input('Informe o seu salário: '))
salariomaior = (salario * 10) / 100
salariomenor = (salario * 15) / 100

if salario >= 1250:
    print(f'Prezado {nome}, o seu salário de R$ {salario:.2f} acabou de receber um aumento de 10%. Dessa forma, a partir do próximo mês ele será de R$ {salario + salariomaior:.2f} reais.')
else:
    print(f'Prezado {nome}, o seu salário de R$ {salario:.2f} acabou de receber um aumento de 15%. Dessa forma, a partir do próximo mês eleserá de R$ {salario + salariomenor:.2f} reais.')
