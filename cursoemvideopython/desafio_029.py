# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

from time import sleep
usuario = str(input('Informe o seu nome: '))
carro = str(input('Informe o modelo do seu carro: '))
velocidade = int(input('Informe a velocidade do seu carro em km/h: '))
multa = (velocidade - 80) * 7
print('Analisando as informações inseridas...')
sleep(3)
if velocidade <= 80:
    print(f'Prezado {usuario} do veículo {carro}, tenha uma boa viagem!')
else:
    print(f'Prezado {usuario} do veículo {carro}, por dirigir na velocidade de {velocidade} km/h, você será multado no valor de R$ {multa:.2f} reais.')
