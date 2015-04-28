import tkinter
import tkinter.filedialog

##Checks to see if there is a file called "Current Deck List" in the current
##directory. If there isn't, the program will prompt the user to located it.

def locateDeck():

    try:
        deckList = open("Current Deck List.txt",'r+')
        deckList.close()
        directory = "Current Deck List.txt"
        return directory
    except FileNotFoundError:
        x = """"Current Deck List" was not found in current directory"""
        print(x)
        print("Please locate text file with Deck List.")
        while True:           
            root = tkinter.Tk()
            root.update()
            directory = tkinter.filedialog.askopenfilename()
            print(directory)
            root.withdraw()
            if directory.endswith(".txt"):
                break
            print("""Please locate a file with a ".txt" extension!""")
        return directory

#Card inputed by the user will be added to the file.
    
def addCard(d):
    deck = open(d,'w')
    card = getCardName()
    deck.write(card)
    deck.close()
    print("The card " + card + "has been successfully added to the deck list.")

#A card name will be prmpted by the user.
    
def getCardName():

    a = input("Please enter the name of the card you would like to add.\n")
    print("Please verify that the card name is spelled correctly:")
    print(a.upper())
    c = input("Is this correct? Please enter yes/no\n")
    while True:
        if c == "yes":
            a = a.upper()
            return a
        elif c == "no":
            return getCardName()
        else:
            print("""Please enter either "yes" or "no".""")
            c = input()            
        
    
def main():
    directory = locateDeck()
    addCard(directory)
    
    

main()
