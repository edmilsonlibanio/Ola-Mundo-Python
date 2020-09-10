# formatacao de strings antiga do Python
print('Hoje é dia %i.' % 15)
print('12 em octal é %o' % 12)
print('255 em hexadecimal é %x' % 255)
print('pi com duas casas decimais é aproximadamente %.2f' % 3.1415926)
print('pi com tres casas decimais é aproximadamente %.3f' % 3.1415926)
nome = 'Francisco'
print('Meu nome é %s' % nome)

# nova formatacao de strings a partir do Python 3.6 de 2016
nome = 'Francisco'
print(f'Nome do usuário: {nome}')

#nova sintaxe = f'string {expressao}'
# string = uma cadeia de de caracteres qualquer
# expressao = uma expressao valida em Python limitada por chaves
