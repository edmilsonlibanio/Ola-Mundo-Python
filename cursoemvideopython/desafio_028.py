# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
usuario = int(input('Em que número eu pensei? '))
print('Analisando...')
sleep(2)
if usuario == computador:
    print(f'Parabéns, você e o computador escolheram o mesmo número {usuario}')
else:
    print(f'Que pena, você escolheu o número {usuario} e o computador o número {computador}, eu ganhei!')
 
