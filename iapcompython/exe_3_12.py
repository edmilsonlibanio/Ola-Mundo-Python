# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

usuario = str(input('Informe o seu nome: '))
distancia = float(input('Informe a distância do trajeto: '))
velocidade = float(input('Informe a velocidade média esperada: '))
calculo = distancia / velocidade
conversao = calculo * 60 
print(f'Prezado {usuario}, de acordo com a distância de {distancia} km e a velocidade média de {velocidade} km/h informada, o tempo estimado para a viagem será de {conversao} minutos.')

# Na linha 7 estou convertendo o percentual da divisão para hora/calculo (por isso multipliquei o resultado por 60 minutos).