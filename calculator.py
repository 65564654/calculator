import math, time, random
#Prints the introduction
print("""Welcome to my calculator!
By: Lukas
Version: 0.1 beta
Release date: 10/5/2020
All actions are done as commands in the terminal and enter help for a list of simple commands.""")
returnVariable = 0 #stores the number that is returned
operationList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "/", "+", "-", "^", "(", ")", "."]#stores numbers, parenthesis, and operations
operations = operationList[10:15] #stores all the basic operations
operationListShort = operationList[0:15] #Stores everything except parenthesis
def root(calc): #root function by making it into float,taking the root, and then converting to integer if no decimal and to float if it has a decimal 
    global returnVariable
    simpleArithmetic(calc)
    calc = float(returnVariable) 
    calc = math.sqrt(calc) 
    if int(calc) == calc:
        calc = int(calc)
    returnVariable = str(calc)
def simpleArithmetic(calc):#used to run very simple adding subtracting dividing and multiplying with order of operations
    global returnVariable
    for type in operations:
        operation = calc.find(type) #stores where the earliest operation sign is
        while not calc.find(type) == -1: #Checks if there is still a valid operation sign
            distance = 0 #variable used for how far through the calculation is
            firstNumber = []#clears ffirstNumber and then appends the location of operation signs 
            for x in operations:
                firstNumber.append(calc.find(x, distance))
            firstNumber = [len(calc) + 1 if x == -1 else x for x in firstNumber] #replaces them with a number at the end of the string if they do not exist
            firstNumber1 = min(firstNumber) #finds the smallest number
            if firstNumber1 == operation: #checks if the operation being calculated is the first
                firstNumber1 = distance
            else:
                firstNumber1 += 1
            distance = operation + 1
            #does the same as for the first number but for the second
            secondNumber = []
            for x in operations:
                secondNumber.append(calc.find(x, distance))
            secondNumber = [len(calc) if x == -1 else x for x in secondNumber]
            secondNumber1 = min(secondNumber)
            #calculates what the 2 numbers being used are
            firstNumber2 = float(calc[firstNumber1:operation])
            secondNumber2 = float(calc[operation + 1:secondNumber1])
            #does the valid operation on the 2 numbers
            if type == "*":
                replaceWith = firstNumber2 * secondNumber2
            elif type == "/":
                replaceWith = firstNumber2 / secondNumber2
            elif type == "+":
                replaceWith = firstNumber2 + secondNumber2
            elif type == "-":
                replaceWith = firstNumber2 - secondNumber2
            elif type == "^":
                replaceWith = firstNumber2 ** secondNumber2
            if int(replaceWith) == replaceWith: #checks if the number needs decimal places
                replaceWith = int(replaceWith)
            #replaces the operation with the answer
            replaceWith1 = str(replaceWith)
            replace = calc[firstNumber1:secondNumber1]
            calc = calc.replace(replace, replaceWith1)
    returnVariable = calc
#finds and runs all functions
def function(calc):
    #Here is a dictionary of all supported functions in a list
    validFunc = {
        "root":root
    }
    closed = calc.find(")") #stores first closed parenthesis
    while not closed == -1: #runs until there are no more closed parenthesis
        open1 = calc.find("(") #finds the mathching open parenthesis and stores it in open2
        while closed > open1:
            open2 = open1
            open1 = calc.find("(", open1 + 1)
            if open1 == -1:
                open1 = len(calc)
        replaceWith = calc[open2 + 1:closed] #stores the inside of the parenthesis
        search = open2 - 1 #Looks at the character infront of the parenthesis
        searched = calc[search]
        while searched not in operationList: #Repeats the process above while checking if it is in operationList
            search -= 1
            searched = calc[search]
        search += 1
        if search == open2: #checks if there was no function before the parenthesis and runs simple arithmetic over it
            replace = calc[open2:closed + 1]
            simpleArithmetic(replaceWith)
        else:#runs the correct function with the input in the parenthesis
            function = calc[search:open2]
            validFunc[function](replaceWith)
            replace = calc[search:closed + 1]
        calc = calc.replace(replace, returnVariable)
        closed = calc.find(")")
    simpleArithmetic(calc)
while True:
    print("____________________________________________")#used to divide commands
    command = input()#stores input
    if command == "help": #prints a simple help
        print("""This is the help page:
Use + to add, - to subtract, * to multiply, / to divide, and ^ to use exponents
Use root(X) to calculate the root of X
Use quit to exit""")
    elif command == "quit": #exits the program
        print("Exiting...")
        time.sleep(5 * random.random())
        quit()
    else: #goes through the functions
        try:
            function(command)
            print(returnVariable)
        except:
            print("Error, You messed up your code or this code has a bug! If this is a bug please report it!")