import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
    
def main():
    folder_paths = input("Enter a list of folder separted by spaces: ").split()

    for folder_path in folder_paths:
        files, error_messages = list_files_in_folder(folder_path)
        if(files):
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"error in {folder_path}: {error_messages}")

if __name__=='main':
    main()                        
