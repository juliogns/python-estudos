'''
Ex16
faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
'''
import math

print ('===== EXERCÍCIO 16 =====')
ang = float(input('Digite o ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print ('O ângulo de {}° possui\nSeno: {:.4f}\nCosseno: {:.4f}\nTangente: {:.4f}'.format(ang, sin, cos, tg))
