# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.

passageiro = str(input('Nome do passageiro: '))
distancia = int(input('Informe a distância da viagem em km: '))
trechocurto = distancia * 0.50
trecholongo = distancia * 0.45 
if distancia <= 200:
    print(f' Prezado {passageiro}, o percurso de {distancia} km corresponde a uma corrida de R$ {trechocurto:.2f} reais.')
else:
    print(f'Prezado {passageiro}, o percurso de {distancia} km corresponde a uma corrida de R$ {trecholongo:.2f} reais.')
