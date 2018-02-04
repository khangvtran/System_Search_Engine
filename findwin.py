# Author: Khang Vinh Tran
# Local System File Search Engine
# Assignment 4
# CIS 41B

import tkinter as tk
import os
import os.path
import platform

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
        
        # add label: "Current Folder: "
        currentFolderLabel = tk.Label(self, text = "  Current Folder: ")
        currentFolderLabel.grid(row = 0, column = 0, sticky = "w")
        
        # add Label that shows current start directory. The default is Home directory of the system
        startDir = tk.StringVar()
        startDir.set(os.path.expanduser("~"))        
        currentStartDirLabel = tk.Label(self, textvariable= startDir)
        currentStartDirLabel.grid(row = 0, column = 1, sticky = 'w')
        
        #add Button: "Change Folder". Call back selectDir() 
        changeFolderButton = tk.Button(self, text = "Change Folder", command = self.selectDir)
        changeFolderButton.grid(row = 1, column = 0, sticky = "w")
        
        # add Label: "Regex Filter"
        regexFilterLabel = tk.Label(self, text = "Regex Filter: ")
        regexFilterLabel.grid(row = 2, column = 0, sticky = 'w')
        
        # add Label: "result"
        resultLabel = tk.Label(self, text = "Result:")
        resultLabel.grid(row = 3, column = 0, sticky = 'w')
        
        # add listbox and scrollbar
        scrollBar = tk.Scrollbar(self)
        
        self.listBox = tk.Listbox(self, yscrollcommand = scrollBar.set)
        self.listBox.grid(row = 4, column = 0,sticky = 'nsew', columnspan = 2)
        self.rowconfigure(4, weight = 1)  
        self.columnconfigure(0, weight = 1)  
        
        scrollBar.config(command = self.listBox.yview)        
        scrollBar.grid(row = 4, column = 2, sticky = "wns")
        
        # add empty buffer
        tk.Label(self).grid(row = 5, column = 0, sticky = 'w')
        
        
    def selectDir(self):
        print("Call selectDir")
    def search(self):
        pass



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

