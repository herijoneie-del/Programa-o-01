# importar modulos personalizados
# De uma forma simplificada, módulos são ficheiros 'normais' de código que podem ser importados por outros ficheiros
# Os objectivos dos módulos são organizar o código, facilitar a reutilização e melhorar a manutenção.
# Estes módulos podem conter funções, classes e variáveis que mantêm caracteristicas em todas as utilizações
# Qualquer ficheiro Python pode ser considerado um módulo, desde que possa ser importado por outros ficheiros.
# Todo os conteúdo de um módulo estará disponível para os ficheiros que o importarem, desde variáveeis a aplicações

# Existem dois tipos base de módulos:
# - internos, que fazem parte da biblioteca padrão do Python, 
# - externos, que são criados pelo utilizador ou obtidos de terceiros.
# a utilização tem diferenças, principalmente na forma como são instalados e importados.
# Módulos internos podem ser importados diretamente, enquanto módulos externos podem necessitar de instalação prévia.
# Já vimos exemplos de módulos internos em lições anteriores: 'import math' ou 'from math import randint'

# Os módulos esternos podem ser obtidos de terceiros e geralmente necessitam de instalação antes de serem importados.
# A instalação é normalmente feita através de ferramentas como 'pip', que é o gestor de pacotes do Python.
# No presente contexto, um 'pacote' é um conjunto de 'módulos' organizados numa estrutura de diretórios.
# A instalação de um pacote, naturalmente, inclui os vários módulos que o compõem.
# Por norma, a instalação de pacotes externos é feita através do comando 'pip install nome_do_pacote'.

# Um módulo externo também pode ser desenvolvido pelo próprio utilizador, ficando disponível juntamente com o código aplicacional
# A utilização é semelhante aos módulos isntalados, mas há mais personalização e racionalização de código
# Para utilizar modulos personalizados é necessário indicar o caminho correto para o ficheiro ou pacote que contém o módulo.
# Além disso, é necessário importar o módulo 'modules' do pacote 'sys' para manipular o caminho de pesquisa de módulos.

## Utilização
# independentemente do tipo de módulo, é necessário importá-lo antes de utilizar as suas funcionalidades.
# Existem várias formas de importar módulos:
# - import modulo               : importa o módulo completo
# - from modulo import funcao   : importa apenas a função especificada do módulo
# - from modulo import *        : importa todas as funções e variáveis do módulo (não recomendado)
# É importante escolher a forma de importação adequada ao contexto para evitar conflitos de nomes e sobreposição de funcionalidades.
#
# Para facilitar o seu uso dentro do código, os módulos podem ser importados com alias, utilizando a palavra-chave 'as'
# Exemplo:
# - import modulo as m
# - from modulo import funcao as f
#
# Para executar uma funcionalidade ou recurso importado é necessário ter em conta a forma de importação:
# - Importação de Módulo completo: import modulo -> usar o prefixo do módulo: modulo.funcao()
# - Módulo importado com alias: import modulo as m -> usar o alias em vez do nome: m.funcao()
# - Importação de Função especifica: from modulo import funcao -> usar a função diretamente: funcao()
# - Função importada com alias: from modulo import funcao as f -> usar o alias em vez do nome: f()

from sys import modules # indispensável para módulos carregados dinamicamente
import AP06_modules.AP06_3_modules as m   # importa todos os módulos existentes na pasta AP06_modules

# exemplos do ficheiro AP04.2_dic.py
dicionario_vazio = {}
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'Lisboa'}

#AP06_modules.lista_dicio(dicionario_vazio)
#AP06_modules.lista_dicio(pessoa)

# o mesmo resultado pode ser obtido utilizando a importação direta da função
from AP06_modules.AP06_3_modules import lista_dicio
m.lista_dicio(dicionario_vazio)
m.lista_dicio(pessoa)

# com alias
# from AP06_modules.AP06_3_modules import lista_dicio as ld
# ld(dicionario_vazio)
# ld(pessoa)


