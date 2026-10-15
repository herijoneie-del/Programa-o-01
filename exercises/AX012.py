'''
Escrever uma aplicação que recebe 2 numeros de utilzador 
E devolve a soma
'''
import sys
sys.stdout.reconfigure(encoding='utf-8')

print('Ola, escreva dois numeros;')

numero_1 = int(input('número 1;'))
numero_2 = int(input('número 2;'))
resultado = numero_1 + numero_2

print ('a soma dos dois números recebidos é', resultado)
