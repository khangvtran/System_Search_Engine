#lab 4: system calls, package, GUI and regex review
from findwin import *
import sys

def usage():
    """ print Usage message if command line is invalid
        Valid format:  python  lab4.py   directory_path   regex
    """
    print("Usage:", end=' ')
    print("lab4.py <search directory> <regular expression filter>")



def main() :
    numArgv = len(sys.argv)
    
    # if command line argument has only one word, instantiate the GUI window and run the mainloop
    if numArgv == 1:
        app = FindWin()
        if platform.system() == 'Darwin': 
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
            os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid())) 
        app.mainloop()        
    
    # else if 3 words in command line argument,
    elif numArgv == 3:
        # if the 2nd word is not a valid directory, print error message and return
        try:
            if not os.path.isdir(sys.argv[1]):
                raise FileNotFoundError
        except FileNotFoundError as e:
            print("Directory not found: " + sys.argv[1])
            return
        
        # otherwise compile the regex in the 3rd word on the command line
        try :
            regex = re.compile(sys.argv[2], re.I)
        except Exception as e :
            print("Invalid regex: " + str(e))
            return
        
        # run the search of the FileSearch object and print all the filenames
        fileSearchObject = FileSearch(sys.argv[1])
        fileSearchObject.searchName(regex)
        print([file for file in fileSearchObject.searchResult])
        
    # else, show the instruction    
    else:
        usage()

main()

