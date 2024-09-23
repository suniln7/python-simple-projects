import os


def list_files_and_errors(folder_path):
    
    """
    this function will take the folder path as input and list it in try block if is present it will return list of files and a none
    FileNotFoundError and PermissionError are handled in except block that return none , error string

    """
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None,"dir not present"
    except PermissionError:
        
        return None, "user does have permission to list the folder:" 
    



folders_list = input("Enter folders with space: ").split()

for folder in folders_list:
    """
    this for loop will loop through the list of folders inputed by user and is passed to function that will rerturn files,errors
    if files are returned they will be looped and print to console 
    else the error will print that is returned from function 
    
    """
    files, errors = list_files_and_errors(folder)

    if files:
        print("=============listing dir: " + folder)

        for file in files:
            print(file)
    else:
        print(f"Error in {folder}: {errors}")


