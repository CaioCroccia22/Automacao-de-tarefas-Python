from pathlib import Path

root_dir = Path('files')
# file_path = root_dir.iterdir()

# for path in file_path:
#     # Vai exibir somente as pastas
#     print(path)
#     # Vai exibir os arquivos dentro da pasta
#     for filepath in path.iterdir():
#         print(filepath)
        
#  Para evitar todas essas linhas de codigo temos uma função:


file_paths = root_dir.glob('**/*')
for path in file_paths:
    print(path)