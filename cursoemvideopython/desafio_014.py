c = float(input('Insira a temperatura em °C: '))
f = (c * 1.8 + 32)
k = (c + 273)
print('{}°C na escala Fahrenheit corresponde a: {:.1f}°F'.format(c, f))
print('{}°C na escala Kelvin corresponde a: {:.1f}°K'.format(c, k))