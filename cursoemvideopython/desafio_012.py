preco = float(input('Informe o preço do produto: R$ '))
novopreco = preco - (preco*5/100)
print('O produto que custava originalmente R$ {:.2f}, com 5% de desconto passa a custar R$ {:.2f}.'.format(preco, novopreco ))
