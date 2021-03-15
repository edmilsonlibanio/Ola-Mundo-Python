# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), divisão (/) e multiplicação (*). Exiba o resultado da operação realizada.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2

operacao = str(input('Qual operação você deseja realizar, sendo: 1 - Soma, 2 - Subtração, 3 - Divisão e 4 - Multiplicação:'))

if operacao == '1':
    print(f'Resultado: {numero1} mais {numero2} é igual a {soma}.')
elif operacao == '2':
    print(f'Resultado: {numero1} menos {numero2} é igual a {subtracao}.')
elif operacao== '3':
    print(f'Resultado: {numero1} dividido por {numero2} é igual a {divisao:.5f}.')
elif operacao == '4':
    print(f'Resultado: {numero1} multiplicado por {numero2} é igual a {multiplicacao}.')
else:
    print('Operação inválida, favor escolher entre os números 1 e 4 para realizar uma operação, sendo eles: 1 - Soma, 2 - Subtração, 3 - Divisão e 4 - Multiplicação:')


# Abaixo o mesmo exercicio resolvido pelo professor Nilo Ney Coutinho Menezes de outra forma, ele evita a utilização da função print ao longo do código. Ele utilizar essa função apenas na hora de mostrar o resultado na tela. Isso bate com o que foi falado pelo Henrique Bastos na live, sobre não utilizar a função print toda hora no meio do código. Nilo Ney resolve o exercicio usando print somente no final e, principalmente, já realizando a soma das variaveis dentro do bloco de if e elif. Por fim ele também utiliza um validador de entrada para invalidar a operação caso o usuário digite outra letra aleatória que não as das opções dadas.

#a = float(input("Primeiro número:"))
#b = float(input("Segundo número:"))
#operação = input("Digite a operação a realizar (+,-,* ou /):")
#if operação == "+":
#    resultado = a + b
#elif operação == "-":
#    resultado = a - b
#elif operação == "*":
#    resultado = a * b
#elif operação == "/":
#    resultado = a / b
#else:
#    print("Operação inválida!")
#    resultado = 0
#print("Resultado: ", resultado)
