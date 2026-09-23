import os #operating system
def clear_terminal(): #Clears terminal before
    # Check the operating system name
    if os.name == 'nt':  # 'nt' is for Windows
        _ = os.system('cls')
    else:  # 'posix' is for Linux/macOS/Unix
        _ = os.system('clear')

def printTestNum(): #prints test10 - test1
    for testNumber in range(10, 0, -1):
        print(f"Test {testNumber}")

# Call the function to clear the screen
clear_terminal()
def x(): #supposed to exit
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    print(" ")
    print("Saving session...")
    print("...copying shared history...")
    print("...saving history...truncating history files...")
    print("...completed.")
    print("Deleting expired sessions...none found.")
    print(" ")
    print("[Process completed]")
    print(" ")
def menuPrint(): #This prints out the menu aka the options and asks for 'option'
    RED = '\033[31m'
    RESET = '\033[0m'
    print(" ------------------------------------------------ ")
    print("|                                                |")
    print("|    9CT Task 4                                  |")
    print("|    Name : Katrina S                            |")
    print("|    Version : 01.1                              |")
    print("|                                                |")
    print(" ------------------------------------------------ ")
    print(" ")
    print(f"{RED}1. Hello World" )
    print(f"{RED}2. Goodbye World")
    print(f"{RED}3. Goodbye Person")
    print(f"{RED}4. Good Teacher" + RESET)
    print("5. forLoop")
    print("5.5. forLoop2")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("10. Decode a string")
    print("x. To Exit")
    option = input("Enter an option ")
    return option
def option1(): #Hello World
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    print("Hello World")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option2(): #Goodbye World
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    print("Hello World")
    input("------> Program paused - press enter to continue") #Makes a pause in the program
    print("Goodbye World")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option3(): #Goodbye Person
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    print("Hello World")
    name = input("What is your name ? ") 
    print("Goodbye "+ name)
    print("")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option4(): #Good teacher
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    teacherName = input("Teacher's name (try Mr Horan) ")
    if teacherName == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(teacherName + " is an ok teacher")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option5(): #forLoop
    print(" ")
    print ("----Start of Output ---------------------------")
    print ("")
    for numberRange in range (1,500): #for = variable, execution = after in
        print (numberRange) 
    print ("")
    print ("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print("")
def option5_5(): #forLoop2 
    print(" ")
    print("----Start of Output ---------------------------")
    print("")
    for i in range(1,5): #1,2,3,4
        print (i)
        printTestNum() #Test -
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option6(): #whileLoop
    print(" ")
    print("----Start of Output ---------------------------")
    print("")
    while True:
        subject=input ("What is the name of this subject ")
        if (subject) == "Computing Technology" :
            print("")
            print("")
            print("Congratulations!!")
            print("")
            print("")
            print("")
            print("----End of Output -----------------------------")
            print(" ")
            print(" ")
            print(" ")
            break #breaks and leave
        else :
            print ("Not Correct - try again")
def option7(): #string Loop
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    userString = input("What is your string? ")
    for letter in userString:
        print(letter)
    print(" ")
    print("----End of Output -----------------------------")   
    print(" ")
    print(" ")
    print(" ")
def option8(): #Convert to ascii
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    list1 = input("What is your string? ")
    list2 = [ord(character) for character in list1] #converts to ascii

    for item1, item2 in zip(list1, list2): #prints at the same time (it should)
        print(f"{item1} = {item2}")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option9(): #Encode a string
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    original_string = input("What is your string? ") 
    increment_by = 1 

    modified_string = increase_ascii_value(original_string, increment_by) 

    def print_prefix_up_to(i): 
        print(modified_string[:i+1]) 
    for i, (item1, item2) in enumerate(zip(original_string, modified_string)): 
        print(f"{item1}={item2}") 
        print_prefix_up_to(i)
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
def option10(): #Decode a string
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    original_string1 = input("What is your string? ") 
    increment_by1 = 1 

    modified_string1 =decrease_ascii_value(original_string1, increment_by1) 

    def print_prefix_up_to(i1): 
        print(modified_string1[:i1+1]) 
    for i1, (item1_1, item2_1) in enumerate(zip(original_string1, modified_string1)): 
        print(f"{item1_1}={item2_1}") 
        print_prefix_up_to(i1)
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
while True: #keep running options

    import os

    def clear_terminal():
        # Check the operating system name
        if os.name == 'nt':  # 'nt' is for Windows
            _ = os.system('cls')
        else:  # 'posix' is for Linux/macOS/Unix
            _ = os.system('clear')
    def printTestNum(): #prints test10 - test1
        for testNumber in range(10, 0, -1):
            print(f"Test - {testNumber}")
    def increase_ascii_value(input_string, increment_value): #gets ascii value and makes a new string by decoding

        new_characters = []
        for char in input_string:
            # Get the ASCII value, add the increment, and convert back to a character
            new_char_code = ord(char) + increment_value
            try:
                new_char = chr(new_char_code)
                new_characters.append(new_char)
            except ValueError:
                # Handle cases where the new value is outside the valid Unicode range
                print(f"Warning: ASCII value {new_char_code} is out of range for character '{char}'. Skipping or handling differently.")

        return "".join(new_characters)
    def decrease_ascii_value(input_string1, increment_value1): #gets ascii value and makes a new string by decoding

        new_characters1 = []
        for char1 in input_string1:
            # Get the ASCII value, add the increment, and convert back to a character
            new_char_code1 = ord(char1) - increment_value1
            try:
                new_char1 = chr(new_char_code1)
                new_characters1.append(new_char1)
            except ValueError:
                # Handle cases where the new value is outside the valid Unicode range
                print(f"Warning: ASCII value {new_char_code1} is out of range for character '{char1}'. Skipping or handling differently.")

        # Join the list of characters into a single string
        return "".join(new_characters1)

    # Call the function to clear the screen
    clear_terminal()
    number = menuPrint() #prints menu + makes number = userinput
    if number == "x":
        x()
        break
#runs all
    elif number == "1": 
        option1() 
        input ("Press Enter to continue")
        print("sh: cls: command not found") #prints regardless of input so idk why its here but dont delete it (might be a typo ngl)
        clear_terminal()
    elif number == "2":
        option2 ()
        input ("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "3":
        option3 ()
        input ("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "4":
        option4 ()
        input ("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "5":
            option5 ()
            input ("Press Enter to continue")
            print("sh: cls: command not found")
            clear_terminal()
    elif number == "5.5":
        option5_5()
        input("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "6":
        option6()
        input("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "7":
        option7()
        input("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "8":
        option8()
        input("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "9":
        option9()
        input("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()
    elif number == "10":
        option10()
        input("Press Enter to continue")
        print("sh: cls: command not found")
        clear_terminal()

    else: #invalid options - press enter to continue
            print ("----Start of Output ---------------------------")
            print ("")
            print ("invalid option")
            print ("")
            print ("----End of Output -----------------------------") 
            print ("")
            print ("")
            input ("Press Enter to continue")
            clear_terminal()

