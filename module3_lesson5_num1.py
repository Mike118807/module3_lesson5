# Task 1: Directory Inspector:
# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user 
# for the directory path and then display the contents.
# Code Example:
    
# import os

# def list_directory_contents(path):

# List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for 
# invalid paths or inaccessible directories.

import os

def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f'Directory: {entry.name}')
                else:
                    print(f'File: {entry.name}')
    
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("Permission denied. Cannot access this directory.")
    except Exception as e:
        print(f"An error occored: {e} ")
if __name__ == "__main__":
    
    # prompt user for directory path.
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)