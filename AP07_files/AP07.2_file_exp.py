from pathlib import Path

# localização do ficheiro
path = Path('C:/WorkingArea/Developer/Python/ficheiros/teste.txt')
# Path converte a string para um objeto de sistema de ficheiros (caminho ou ficheiro)

# Ler o conteúdo do ficheiro
conteudo = path.read_text(encoding='utf-8')
print(conteudo) # mantém o conteúdo original do ficheiro, incluindo quebras de linha

# Obter/separar linhas
linhas = conteudo.splitlines()
i = 1
for linha in linhas:
    print(f'Linha {i}: {linha}')
    i += 1


path.write_text('Novo conteúdo do ficheiro\nSegunda linha do novo conteúdo', encoding='utf-8')    

conteudo = path.read_text(encoding='utf-8')
print(conteudo) # mantém o conteúdo original do ficheiro, incluindo quebras de linha
