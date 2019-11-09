def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calc():
    
    print ("\033[92m\nType in a number")
    numb1 = input("\033[0m\033[1m")
    print ("\033[92mType in a number")
    numb2 = input("\033[0m\033[1m")
    print ("\033[92mWhat sort of sum do you want?\n1 = add\n2 = minus\n3 = times\n4 = divison")
    typ = input("sum = \033[0m\033[1m")
    
    otr = ""

    if is_number(numb1) == False or is_number(numb2) == False:

        otr = "ERROR: is not a valid input"

    elif typ == "1":
        
        numb3 = float(numb1) + float(numb2)
        
    elif typ == "2":
        
        numb3 = float(numb1) - float(numb2)
        
    elif typ == "3":
        
        numb3 = float(numb1) * float(numb2)
        
    elif ((typ == "4") and (numb2 != "0")):
        
        numb3 = float(numb1) / float(numb2)
    
    elif typ == "4":

        otr = "\033[92m\033[1mYou answer is \033[4m∞"
        file  = open("output.calc", "w")
        file.write("Output = ∞") 
        file.close()
        
    else:
        
        otr = "ERROR: is not a valid input"
        
    if otr == "":

        print ("\033[92m\033[1m\nYou answer is \033[4m" + str(f"{numb3:g}"))
        file  = open("output.calc", "w")
        file.write("Output = " + str(numb3)) 
        file.close()
    
    else:

        print("\033[91m\n" + otr)

    print ("\033[0m\033[92m\033[1m\nPress ENTER to do more sums or any button then ENTER to exit")
    re = input("\033[0m\033[1m")
    
    if re == "":
        
        return True
        
    else:
        
        print("\033[92mThanks for using!")
        return False
        
print("\033[0m\033[1m\033[92mWelcome to my Calculator!")

keepGoing = True

while(keepGoing):

    keepGoing = calc()

