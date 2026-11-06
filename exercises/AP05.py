import math
'''
teste = input('Escreve um valor para verificar se é número -->')

teste = teste.strip()
if teste == '':
    print('nenhum valor foi escrito.')
elif teste.isdigit():
    print('o valor é um número inteiro.')
elif teste[:1] in {"+", "-"} and teste[1:].isdigit():
    print('o valor é um número inteiro.')
else:
    print('o valor não é um número inteiro.')


# Exemplo de uso do bloco try-except para capturar erros durante a execução do código
# O python, como a maioria das linguagens de programação, permite capturar e tratar erros durante a execução do código usando o bloco try-except.
# O uso deste tipo de abordagem permite simplificar o código evitando a necessidade de múltiplas verificações condicionais para tratar erros 
# esperados e inesperados.
#
# A estrutura try-except é utilizada para capturar e tratar erros durante a execução do código.
# A sintaxe básica é:
# try:
#     # código que pode gerar erro
# except Exception as ex:
#     # código para tratar o erro
#
# O bloco try contém o código que pode gerar um erro, enquanto o bloco except contém o código que será executado caso ocorra um erro.
# Caso não ocorra qualquer erro dentro do bloco try, o bloco except é ignorado. A execução do código salta para a 1ª instrução após o bloco try-except.
# Qualquer erro ocorrido fora do bloco try não será capturado e resultará em uma exceção não tratada (unhandled exception), 
# com a consequente interrupção do programa (hard stop ou crash).
# O que pode acontecer se ocorrer um erro no bloco except?
#   O erro não será capturado pelo mesmo bloco e resultará em uma exceção não tratada, interrompendo a execução do programa.
#
# O 'except' identifica erros que podem ocorrer durante a execução do código e inicia um bloco de código e executar em caso de erro
# Pode ser escrito como:
#   except Exception:
# ou
#   except:
# ou
#   except «TipoDeErro»:
#   «TipoDeErro» pode ser obtido consultando a documentação do Python ou executando código que gera erros
# ou, para capturar vários tipos de erros:
#   except («TipoDeErro1», «TipoDeErro2»):
#   No exemplo acima:
#       ValueError: erro gerado quando a conversão de string para float falha
#       TypeError: erro gerado quando a função recebe um argumento de tipo errado

# exemplo com teste (TRY) em vez de IF  
print()
ttry = input('Exemplo TRY. Escreve um valor para verificar se é número -->')
try:
    ttry = float(ttry.strip())
    print(f'O valor "{ttry}" é um número.')
except Exception as ex:
    print(f'O valor "{ttry}" não é um número válido: {type(ex).__name__}: {ex}')
#       trata erros não previstos (unhandled exceptions)      
#       Exception é a classe base para os erros em Python, captura todos os tipos de erros
#       A instrução 'except Exception as ex' deve ser colocada após todas as outras instruções 'except', 
#       de modo a não impedir a captura dos erros específicos    
#       
#      type(ex).__name__} --> indica o tipo de erro detectado
#      {ex} --> indica a mensagem de erro associada ao erro detectado
'''
# exemplo com erros conhecidos
print()
tknownerr = input('Exemplo TRY. Escreve um valor para verificar se é número -->')
try:
    x = float(tknownerr.strip())
    print(f'O valor "{tknownerr}" é um número.')
except (ValueError, TypeError):
    print(f'"{tknownerr}" não é um literal float válido.')      
#       trata erros conhecidos, no caso, de conversão falhada de string para float
#       Podem ser utilizadas tantas instruções except quantas forem necessárias para particularizar o tratamento de erros
except Exception as ex:
    print(f'O valor "{tknownerr}" não é um número válido: {type(ex).__name__}: {ex}')
#       A instrução 'except Exception as ex' deve sempre existir após todas as outras instruções 'except', 
#       de modo a garantir a captura dos erros específicos
#       Se o erro ocorrido não constar da lista de erros conhecidos, ele será capturado pelo bloco 'except Exception as ex'.
#       Neste caso, a omissão deste bloco irá resultar em erros não tratados e consequente interrupção da execução do programa
