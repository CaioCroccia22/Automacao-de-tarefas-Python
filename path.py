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
if p1.exists():
    # Se existir, abre o arquivo para leitura
    with open(p1, 'r', encoding='utf-8') as file:
        # Lê e imprime o conteúdo do arquivo
        print(file.read())
        
        