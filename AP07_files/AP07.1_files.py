from pathlib import Path

# localização do ficheiro
path = Path('/workspaces/Programa-o-01/ficheiros/teste.txt')
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
# Escrever novo conteúdo no ficheiro (o conteúdo existente é apagado)
path.write_text('Novo conteúdo do ficheiro\nSegunda linha do novo conteúdo', encoding='utf-8')
# A função write_text escreve apenas uma string no ficheiro
# Havendo necessidade de escrever múltiplas linhas, deve-se usar o caractere de nova linha \n

# Acrescentar conteúdo ao ficheiro (o conteúdo existente é mantido)
# A classe path não tem método para acrescentar, deve utilizar-se a função open em modo append 'a' (v. no próximo exemplo)
# No formato simplificado - path.write_text - o acrescento faz-se em dois passos:
# 1. ler o conteúdo existente
# 2. escrever o conteúdo existente + novo conteúdo
# Exemplo:
conteudo_existente = path.read_text(encoding='utf-8')   
conteudo_novo = conteudo_existente + '\nConteúdo acrescentado ao ficheiro'
path.write_text(conteudo_novo, encoding='utf-8')    
# verificar o conteúdo atualizado do ficheiro
print(path.read_text(encoding='utf-8'))

# Se o ficheiro não existir, os métodos write_text cria o ficheiro automaticamente
# assomindo que o diretório onde o ficheiro vai ser criado já existe e que o utilizador tem permissões de escrita nesse diretório
path = Path('/workspaces/Programa-o-01/ficheiros/teste.txt')
path.write_text(conteudo_novo, encoding='utf-8')    
print(path.read_text(encoding='utf-8'))
