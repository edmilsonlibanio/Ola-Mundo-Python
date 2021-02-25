# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input('Informe o valor da mercadoria: R$ '))
desconto = float(input('Informe o percentual de desconto: '))
calculo = mercadoria * desconto / 100
descontoaplicado = mercadoria  - calculo
print(f'O produto no valor original de R$ {mercadoria:.2f} reais, aplicando-se um desconto de R$ {calculo:.2f} reais passará a custar R$ {descontoaplicado:.2f}.')
