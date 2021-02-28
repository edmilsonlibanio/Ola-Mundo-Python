# Escreva um programa  que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00  calcule um aumento de 10%. Para os inferiores ou iguais, um aumento de 15%.

funcionario = str(input('Informe o nome do funcionário: '))
salario = float(input('Informe o salário do funcionário: '))
aumento10 = salario * 10 / 100
aumento15 = salario * 15 / 100
salariofinal10 = salario + aumento10
salariofinal15 = salario + aumento15

if salario <= 1250:
    print(f'Funcionário: {funcionario} Salário: {salario:.2f} Aumento: {aumento15:.2f} Novo Salário: {salariofinal15:.2f}')

if salario > 1250:
    print(f'Funcionário: {funcionario} Salário: {salario:.2f} Aumento: {aumento10:.2f} Novo Salário: {salariofinal10:.2f}')
