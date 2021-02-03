preco = float(input('Informe o valor do produto:R$ '))
desconto = (preco * 5 / 100)
vfinal = (preco - desconto)
print('Considerando o desconto de {:.0f}%, o seu produto passa de R$ {:.2f} para R$ {:.2f}.'.format(desconto, preco, vfinal))