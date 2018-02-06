# Author: Khang Vinh Tran
# Local System File Search Engine
# Assignment 4
# CIS 41B

import os 
import os.path
import re

class FileSearch():
    def __init__(self, startDir):   
        self.absPathDict = { }
        walkResult = os.walk(startDir)                    # recursively walk down all path of the directory
        for (path, dirList, fileList) in walkResult:      # store all files (including directory) into a dictionary using filenames as keys
            [self.absPathDict.update({d : os.path.join(path, d)}) for d in dirList]   
            [self.absPathDict.update({f : os.path.join(path, f)}) for f in fileList]   
        #print(self.absPathDict)
                
    def searchName(self, regex):
        self.searchResult = [self.absPathDict[fileName] for fileName in self.absPathDict if regex.search(self.absPathDict[fileName])]
        #print(self.searchResult)
    
    
#############################################################
######################### Test Area ######################### 
############################################################# 
  
'''      
testDir = '/Users/KVTran/Documents/CIS41B/Module4_System/System_Search_Engine'
testDir2 = '/Applications'
testDir3 = '/Users/KVTran/Documents/ECON'
testString = 'lab4'
fileSearchObject = FileSearch(testDir)
fileSearchObject.searchName(re.compile(testString))

'''