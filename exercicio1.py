from pathlib import Path

root_dir = Path('exer_folder')
filepath = root_dir.iterdir()
for path in filepath:
    if path.is_file():
        print(path)
        
        file_extension = path.suffix.lower()
        print(file_extension)
        
    