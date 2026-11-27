
def lista_dicio (dct: dict) -> None:       
    """Função para apresentar um dicionário em ecrã"""
    for item in dct.keys():
            print(f'{item}: {dct[item]}')  