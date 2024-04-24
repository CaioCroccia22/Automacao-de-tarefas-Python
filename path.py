from pathlib import Path

p1 = Path('dados', 'texto.txt')
print(p1)

# Verificar o tipo do arquivo

print(type(p1))

#  Verificando o nome

print(p1.name)

# Pega apenas o nome do arquivo

print(p1.stem)

#  Pega apenas o tipo do arquivo

print(p1.suffix)

# Verifica se o arquivo existe

print(p1.exists)