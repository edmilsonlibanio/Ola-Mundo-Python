nome = input('Qual é o seu nome? ')
salario = int(input('Informe o seu salário: R$ '))
novosalario = salario + (salario * 15 / 100)
print('Parabéns {}, \nVocê recebeu um reajuste salarial de 15%. Com isso, o seu salário passa de R$ {:.2f} para R$ {:.2f} à partir do próximo mês!'.format(nome, salario, novosalario))
