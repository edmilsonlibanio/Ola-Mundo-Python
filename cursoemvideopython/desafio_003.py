# Desafio nº 3 - Crie um script Python que leia dois números e mostre a soma entre eles.

n1 = int(input('Insira um número:'))
n2 = int(input('Insira outro número:'))
s = n1+n2
#print('A soma dos números informados é',s) ***sintaxe antiga***
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
