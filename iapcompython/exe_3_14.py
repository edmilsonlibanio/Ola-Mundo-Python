# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

usuario = str(input('Informe o seu nome: '))
carro = str(input('Informe o nome do carro: '))
km = int(input('Informe a quilometragem total percorrida: '))
diarias = int(input('Informe o total de diários do veículo: '))
valordiarias = (diarias * 60.00)
valorkm = (km * 0.15)
valortotal = valordiarias + valorkm

print(f'Prezado {usuario}, obrigado pelo aluguel do veículo {carro}. A quilometragem total percorrida foi de {km} km durante {diarias} dias.')

print(f'O valor total das diárias corresponde a R$ {valordiarias:.2f}, e a quilometragem total corresponde a R$ {valorkm:.2f}.')

print(f'Diante disso, o valor total a pagar é R$ {valortotal:.2f}.')