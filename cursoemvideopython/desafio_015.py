km = float(input('Qual a km percorrida? '))
dias = int(input('Em quantos dias de aluguel? '))
kmvalor = km * 0.15
diariavalor = dias * 60.00
total = diariavalor + kmvalor
print('O valor total a pagar por {} dias de aluguel e {:.2f} kilometros 
rodados é R$ {:.2f} '.format(dias, km, total))
