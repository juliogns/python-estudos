'''
Ex13
faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
'''


print ('===== EXERCÍCIO 13 =====')
s = float(input('Digite o salário atual: '))
p = s + (s*0.15)
print ('R${} com 15% de aumento fica: R${}'.format(s, p))
