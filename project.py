from pathlib import Path
import os

try:
    def readfileandfolder():
        p = Path('')
        items = list(p.rglob('*'))
        for index , file in enumerate(items):
            print(f"{index+1} - {file}")
except Exception as e:
    print(e)


def create_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file: ")
        p = Path(file_name)
        if p.exists():
            print("FILE ALREADY EXISTS!!")
        else:
            with open(file_name,'w') as file:
                content = input('Enter your file content: ') 
                file.write(content)
                print('File added!')
    except Exception as e:
        print(e)


def read_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file: ")
        p = Path(file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print("FILE NOT FOUND!")
    except Exception as e:
        print(e)


def update_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file")
        p = Path(file_name)
        if p.exists:
            print("Press 1 to overwrite content")
            print("Press 2 to append the content")
        
            option = int(input("Enter your choice: "))
            if option == 1:
                with open(file_name,'w') as file:
                    content = input("Enter your content: ")
                    file.write(content)
                    print("Content Changed!!")
            elif option == 2:
                with open(file_name,'a') as file:
                    content = input("Enter your content: ")
                    file.write(content)
                    print("Content Changed!!")
            else:
                print("Invalid input")
        else:
            print("File does not exist!")
    except Exception as e:
        print(e)


def delete_file():
    readfileandfolder()
    file_name = ("Enter name of your file: ")
    p = Path(file_name)
    if p.exists():
        os.remove(p)
        print("FILE DELETED!")
    else:
        print("File does not exist")
def rename_file():
    readfileandfolder()
    file_name = ("Enter name of your file: ")
    p = Path(file_name)
    if p.exists():
        new_name = input("Enter new name of the file: ")
        p.rename(new_name)
        print("File name changed")

def create_folder():
    readfileandfolder()
    folder_name = input("Enter name of your folder: ")
    p = Path(folder_name)
    if p.exists():
        print("Folder already exists!")
    else:
        os.mkdir(folder_name)
        print("Folder Created!")

def delete_folder():
    readfileandfolder
    folder_name = input("Enter folder name: ")
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print("File Deleted!")
    else:
        print("Folder does not exist")

def file_in_folder():
    readfileandfolder()
    folder_name = input("Enter name of your folder: ")
    file_name = input("Enter name of your file: ")
    p = Path(folder_name) / file_name
    if p.exists():
        print("FILE ALREADY EXISTS!!")
    else:
        with open(p,'w') as file:
            content = input('Enter your file content: ') 
            file.write(content)
            print('File added!')

while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 5 for renaming file")
    print("Press 6 for creating a folder")
    print("Press 7 for deleting a folder")
    print("Press 8 to create file in folder")
    print("Press 0 for exiting")
    
    option = int(input("Enter your choice: "))
    if option == 1:
        create_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file()
    if option == 5:
        rename_file()
    if option == 6:
        create_folder()
    if option == 7:
        delete_folder()
    if option == 8:
        file_in_folder()
    if option == 0:
        break
