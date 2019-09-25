#Importing Necessary Packages
import os
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import filedialog

#Setting plotting style
sns.set_style("darkgrid")

#Creating a window in tkinter making it of fixed width and non-resizeable
window = tk.Tk()
window.geometry("600x400")
window.resizable(0,0)
window.title("Graph Generator")


#Declaring Tkinter Variables
entryfile=tk.StringVar()
folderpath=tk.StringVar()

#Select File Name Function
def selectfilename():
    global filename
    filename=tk.filedialog.askopenfilename(initialdir=os.getcwd())
    entryfile.set(filename)

#Location to save Function
def selectfolder():
    global foldername
    foldername=tk.filedialog.askdirectory(initialdir=os.getcwd())
    folderpath.set(foldername)

#Submit Button Function Command
def submit():
    data=filename.split('/')[-1]
    directory=filename[:filename.rfind('/')]
    graph(data,save=directory)
    done.config(text="Done..Graphs are saved at the specified directory")

#Main Graph Function
def graph(data, column=None, save=None):
    '''Function Graph Takes in all standard file types supported by pandas..
    ``data`` takes in the file name with extension
    ``column`` is used to specify the column labels for which the graph is to be 
    created
    ``save`` takes in the location of the folder where the created graph to be saved'''

    # Setting directory to current directory if No value is provided
    if save == None:
        save = os.getcwd()

    # Modify df based on user provided column name
    if column != None:
        df = df[column]

    # Get the file type and filename from data
    filename = data[:data.find('.')]
    filetype = data[data.find('.')+1:]

    # Make directory in the filename and change cwd to that folder to store all data in that
    # Handling Removing of empty directory in the name of filename
    if filename not in os.listdir(save):
        os.mkdir(save+'\\'+filename)
    else:
        os.removedirs(save+'\\'+filename)
        os.mkdir(save+'\\'+filename)

    # Combining file types to call relevant read function
    read = "pd.read_"+filetype

    # Evaluating the file based on the filename provided and storing it in the dataframe
    # Handling multiple file types
    try:
        if filetype=='xlxs':
            df = pd.read_excel(filetype)
        else:
            df = eval(read)(data)
    except AttributeError as ae:
        print(ae)

    # Separate Numerical and Categorical data
    categorical = df.select_dtypes(include="object")
    numerical = df.select_dtypes(exclude="object")

    # Changing directory to save all graph
    os.chdir(save+'\\'+filename)

    for i in list(numerical.columns):

        # Generating histogram for all numerical columns
        plt.hist(numerical[i])
        plt.title('Histogram of ' + i.upper())
        plt.xlabel(i.upper())
        plt.ylabel("Frequency")
        plt.savefig(i.upper()+'-Histogram.png')
        plt.clf()

        # Generating BoxPlot for all numerical columns
        plt.boxplot(numerical[i])
        plt.title('Box Plot of ' + i.upper())
        plt.ylabel(i.upper())
        plt.savefig(i.upper()+'-box.png')
        plt.clf()
        
    for c in list(categorical.columns):
        # Plotting Bar chart
        if len(categorical[c].unique()) <= 30:
            plt.bar(categorical[c].unique(), categorical[c].value_counts())
            plt.title('Bar Graph of ' + c.upper())
            plt.ylabel('Frequency')
            plt.savefig(c.upper()+'-bar.png')
            plt.clf()

    # Changing directory to parent
    os.chdir('..')

#TITLE FRAME
top_frame = tk.Frame(master=window, height=60, background="blue",bd=1,relief="raised")
top_frame.pack(fill='x',padx=5,pady=5)

#Top Label
top_label = tk.Label(master=top_frame,text="GRAPH GENERATOR",font=("Times",30),bg="blue",fg="white").pack()

#MIDDLE FRAME
mid_frame = tk.Frame(master=window,height = 320)
mid_frame.pack(fill="both",padx=5,pady=5)

#Mid Labels

#file and path of file
file = tk.Label(master=mid_frame,text="File: ",font=("Times",15)).place(x=135,y=50)

#Select File Button:
# select = tk.Button(master = mid_frame, text="Select", command=select)
select = filedialog.Button(master = mid_frame, text="Select", command=selectfilename)
select.place(x=520,y=50)

#Entry button
file_entry = tk.Entry(master=mid_frame,textvariable=entryfile,width=50).place(x=200,y=54)

#Location to save the graph
location=tk.Label(master=mid_frame,text="Location to save: ",font=("Times",15)).place(x=40,y=150)

#Select Location Button
select2 = filedialog.Button(master = mid_frame, text="Select", command=selectfolder).place(x=520,y=150)

#Folder to save in...
file_entry = tk.Entry(master=mid_frame,textvariable=folderpath,width=50).place(x=200,y=154)

#Submit Button
submit = tk.Button(master=mid_frame,text="Submit",command=submit).place(x=300,y=250)

#result
done = tk.Label(master=mid_frame,text="")
done.place(x=200,y=280)

tk.mainloop()