import os
import hashlib


def menu():
    condition = True
    
    while condition != False:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = int(input("Choose an option: "))
       
        if choice == 1:
            directory = input("Please input the directory name: ")
            return directory

        elif choice == 2:
            
            break

        else: 
            print("Not one of the available options.")
   

def find_duplicates(directory):
    found_files = {}
    found_duplicates = []

    # for filename in os.walk(directory):
    #     # use a dictionary to store file names and paths
                
    #     checksum = get_checksum(filename)
    #     found_files[checksum]=filename
    

    # # compare files with the same name
    # if checksum in found_files: 
    #     found_duplicates.append(filename, checksum)

    # return found_duplicates

    #taken from ChatGPT
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            checksum = get_checksum(file_path)
            
            if checksum:
                # If checksum already exists, it's a duplicate
                if checksum in found_files:
                    found_duplicates.append((file_path, found_files[checksum]))
                else:
                    found_files[checksum] = file_path

    return found_duplicates

def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()