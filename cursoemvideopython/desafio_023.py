# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
# Tentar fazer isso como string e também matematicamente, para daí decidir qual forma se adapta melhor à minha necessidade.

# A forma de resolução abaixo foi feita trabalhando-se com string, na verdade convertemos uma variável inteira para string e pedimos para o programa mostrar o índice dessa string (0,1,2,3). Entretanto, esta forma de resolução tem um problema quando digitamos um número com apenas 3 ou 2 caracteres. Nesse caso o Python dá erro. Para evitar este problema a proxima forma de resolver o problema será feita pelo método matemático.

#numero = int(input('Insira um número: '))
#n = str(numero)
#print(f'Analisando o número {numero}...')
#print(f'Unidade: {n[3]}')
#print(f'Dezena: {n[2]}')
#print(f'Centena: {n[1]}')
#print(f'Milhar: {n[0]}')

# Método matemático de resolução desse problema não teremos o mesmo problema apresentado na solução em que tratamos os números como strings.

numero = int(input('Insira um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Analisando o número {numero}...')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')


