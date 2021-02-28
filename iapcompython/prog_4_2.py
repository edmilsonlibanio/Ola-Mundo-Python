# Programa: Carro Velho ou Carro Novo?

idade = int(input('Digite a idade do seu carro: '))
if idade <= 3:
    print('O seu carro é novo!')
if idade > 3:
    print('O seu carro é velho!')

#Se observarmos de perto não há um só numero que torne ambas as condições verdadeiras ao mesmo tempo. A segunda condição é responsável por decidir a impressão da mensagem do carro velho.