import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import platform

root = tk.Tk()
root.withdraw()

listOfAll = []
NameOfCategories = ["Buisiness", "Programming"]
DictionaryOfKeywords = {
    "Buisiness" : ["Business", "Startup", "Start up", "Economics", "Money", "Sales"],
    "Programming": ["Programming", "Python" ,"JavaScript"]
}
categorized_files = {category :[] for category in NameOfCategories}


FolderPath = filedialog.askdirectory()

def CategoriseFiles():
    """ 
    This function is responsible to ssepaate the files given to it into separate lists based onthe keywords given in the DictionaryOfKeywords dictionary and the category in the  name of categories
    
    """
    if FolderPath:
        FilesInDirectory = os.listdir(FolderPath)
        for FileName in FilesInDirectory:
            if ".pdf" in FileName :
                listOfAll.append(FileName)
                for category in NameOfCategories:
                    for keyword in DictionaryOfKeywords[category]:
                        if keyword in FileName :
                            if FileName in categorized_files[category] : 
                                continue
                            else :
                                categorized_files[category].append(FileName)

def RunCode():
    """ 
    This function is used to get the user input and then exits if the user wants to exit else it continues for asking the user about the choices
    
    """
    for i in range(0,len(NameOfCategories)) :
        print("For " +NameOfCategories[i] +" Enter : " +str(i+1))
    print("Enter " +str(len(NameOfCategories) + 1) + " To Exit")
    UserChoice = input("Enter Your choice : ")
    return int(UserChoice)

def ShowBooks(k) :
    UserCategoryChoice = str(NameOfCategories[int(k)-1])
    print("contents of the category : " )  
    BooksList = categorized_files[UserCategoryChoice]
    i = 1
    for book in BooksList : 
        print(book + " = " + str(i))
        i +=1
    print()
    SelectBooks(UserCategoryChoice)

def SelectBooks(category):
    BooksList = categorized_files[category]
    UserInputSelectBook = int(input("Enter The number in front of the book you want to select it : "))
    if UserInputSelectBook in range(1,(len(BooksList) - 1)) :
        SelectedBook = BooksList[UserInputSelectBook]
        SelectedBookPath = FolderPath + "/" + SelectedBook
        open_file_with_default_program(SelectedBookPath)
        # UserOption = int(input("enter 1 to open the book and "))

def open_file_with_default_program(file_path):
    system = platform.system()
    if system == 'Windows':
        os.startfile(file_path)
    elif system == 'Darwin':  # Mac OS
        subprocess.call(['open', file_path])
    else:  # Linux and other Unix-like systems
        subprocess.call(['xdg-open', file_path])
   
    
if __name__ =="__main__" :                               
    CategoriseFiles()
    run_code = RunCode()
    while run_code != (len(NameOfCategories) + 1):
        ShowBooks(run_code)
        run_code = RunCode()