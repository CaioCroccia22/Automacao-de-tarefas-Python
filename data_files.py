from pathlib import Path
from datetime import datetime

path = Path('files', 'dados2', 'teste.txt')

print(path.stat())

# Retorna -> st_ctime=1713998874 -> metadado

stats = path.stat()
second_created = stats.st_ctime

# Selecionada a data e hora + ponto
date_created = datetime.fromtimestamp(second_created)
print(date_created)


# colocando a formatação apenas de data e hora
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(date_created_str)