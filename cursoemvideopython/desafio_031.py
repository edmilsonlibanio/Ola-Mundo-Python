# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

usuario = str(input('Informe o seu nome: '))
distancia = int(input('Informe a distância da viagem em km/h: '))
viagemcurta = distancia * 0.50
viagemlonga = distancia * 0.45
if distancia <= 200:
    print(f'Prezado {usuario}, a sua viagem de {distancia} km terá o custo de R$ {viagemcurta:.2f} reais.')
else:
    print(f'Prezado {usuario}, a sua viagem de {distancia} km terá um custo de R$ {viagemlonga:.2f} reais.')
