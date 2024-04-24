from pathlib import Path

root_dir = Path('files')
file_path = root_dir.iterdir()

for path in file_path:
    print(path)