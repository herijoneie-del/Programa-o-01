import sys 
sys.stdout.reconfigure(encoding="utf-8")
# comentario: este codigo vai fazer a interpretação para iunicode do computador
"""
comentario de varias linhas 
"""

nome = 'Herijoni José Ié'
print("olá " + nome)

print(f"olá {nome}, \nbem-vindo")

# receber dados de utilizador
novonome = input(f"Olá {nome}, escreve o nome de uma disciplina:")

print(f"olá {nome}, \nbem-vindo a {novonome}!")

print("nome é do tipo: " + type(nome).__name__)