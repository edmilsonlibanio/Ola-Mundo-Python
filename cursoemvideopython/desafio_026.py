# Faça um programa que leia uma frase qualquer pelo teclado e mostre:
# Quantas vezes a letra ‘’a’’ aparece;
# Em que posição ela aparece a primeira vez; e
# Em que posição ela aparece a última vez.

frase = str(input('Insira uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} da frase.'.format(frase.find('A')+1))
print('A letra A aparece pela última vez na posição {} da frase.'.format(frase.rfind('A')+1))
