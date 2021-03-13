# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas; - O nome com todas as letras minúsculas; - Quantas letras ao todo sem considerar os espaços; e  - Quantas letras tem o primeiro nome.

nome = str(input('Informe o seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é: {nome.upper()}.')
print(f'Seu nome em letras minúsculas é: {nome.lower()}.')
print('O seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))