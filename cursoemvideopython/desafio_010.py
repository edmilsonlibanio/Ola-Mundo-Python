# Desafio nº 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (considerar 1 dólar  a 3,27). 

saldo = float(input('Quanto dinheiro voce tem em carteira? R$ '))
dolar = 3.27
conversao = (saldo/dolar)
print('Com R$ {:.2f} reais é possivel adquirir {:.2f} dólares americanos a uma cotação de US$ 3.27 em relação ao real.'.format(saldo, conversao))
