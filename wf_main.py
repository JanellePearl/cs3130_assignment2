#cs3130 Assignment 2
#Janelle Montgomery
#Reading from a file and counting the word(string) frequency
#Main program

import wf_table

def display():
    print("--")
    print("Word Frequency Table Generator")
    print("\n")
    print("Enter name of file to process:")
    print("--")
    
def get_file():
    obtained = False
    while not obtained:
        try:
            filename = input().strip()
            openfile = open(filename,'r')
            readfile = openfile.read()
            openfile.close()
            obtained = True

        except FileNotFoundError:
            print("\n")
            print("The file does not exist please try again.")
            

    
    return readfile
        
   

def main():
    display()
    file = get_file()
    print("--\n")
    print("file processing complete\n")
    wf_table.table(file)

if __name__ == "__main__":
    main()
