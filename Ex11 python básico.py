'''
Ex11
faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m².
'''


print ('===== EXERCÍCIO 11 =====')
a = float(input('Digite altura da parede em metros: '))
l = float(input('Digite largura da parede em metros: '))
area = a * l
tinta = area / 2
print ('Para pintar uma área de {}m² é necessário {}L de tinta'.format(area, tinta))
