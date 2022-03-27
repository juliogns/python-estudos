'''
Ex15
faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
'''
import math

print ('===== EXERCÍCIO 15 =====')
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))
print ('A hipotenusa é {}'.format(hi))
