'''
Ex8
escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
'''


print ('===== EXERCÍCIO 8 =====')
me = float(input ('Digite um valor em metros: '))
c = round(me * 100)
mi = round(me * 1000)
print ('\nO valor "{}" em metros, vale:\nEm centímetros: {} \nEm milímetros: {}'.format (me, c, mi))
