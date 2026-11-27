from pathlib import Path

def listar_arquivos(diretorio: str) -> list:
    """Função que lista todos os arquivos em um diretório."""
    p = Path(diretorio)
    arquivos = [str(arquivo) for arquivo in p.iterdir() if arquivo.is_file()]
    return arquivos 

def ler_arquivo(caminho_arquivo: str) -> str:
    """Função que lê o conteúdo de um arquivo e retorna como string."""
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    return conteudo 

def escrever_arquivo(caminho_arquivo: str, conteudo: str) -> None:
    """Função cria ficheiro novo com o conteúdo fornecido. 
       Se o ficheiro já existir, não substitui."""
    myFile = Path(caminho_arquivo)
    if myFile.exists():
        print(f'O ficheiro {caminho_arquivo} já existe. O conteúdo NÃO será substituído.')
        raise FileExistsError(f'O ficheiro {caminho_arquivo} já existe.') # também se pode utilizar raise Exception()
    else:
        print(f'va ser criado o ficheiro {caminho_arquivo}')
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)

def acrescenta_arquivo(caminho_arquivo: str, conteudo: str) -> None:
    """Função que adiciona conteúdo a um ficheiro. O ficheiro é criado se não existir."""
    with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

path = 'C:/WorkingArea/Developer/Python/ficheiros'
for arquivo in listar_arquivos(path):
    print(arquivo)

file = f'{path}/teste.txt'   
try:
    escrever_arquivo(file, 'Olá, mundo!\nEsta é uma linha de teste.')
except FileExistsError as e:
    print(e)

acrescenta_arquivo(file, '\nEsta linha foi acrescentada ao ficheiro.')    
    
conteudo = ler_arquivo(file)    
print(conteudo)
