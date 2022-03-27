'''
Ex17
um professor quer sortear um dos seus quatro aluno para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random

print ('===== EXERCÍCIO 17 =====')
aluno1 = str(input('Digite o nome dos alunos:\n >'))
aluno2 = str(input(' >'))
aluno3 = str(input(' >'))
aluno4 = str(input(' >'))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print ('O aluno sorteado foi: {}'.format(sorteado))
