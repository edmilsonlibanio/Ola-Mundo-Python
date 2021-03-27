# Escreva um programa que leia dois numeros, imprima o resultado da multiplicação  do primeiro pelo segundo. Utilize apenas os operadores de soma e subtraçao para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4x5 seria 5 + 5 + 5 + 5 = 4 +4 + 4 +4 +4.

primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))
x = 1
r = 0
while x <= segundo:
    r = r + primeiro
    x = x + 1
print(f"{primeiro} x {segundo} = {r}")

