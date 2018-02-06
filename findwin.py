# Author: Khang Vinh Tran
# Local System File Search Engine
# Assignment 4
# CIS 41B

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import platform

from filesearch import *

class FindWin(tk.Tk):
    '''
    Main window of the program, derived from Tk class,has 3 methods:
    - Constructor
    - selectDir
    - search
    '''
    
    def __init__(self):
        super().__init__()
        
        # add title
        self.title("Local System Search")
        
        # set resizable
        self.resizable(True, True)
        
        
        # add Label that shows current start directory. The default is Home directory of the system
        self.startDir = tk.StringVar()                                   # must use tk.StringVar()
        # self.startDir.set(os.path.expanduser("~"))                       # must set() to assign string. Do not use "="
       
        #########################################
        self.startDir.set(os.path.expanduser("/Users/KVTran/Documents/CIS41B/Module4_System/System_Search_Engine")) 
        #######################################
       
       
        self.currentFolderStringVar = tk.StringVar()
        self.currentFolderStringVar.set("  Current Folder:   " + str(self.startDir.get()))
        currentStartDirLabel = tk.Label(self, textvariable = self.currentFolderStringVar)
        currentStartDirLabel.grid(row = 0, column = 0, sticky = 'w')
        
        
        #add Button: "Change Folder". Call back selectDir() 
        changeFolderButton = tk.Button(self, text = "Change Folder", command = self.selectDir)
        changeFolderButton.grid(row = 1, column = 0, sticky = "w")
        
        
        # add Label: "Regex Filter"
        regexFilterLabel = tk.Label(self, text = "Regex Filter: ")
        regexFilterLabel.grid(row = 2, column = 0, sticky = 'ew')
        
        self.regexFilter = tk.StringVar()
        regexFilterEntry = tk.Entry(self, textvariable = self.regexFilter)
        regexFilterEntry.grid(row = 2, column = 1,  sticky = 'ew')
        
        regexFilterEntry.focus_set()                                 # set the current cursor to the regexFilterEntry
        regexFilterEntry.bind("<Return>", self.search)               # bind regexFilterEntry with Return Key, with self.search function
                                                                     # Strong notice: this binding will pass regexFilter into self.search(). 
                                                                     
        # add Label: "result"
        resultLabel = tk.Label(self, text = "Result:")
        resultLabel.grid(row = 3, column = 0, sticky = 'w')
        
        
        # add listbox and scrollbar
        scrollBar = tk.Scrollbar(self)
        
        self.listBox = tk.Listbox(self, yscrollcommand = scrollBar.set)
        self.listBox.grid(row = 4, column = 0,sticky = 'nsew', columnspan = 2)
        self.rowconfigure(4, weight = 1)  
        self.columnconfigure(1, weight = 1)  
    
        scrollBar.config(command = self.listBox.yview)        
        scrollBar.grid(row = 4, column = 2, sticky = "wns")
        
        
        # add empty buffer
        tk.Label(self).grid(row = 5, column = 0, sticky = 'w')
        
        # update window on screen
        self.update()
        
        # instantiate the fileSearch object with the string of self.startDir()
        self.fileSearchObject = FileSearch(self.startDir.get())
        
        
    def selectDir(self):
        '''
        This function use tk.filedialog.askdirectory(initialdir) to set new starDir 
        '''
        # clear the previous search result        
        self.listBox.delete(0, tk.END)
        
        # set a new startDir
        newDir = tk.filedialog.askdirectory(initialdir = self.startDir)    # notice: newDir can be an empty string if user cancel the search
        if newDir != "":                                                   # only update the new directory if the user confirm the search
            self.startDir.set(newDir)
        self.currentFolderStringVar.set("  Current Folder:   " + str(self.startDir.get()))
        
        # create a new fileSearch object with new path
        self.fileSearchObject = FileSearch(self.startDir.get())
        
        # call the private search function
        self.search(self.regexFilter)
        
       
       
        
    def search(self, regex):
        # clear the previous search result
        self.listBox.delete(0, tk.END) 
        
        try:
            regex = re.compile(self.regexFilter.get(), re.I)
            self.fileSearchObject.searchName(regex)
            searchResultSize = len(self.fileSearchObject.searchResult)
            if (searchResultSize > 1000):
                tk.messagebox.showwarning("High Number of results", "Found more than 1000 results. Ommited")
            else:
                [self.listBox.insert(tk.END, result) for result in self.fileSearchObject.searchResult]
        
        except Exception as e:
            tk.messagebox.showerror("Regex Error", e)

        
        


#############################################################
######################### Test Area ######################### 
#############################################################

def main():
    app = FindWin()
    
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid())) 
        
    app.mainloop()

main()

