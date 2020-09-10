n1 = input('Digite algo:')
print('O tipo primitivo digitado é:',type(n1))
print('Só tem espaços?',n1.isspace())
print('É um número?',n1.isalnum())
print('É alfabético?',n1.isalpha())
print('É alfanumérico?',n1.isalpha())
print('Está em letras maiúsculas?',n1.isupper())
print('Está em letras minúsculas?',n1.islower())
print('Está capitalizada?',n1.istitle())



#n1 = input('Digite algo:')
#print(f'O tipo primitivo digitado é:'{type(n1)}')
#print(f'Só tem espaços?'{n1.isspace()}')
#print(f'É um número?'{n1.isalnum()}')
#print(f'É alfabético?'{n1.isalpha()}')
#print(f'É alfanumérico?'{n1.isalpha()}')
#print(f'Está em letras maiúsculas?'{n1.isupper()}')
#print(f'Está em letras minúsculas?'{n1.islower()}')
#print(f'Está capitalizada?'{n1.istitle()}')
#No Python 3.7, não precisa colocar o .format() no final, basta colocar "f" na frente das aspas e inserir os valores dentro dos colchetes, como está acima.