# Author: Khang Vinh Tran
# Local System File Search Engine
# Assignment 4
# CIS 41B

import os 
import re

class FileSearch():
    def __init__(self, startDir):   
        absPathDict = { }
        walkResult = os.walk(startDir)                    # recursively walk down all path of the directory
        for (path, dirList, fileList) in walkResult:      # store all files (including directory) into a dictionary using filenames as keys
            [absPathDict.update({d : os.path.join(path, d)}) for d in dirList]   
            [absPathDict.update({f : os.path.join(path, f)}) for f in fileList]   
        print(absPathDict)
                
    def searchName(self, regexFilter):
        pass
    
    
#############################################################
######################### Test Area ######################### 
############################################################# 
  
'''    
walkResult = os.walk(testDir)
for (path, dirList, fileList) in walkResult:
    for d in dirList:
        print("d")
        print(d)
        print(os.path.join(path, d))
    for f in fileList :
        print("f")
        print()
        print(os.path.join(path,f))        
'''     
testDir = '/Users/KVTran/Documents/CIS41B/Module4_System'
testDir2 = '/Applications'
testDir3 = '/Users/KVTran/Documents/ECON'
fileSearchObject = FileSearch(testDir3)
