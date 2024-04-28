from pathlib import Path


list_file = []

root_dir = Path('exer_folder')
filepath = root_dir.iterdir()
for path in filepath:
    if path.is_file():
        # print(path)
        
        file_extension = path.suffix.lower()
        # print(file_extension)
        
        if file_extension == ".zip":
            list_file.append(path)
            
            
        if file_extension == ".csv":
            list_file.append(path)
            
            
        if file_extension == ".Ink":
            list_file.append(path)
          
            
        if file_extension == ".png":
            list_file.append(path)
           
print(list_file)
    