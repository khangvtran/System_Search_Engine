#lab 4: system calls, package, GUI and regex review


def usage():
    """ print Usage message if command line is invalid
        Valid format:  python  lab4.py   directory_path   regex
    """
    print("Usage:", end=' ')
    print("lab4.py <search directory> <regular expression filter>")

def main() :
    # if command line argument has only one word, instantiate the GUI window and run the mainloop
    if 
    
    # else if 3 words in command line argument,
    elif 
        # if the 2nd word is not a valid directory, print error message and return
        if 
        
            return
        # otherwise compile the regex in the 3rd word on the command line
        try :
            regex = re.compile(    ,re.I)
        except Exception as e :
            print("Invalid regex: " + str(e))
            return
        # run the search of the FileSearch object and print all the filenames
        
        
    else:
        usage()

main()

