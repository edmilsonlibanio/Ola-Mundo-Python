# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kwh consumida e o tipo de instalção: 'R', 'I' para indústrias e 'C' para Comércios. Calcule o preço a pagar de acordo com a tabela a seguir (tabela consta na página 83 do livro):

consumo = int(input('Informe a quantidade de kWh consumida no mês:'))

instalacao = str(input('Informe o tipo de instalação, sendo: R para residências, I para indústrias e C para comércios: '))

if instalacao == 'R':
    if consumo <= 500:
        tarifa = 0.40
    else:
        tarifa = 0.65
elif instalacao == 'I':
    if consumo <= 1000:
        tarifa = 0.55
    else:
        tarifa = 0.60
elif instalacao == 'C':
    if consumo <= 5000:
        tarifa = 0.55
    else:
        tarifa = 0.60
else:
    tarifa = 0
    print('Tipo de instalação inválida, favor selecionar: R para residências, I para indústrias e C para comércios')

custofinal = consumo * tarifa

print(f'O valor total a pagar é R$ {custofinal:.2f} reais.')
