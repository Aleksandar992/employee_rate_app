import psycopg2 as pg2
import array

print("Hello, welcome to the app for rating employee attributes in this company.")

def main():

    yeslist = ["yes","y","yeah"]
    conn = pg2.connect(database='Project',user='postgres',host='localhost')
    cur = conn.cursor()
    cur.execute('SELECT first_name, last_name FROM Employee')
    rows = cur.fetchall()
    for rw in rows:
        print(rw)

    usersArray = ['John','Alex','Marry','Michel','Ray','Mia','Jack','Rachel','Ashley','Paul']
    print("What is your name? Please type a number which shows your name.")
    userChoice = int(input())
    print()
    selectedUser = userChoice - 1
    user = usersArray[selectedUser]
    print("Hy, welcome" ,user, ". Which employee you want to rate? Choose a number please.")
    userChoice1 = int(input())
    print()
    selectedUser1 = userChoice1 - 1
    user1 = usersArray[selectedUser1]
    print("Ok,", user,"you choose to rate", user1)
    print("There is a list of attributes.")

    cur.execute('SELECT attr_name FROM Attributes')
    atr = cur.fetchall()
    for a in atr:
        print(a)

    attrsArray = ['productivity','responsibility','commuication','creativity','determination','practical','empathy','logic','resul-orientation','composed','proactive']
    print("Select attribut which you want to rate for", user1, ". Rate is between 1 and 10")
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate1 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate1, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate2 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate2, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate3 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate3, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate4 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate4, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate5 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate5, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate6 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate6, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate7 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate7, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate8 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate8, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate9 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate9, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ".Now you rate", user1, "for this attribut.")
    rate10 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate10, "Do you want to continue rate this employe? Type 1 if you want or 2 if you finish with rating.")
    userChoice = int(input())
    print()

    if userChoice is 1:
        print()
        print("Great", user, "let's continue. Chose next attribut to rate.")
    elif userChoice is 2:
        print("Thank you for your time")
        
    attrChoice = int(input())
    print()
    selectedAttr = attrChoice - 1
    attr = attrsArray[selectedAttr]
    print("Ok, you chose", attr, ". Now you rate", user1, "for this attribut.")
    rate11 = int(input())
    print("Thank you", user, "you rate", attr, "of", user1, "with", rate11, ". You rate", user1, "for all attributes.")
    print("---------------------------------------------------------------------")
    print("Your average rating for", user1, "is", (rate1 + rate2 + rate3 + rate4 + rate5 + rate6 + rate7 + rate8 + rate9 + rate10 + rate11)/11)
    print("---------------------------------------------------------------------")

    emp_rate=input("Do you want to rate another employe? Yes or no? ").lower()
    print("---------------------------------------------------------------------")

    if emp_rate in yeslist:
        main()
    else:
        quit()

main()
        