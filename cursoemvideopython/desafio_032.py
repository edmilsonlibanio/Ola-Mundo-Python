# Faça um programa que leia um ano qualquer e mostre se ele é bissexto (estudar o que é ou o que significa isso).

ano = int(input('Informe a seguir um ano no formato ****: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
