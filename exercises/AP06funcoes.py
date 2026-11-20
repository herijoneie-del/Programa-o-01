# Nota Prévia: Nos exemplos abaixo aparece várias vezes o erro 
#               "Function declaration "«nome_da_função»" is obscured by a declaração of the same name"
#              Estes erros são propositados para demonstração de variantes da mesma função com diferentes assinaturas
#              Cada nova definição de função com o mesmo nome irá sobrescrever a anterior
#
# O que é uma função?
#   Uma função é um bloco de código que realiza uma tarefa específica e pode ser reutilizado em diferentes partes do programa.
#   Ajuda a organizar o programa em tarefas mais pequenas.
#   Permite alterar uma tarefa num só local, mesmo que seja usada várias vezes.
#
#   'FUNÇÃO' é uma designação geral, também podem ser designadas por SUB-ROTINAS ou SUB-PROGRAMAS
#   A designação mais correcta é SUB-ROTINA, embora FUNÇÃO seja mais comum
#   Existem dois tipos de rotinas
#   1. As que não devolvem valores, designadas por procedimentos (ou rotinas procedimentais)
#   2. As que devolvem valores, que são as funções propriamente ditas (também designadas por rotinas funcionais)
#
#   Uma rotina é composta por duas partes:
#   1. Cabeçalho da rotina, também designado por ASSINATURA, onde se especifica o nome da rotin e os seus parâmetros
#   2. Corpo da rotina, onde se escreve o código que será executado sempre que a rotina for chamada
#      No caso de uma rotina funcional, o cabeçalho inclui também o tipo de valor que será devolvido 
#      e o corpo deve conter uma instrução, ou mais, para devolver o valor produzido
#
#   O uso de rotinas tem duas fases distintas:
#   1. A definição da rotina, onde se escreve o código da rotina com as duas partes referidas acima
#      Esta definição não executa a rotina, apenas a declara, ficando disponível para ser chamada posteriormente
#   2. A chamada, ou invocação, da rotina, onde se requer a sua execução
#      Por conceito (reutilização), esta chamada pode ocorrer várias vezes no programa
#
#   As funções podem ter PARAMETROS, ou seja, podem ser definidas com valores de entrada que influenciam o seu comportamento
#   Os parâmetros podem ter valores por defeito, que são usados caso não seja fornecido um valor na chamada da função
#
# Generalidades sobre funções em python
#   Python já inclui funções como print(), input() e len().
#   Também podemos criar as nossas próprias funções.
#   Definir uma função não a executa: o seu código só corre quando ela é chamada.

# definir funções com def
#   ATENÇÃO à indentação do código dentro da função
def saudacao():
    """função que imprime uma saudação"""
    print('Olá! Seja bem vindo!')

# A linha de comentário logo após a definição da função - """...""" - é a docstring
# a docstring é um comentário de explicação da função e que é automáticamente reconhecido pelo python
# pode ser chamdado através do atríbuto __doc__ da função ou indexado por ferramentas de documentação automática
# NOTA: não confundir a docstring com um comentário normal (# ou """..."""); 
#       A docstring é uma caracteristica especial de uma função, acessível em tempo de execução 
#       através do atributo __doc__ da função
print(saudacao.__doc__)  # imprime a docstring da função

# chamar a função ou INVOCAR a função
saudacao()

# funções com parâmetros
def saudacao_nome(nome):
    """função que imprime uma saudação personalizada com o nome"""
    print(f'Olá {nome}! Seja bem vindo!')       

# chamar a função com o parâmetro
saudacao_nome("Zé Manel")

# os parâmetros podem ter valores por defeito
def saudacao_nome(nome="Zé Manel"):
    """função com valor predefinido"""
    print(f'Olá {nome}!Seja bem vindo!')

# chamar a função com o parâmetro
saudacao_nome("Maria")    
# chamar a função sem o parâmetro usa o valor por defeito
saudacao_nome()     

# em caso de múltiplos parâmetros, a passagem pode ser posicional ou por nome
def saudacao(nome,titulo):
    """função com múltiplos parâmetros"""
    print(f'Olá {titulo} {nome}! Seja bem vindo!')  

# chamada posicional
saudacao("Zé Manel","Sr.")  

# chamada por nome (a ordem é indiferente porque a ligação é feita pelo nome do parâmetro)
saudacao(titulo="Sra.",nome="Maria")

# chamada mista - os parâmetros posicionais devem ser os primeiros
saudacao("Maria",titulo="Sra.")

# Há um erro de concordância entre o titulo e o genéro do 'vindo'...
# Quem quiser pode aplicar uma condicional para corrigir!

# caso se utilizem valores por defeito em funções de múltiplos parâmetros, os valores por defeito devem ser os últimos
def saudacao(nome,titulo="Sr."):
    """função com múltiplos parâmetros e valor por defeito"""
    print(f'Olá {titulo} {nome}! Seja bem vindo!')

# chamada com o valor por defeito
saudacao("Zé Manel")

# Funções que devolvem valores: return
# 
def cubo(numero):
    """função que devolve o cubo de um número"""
    return numero ** 3
# chamar a função e guardar o valor devolvido
res = cubo(3)
print(f'O cubo de 3 é {res}')
# chamar a função diretamente numa expressão
numero = 3
print(f'O cubo de {numero} é {cubo(numero)}')

# passar parametros por valor e por referência
# 1. por valor, mas sem alterar a variável dentro da função

marcas = ['Honda','fiat','ford','smart']

print('--- passar parametros por valor e por referência ---')
def show(marcas):
    marcas_in = []
    for marca in marcas:
        print(marca.title())
        marcas_in.append(marca)
    
    marcas_in.append('dacia')
    return(marcas_in)

# show(marcas)     
marcas_out = show(marcas)   
print(marcas,marcas_out)
print(marcas_out)

# 2. por valor, alterando a variável dentro da função

marcas = ['Honda','fiat','ford','smart']

print('--- passar parametros por valor e por referência ---')
def show(marcas):
    marcas_in = []
    for marca in marcas:
        print(marca.title())
        marcas_in.append(marca)
    
    marcas.append('dacia')
    return(marcas_in)

# show(marcas)     
marcas_out = show(marcas)   
print(marcas,marcas_out)
print(marcas_out)

# 3. por referência, alterando a variável dentro da função

marcas = ['Honda','fiat','ford','smart']

def show(marcas):
    for marca in marcas:
        print(marca.title())
    
    marcas.append('dacia')
    return(marcas)

show(marcas[:])     # passando uma cópia  - [:] - da lista original
                    # assim, a lista original não é alterada
marcas_out = show(marcas[:])   
print(marcas,marcas_out)
print(marcas_out)

# Passar um número variável de argumentos para uma função
print('--- passar um número variável de argumentos para uma função ---')
def var_args(*args):
    """*args define um tupulo de dimensão variável"""
    print(args)

    if args:
        for arg in args:
            print(arg)

global_args = ["a","b"]

var_args()    
var_args(1)
var_args("1")
var_args(1,2,3,4)
var_args(1,"1")
var_args(1,global_args)

# âmbito (ou contexto) de variáveis
def ambito_var(*args):
    """função que demonstra o âmbito (contexto) de variáveis"""
    local_args = "variável local"

    print(f"IN - local_args: {local_args}")     # lista variável local
    print(f"IN - args: {args}")                 # tupulo variável passada como parametro
    print(f"IN - global_args: {global_args}")   # lista variável global

    return local_args

resposta = ambito_var("argumento")
print(f"OUT - global_args: {global_args}")  # lista variável global
# print(f"OUT - local_args: {local_args}")    # erro - variável local não existe fora da função
print(f"OUT - resposta: {resposta}")

# mais sobre âmbito: alteração de variáveis globais dentro de funções
#include <stdio.h>
