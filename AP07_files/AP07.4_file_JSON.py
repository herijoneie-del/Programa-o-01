import json
import JSONFiles
from pathlib import Path

# O JSON é um formato padrão de intercâmbio de dados, baseado em texto, leve e fácil de ler e escrever
# Muito utilizado em aplicações web para troca de dados entre cliente e servidor    
# Permite armazenar estruturas de dados complexas (listas, dicionários, etc.) de forma hierárquica, 
# o que o torna particularmente adequado para persistência de dados de Python pela semelhança entre os tipos de dados
# Em Python, o módulo json permite converter entre objetos Python e strings JSON

# escrever uma estrutura de dados de Python em ficheiro JSON
def make_menu () -> dict:
    """Função para iniciar o menu
       A utilização de uma função garante a reusabilidade do código
       facilitando a leitura em base de dados ou ficheiro"""    
    menu = {}
    menu[1]='opção 1'    
    menu[2]='opção 2'
    menu[3]='opção 3'
    return menu

def lista_dicio (dct: dict) -> None:       
    """Função para apresentar um dicionário em ecrã"""
    for item in dct.keys():
            print(f'{item}: {dct[item]}')  

myMenu = make_menu()
myList = ['item1', 'item2', 'item3']
myMenu['extra']= myList

path = 'C:/WorkingArea/Developer/Python/ficheiros/menu.json'

with open(path, "w", encoding="utf-8") as write_file:
    json.dump(myMenu, write_file, indent=4)

# ler uma estrutura de dados de Python a partir de ficheiro JSON
with open(path, "r", encoding="utf-8") as read_file:
    newMenu = json.load(read_file)    

print(f'{type(newMenu)}')
lista_dicio(newMenu)

for indice,valor in newMenu.items():
    print(f'Índice {indice} é do tipo {type(valor).__name__}')
    if type(valor).__name__ == 'list':
        print(f'Índice {indice} contém uma lista:')
        for item in valor:
            print(f' - {item}')
    else:
        print(f'Índice {indice} contém o valor: {valor}')