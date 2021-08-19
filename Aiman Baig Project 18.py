

import random

class States:     
    def __init__(self):
        
        self.statesCapitals = {}
        gameFile = open("statesAndCapitals.txt", "r")

        for line in gameFile:
            if line != "\n":                                        # check for EOL/EOF
                dictList = line.split(",")                          # split the input at comma
                dictList[1] = dictList[1].strip('\n')               # strip the new line tag
                self.statesCapitals[dictList[0]] = dictList[1]      # add to dictionary

        gameFile.close()
     
    def MyMethod(self):
        
        state, capital = random.choice(list(self.statesCapitals.items()))       # get random key pair from statesCapitals dictionary
        capitalChk = capital.lower()                                            # comparisons made in lowercase for user friendliness
        print("\n" + "What is the Capital of " + state + "\n")                  # ask the question
        answer = input("Your answer > ")                
        answerChk = answer.lower()                                              # convert giver answer to lowercase for comparison

        if answerChk == capitalChk:
            print("\n" + "Correct! " + capital + " is the Capital of " + state) # if right or wrong accordingly
        else:
            print("\n" + "Incorrect. The Capital of " + state + " is " + capital)

    def display(self):
        i = 1                                                               # Print out dictionary if user wants to review
        printLine = ""

        for key in sorted(self.statesCapitals):                          # Format display of data for 3 colums each 26 characters wide
                 
            temp = key + ", " + self.statesCapitals[key]         
            temp = temp.ljust(26)
            printLine = printLine + temp
                
            if i == 3:
                print(printLine)
                i = 1
                printLine = ""
            else:
                i += 1
        print(printLine)                                    # print last two keys and values stored in printLine var           
        print("--------------------------------------------------------------------------------") 

def mainMenu ():
    
    print("\n" + "--------------------------------------------------------------------------------")
    print("Let's play a game!" + "\n")
    print("I will name a State and you give me the Capital." + "\n")
    print("Don't worry about using capital letters.")
    print("--------------------------------------------------------------------------------")

    choice = input("\n" + "Would you like to review first? (y/n) > ")
    
    if choice.lower() == 'y':
        print("\n" + "--------------------------------------------------------------------------------")

        states.display()

        choice = input("\n" + "Ready to play? (y/n) > ")

        if choice.lower() == 'y':
            runGame(choice)                                 # if yes call runGame otherwise exit program
            return       
        else:
            return
    else:
          runGame('y')

    return                                                  # exit mainMenu function


def runGame(choice):

    print("\n" + "Here we go!" + "\n")
    print("--------------------------------------------------------------------------------")

    while choice.lower() == 'y':
        states.MyMethod()
        choice = input("\n" + "Try another (y/n) > ")                       # go again?
        
    return


# begin execution here
states = States()
mainMenu()
print("\n" + "Thank you for playing" + "\n")






















