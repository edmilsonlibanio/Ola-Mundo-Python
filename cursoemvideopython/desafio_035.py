# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo (pesquisar o princípio matemático que explica a formação de um triangulo).

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As medidas {r1}, {r2} e {r3} são capazes de formar um triângulo!')
else:
    print(f'As medidas {r1}, {r2} e {r3} não são capazes de formar um triângulo!')
