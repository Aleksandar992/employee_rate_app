DATABASE_CONFIG = {
    'database': 'Project',
    'user': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

import matplotlib.pyplot as plt
import psycopg2 as pg2

print("Hello, welcome to the app for rating employee attributes in this company.")

def main():

    def repeat_fun(times, f):
        for i in range(times): f()

    def Employee_and_Attributes_Rating():
        selected_attribut = int(input())
        print()

        if selected_attribut in range (1,12):

            rating_attribut = selected_attribut - 1
            attribut_for_rating = attributes[rating_attribut]
            print("Ok, you chose", " ".join (attribut_for_rating), ".Now you rate", " ".join (employe_selected_for_rating), "for this attribut.")

            rate = int(input())
            
            if rate in range(1,11):
                print("Thank you", " ".join (employe_selected_to_rate_other_employee), "you rate", " ".join (attribut_for_rating), "of", " ".join (employe_selected_for_rating), "with", rate, ". Do you want to continue rate this employe?")
                print("If you want to continue rating press 1, otherwise press 2.")
            else:
                print("Sorry, but this number is out of range")
                print("Chose again attribut please." )
                return selected_attribut
            
            selected_employe = int(input())
            print()

            if selected_employe is 1:
                print()
                print("Great", " ".join (employe_selected_to_rate_other_employee), "let's continue. Chose next attribut to rate.")
            elif selected_employe is 2:
                print("Thank you for your time")
                quit()

        else:
            print("That's an invalid number. Chose attribut again please.")
            return selected_attribut

    yeslist = ["yes","y","yeah"]   
    
    conn = pg2.connect(database='Project',user='postgres',host='localhost',port='5432')
    cur = conn.cursor()

    cur.execute('SELECT first_name, last_name FROM Employee')
    rows = cur.fetchall()
    for rw in rows:
        print(" " . join(rw))


    print("What is your name? Please type a number which shows your name.")

    selected_employe = int(input())
    print()

    if selected_employe in range(1,11):

        selected_employe_to_rate_others = selected_employe - 1
        employe_selected_to_rate_other_employee = rows[selected_employe_to_rate_others]
        print("Hy, welcome" ," ".join (employe_selected_to_rate_other_employee), ". What employee do you want to rate? Choose a number please.")

        employee_for_rating = int(input())
        print()

        selected_employe_for_rating = employee_for_rating - 1
        employe_selected_for_rating = rows[selected_employe_for_rating]

        if employe_selected_for_rating == employe_selected_to_rate_other_employee:
            print("Sorry, but you can't rate yourself.")
            quit()
        
        print("Ok,"," ".join (employe_selected_to_rate_other_employee),"you choose to rate", " ".join (employe_selected_for_rating))
        print("There is a list of attributes.")
    
    else:
        print("That's an invalid number, try again")
        return 

    cur.execute('SELECT attr_name FROM Attributes')
    attributes = cur.fetchall()
    for a in attributes:
        print(" " . join(a))   

    print("Select attribut which you want to rate for", " ".join (employe_selected_for_rating), ". Rate is between 1 and 10")

    repeat_fun(len(attributes), Employee_and_Attributes_Rating)

    print("Thank you", " ".join (employe_selected_to_rate_other_employee), "you rate", " ".join (employe_selected_for_rating), "for all attributes.")

    print("-----------------------------------------------------")
    print("Rating sum which you gave"," ".join (employe_selected_for_rating), "is:") 

    rating_sum = int(input())

    print("-----------------------------------------------------")

    print("Your average rating for", " ".join (employe_selected_for_rating), "is", (rating_sum)/len(attributes))

    import transaction_rating
    
    emp_rate = input("Do you want to rate another employe? Yes or no? ").lower()
    print("-----------------------------------------------------")

    if emp_rate in yeslist:
        main()
    else:
        quit()

if __name__ == "__main__":
    main()
    

