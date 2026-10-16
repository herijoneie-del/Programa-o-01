print('escreve o seu nome')
nome =input('nome')
print('o seu nome é:', nome)
# exer 03

print('escreve um numero a tua escolha')
numero =int(input())
print('o seu numero é:', numero)
 # Esta linha serve para input serve para obter o valor de utilizador e o = serve para guardar esse valor na variavel
# paranteses é o argumento
# str é string significa que vai coverter o objeto

import random
lmin,lmax = 1,1000
numbertoguess = random.randint(lmin,lmax)
guess = ""
print(f'valor inserido: {guess}, do tipo ({type(guess).__name__})')
print(f'{guess.isnumeric()} ;{guess.isdecimal()}')

while (guess != numbertoguess):
    guess = input(f'advinha o nemero entre {lmin} e {lmax}: -->')
    print(f'valor inserido: {guess}')
    if (guess.isnumeric().is_integer()):
        guess = int(guess)
        print(type(guess).__name__)
        if (guess > numbertoguess):
            print('mais baixo')
        elif (guess <numbertoguess):
            print('mais alto')
        else:
            print('acertou')
        attemp += 1    
    else:
        print(f'{guess} não é um numero inteiro')
print(f'acabou, o numero a adivinhar era {numbertoguess}')
if (guess == 'end'):
    print(f'desistiu ao fim de{attemp} tentativas')

else:
    print(f'acertou em {attemp} tentativas')