# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h exiba uma mensagem dizendo que o usuário foi multado. Nesse caso exiba o valor da multa, cobrando R$ 5,00 por km acima de 80km/h.

usuario = str(input('Informe o seu nome: '))
carro = str(input('Informe o nome do seu carro: '))
velocidade = int(input('Informe a velocidade do seu carro: '))
limiteultrapassado = velocidade - 80
multa = (velocidade - 80) * 5

if velocidade <= 80:
    print(f'Prezado {usuario} do veículo {carro}, tenha uma boa viagem!')

if velocidade > 80:
    print(f'Prezado {usuario} do veículo {carro}, você está viajando a {velocidade}km/h, {limiteultrapassado}km/h acima do limite de 80km/h permitido por lei. Por conta disso será aplicada multa de R$ {multa} pelo limite excedido.')

