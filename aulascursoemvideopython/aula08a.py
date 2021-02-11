# o exemplo abaixo trabalha os conceitos de importação de biblioteca na linha 2 e de raiz quadrada (sqrt) na linha 4.
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# no exemplo abaixo trabalhamos o conceito de arredondamento do resultado na linha 11.

import math
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

# no exemplo abaixo trabalhamos os conceitos de importação de funções especifica de raiz quadrada da biblioteca na linha 15. Na linha 17 notamos que se eu importei a funcionalidade especifica de sqrt no inicio, eu nao preciso repetir math.sqrt depois, porque isso já está subentendido.

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# No exemplo abaixo eu importei mais de uma funcionalidade já no topo do código.

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

