#escreve um programa que aceita entradas do utilizador 
#adicionando-as a uma lista ate o utilizador escrever 'end'
#quando o utilizador escrever 'end', o progragama apresenta a 
#lista em ecra, sem o 'end'
entrada= ""
lista = []
while(entrada !="end"):
    entrada = input('escreva alguma coisa (ou "end" para terminar):')
    lista.append(entrada)
    
lista.remove('end')
print('lista')
for lista in lista:
    print(lista)
