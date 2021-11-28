#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- Extension wise file categories #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from tkinter import *
from tkinter import filedialog
import os
import shutil

def select_file():    # function for taking folder's path, moving files in separate folder, Print list of all file name before run and after run.

    path_= filedialog.askdirectory()    # using askdirectory function for catching directory path.
    list_= os.listdir(path_)    # using listdir function for creating list of files names.

    Label(f1, text=path_,  bg="black",fg="light blue").pack()   # adding label in horizontal frame, work of label is print path.
    Label(f2, text="List all files names before run", font=('Aerial 15'), bg="black", fg="dodger blue").pack(pady=10)    # adding label in Left vartical frame, work of label is print: "List all files names before run".
    n=1
    for i in list_:    # work of for loop is printing all list elements.
        Label(f2, text=f"({n}) {i}", bg="black",fg="light blue").pack(anchor = "w",padx=40)
        n+=1 
    Label(f2, text=f"Total {n-1} file before run",font=('Aerial 11'), bg="black",fg="light blue").pack(anchor = "s",padx=40)

    # logic of moving files.
    for file_ in list_:
        name,ext = os.path.splitext(file_)    # using splitext function we can split Extension text.
        ext = ext[1:]    # staring from index 1 because 0th index considering '.' that's why we starting from 1.

        if ext == '':    # checking extension name is empty or not, if extension name is empty then skip the next code in for loop and goto next iteration.
	        continue	
        if os.path.exists(path_+'/'+ext):    # checking extension name of folder is already exist or not, if already exist then moving files otherwise goto for else.
            shutil.move(path_+'/'+file_, path_+'/'+ext+'/'+file_)    # using shutil.move we are moving files in separate folder.
        else:
            os.makedirs(path_+'/'+ext)    # creating folder of particular extension name.
            shutil.move(path_+'/'+file_, path_+'/'+ext+'/'+file_)    # using shutil.move we are moving files in separate folder.

    
    list_after_run=os.listdir(path_)    # creating new list for storing sorted folder name.
    Label(f3,text="List all folder name after run", font=('Aerial 15'), bg="black", fg="dodger blue").pack(pady=10)    # adding label in right vartical frame, work of label is print: "List all files names after run".
    
    n=1
    for i in list_after_run:    # work of for loop is printing all list elements.
        Label(f3,text=f"({n}) {i}", bg="black",fg="light blue").pack(anchor = "w",padx=40)
        n+=1
    Label(f3, text=f"Total {n-1} folder after run",font=('Aerial 11'), bg="black",fg="light blue").pack(anchor = "s",padx=40)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#   GUI   #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


# staring from here
root= Tk()  # starting GUI.
root.geometry("720x720")    # GUI window size.
root.title("File Management")   # window's title bar name.
root.minsize(720,720)   # minimum GUI window.

f1 = Frame(root, bg="black", borderwidth=6, relief=GROOVE)    # creating horizontal frame.
f1.pack(side=TOP, fill="x")    # packing horizontal frame.

f2 = Frame(root, bg="black", borderwidth=6, relief=GROOVE)    # creating Left vartical frame.
f2.pack(side=LEFT, fill="both",expand=True)    # packing Left vartical frame.

f3 = Frame(root, bg="black", borderwidth=6, relief=GROOVE)    # creating Right vartical frame.
f3.pack(side=RIGHT, fill="both",expand=True)    # packing right vartical frame.

Label(f1, text="Click on the button to select folder for extension wise file categories", font=('Aerial 15'), bg="black", fg="dodger blue").pack(pady=10)    # creating a label in top frame.
b1=Button(f1, text="Select folder & run", command= select_file,bg='sky blue').pack(padx=5, pady=5,ipadx=5)    # creating a button for select file and put in top frame, "command= select_file" is calling function.
root.mainloop()    #ending GUI