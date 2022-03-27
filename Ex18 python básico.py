'''
Ex18
faça um programa que sorteie uma ordem de apresentação de trabalho dos alunos.
'''
import random

print ('===== EXERCÍCIO 18 =====')
aluno1 = str(input('Digite o nome dos alunos:\n >'))
aluno2 = str(input(' >'))
aluno3 = str(input(' >'))
aluno4 = str(input(' >'))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print ('O lista sorteada foi: \n{}'.format(lista))
