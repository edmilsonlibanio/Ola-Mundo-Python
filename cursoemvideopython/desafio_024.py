# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra ‘’Santo’’.

cidade = str(input('Informe o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
