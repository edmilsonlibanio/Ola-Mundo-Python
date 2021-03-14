# Crie um programa que leia o nome completo de uma pessoa e diga se ela tem ‘’Silva’’ no nome.

#nome = str(input('Informe o seu nome completo: ')).strip()

#if 'Silva' in nome:
 #   print(f'O seu nome tem o sobrenome Silva!')
#else:
 #   print(f'O seu nome não tem Silva como sobrenome.')

# O programa acima resolve o exercício, entretanto, o programa vai diferenciar letras maiúsculas e minúsculas. Sendo assim, se tiver um ou outro caractere escrito de forma UPPER or lower o programa vai dar erro.

# Para evitar esse problema o Gustavo Guanabara passou a seguinte solução de código:

nome = str(input('Informe o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

# Na resolução acima a função da linha 15 vai jogar todos os caracteres da string para maiúsculo (UPPER) ou minúsculo (lower) e depois disso fazer a busca da palavra dentro da string.


