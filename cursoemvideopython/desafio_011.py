altura = float(input('Informe em metros a altura da parede que voce deseja pintar: '))
largura = float(input('Informe em metros a largura da parede que voce deseja pintar: '))
area = (altura*largura)
litro = 2
tinta = (area/litro)
print('Sua parede tem as dimensões de {}x{} e area de {:.2f}m².'.format(altura, largura, area))
print('Para pintar a parede serão necessários {:.2f} litros de tinta.'.format(tinta))
