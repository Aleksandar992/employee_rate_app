DATABASE_CONFIG = {
    'database': 'Project',
    'user': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

import matplotlib.pyplot as plt
import psycopg2 as pg2
from matplotlib import colors

print("------------------------------------------------------------------------")
print("Hy employee. If you want, you can look a different type of average rating.")
print("------------------------------------------------------------------------")

def main():

    def average_rating():
        print()
        print("Enter 1 to see average rating which employee give others from the first to the last employee order by employee_id")
        print("Enter 2 to see average rating with which employe is rate by others from the first to the last employee order by employee_id")
        print("Enter 3 to see average rating for all attributes from the first to the last attribut order by attr_id")

        employe_choice = int(input())
        print()
        
        if employe_choice is 1:
            print("-------------------------------------------")
            print("This is average rating for each employe who rates others")
            
            cur.execute('SELECT ROUND(AVG(rating),2)FROM Transactions GROUP BY employe_id_who_rates ORDER BY employe_id_who_rates ASC')
            AVG = cur.fetchall()
            for a in AVG:
                print(a)

            cur.execute('SELECT first_name FROM Employee')
            name = cur.fetchall()

            columns = print("This is average rating for each employe who rates others")
            rows = name

            chars = AVG

            cmap1 = colors.ListedColormap(['r','g'])
            rate = [0,7,11]
            norm = colors.BoundaryNorm(rate, cmap1.N)


            plt.figure(figsize=(8, 3), dpi=120)

            lightbl = (0.8, 0.9, 0.9)
            tab = plt.table(cellText=chars,
                            rowLabels=rows,
                            colLabels=columns,
                            rowColours=[lightbl] * 10,
                            colColours=[lightbl],
                            cellColours=cmap1(norm(AVG)),
                            cellLoc='center',
                            loc='upper left')

            plt.axis('off')
            plt.title('This is average rating for each employe who rates others')
            plt.show()


        elif employe_choice is 2:
            print("-------------------------------------------")
            print("This is average rating for each employe whom rate others")
            
            cur.execute('SELECT ROUND(AVG(rating),2)FROM Transactions GROUP BY employe_id_whom_rate ORDER BY employe_id_whom_rate ASC')
            AVG1 = cur.fetchall()
            for a1 in AVG1:
                print(a1)
            
            cur.execute('SELECT first_name FROM Employee')
            name = cur.fetchall()

            columns = print("This is average rating for each employe who rates others")
            rows = name

            chars = AVG1

            cmap1 = colors.ListedColormap(['r','g'])
            rate = [0,7,11]
            norm = colors.BoundaryNorm(rate, cmap1.N)


            plt.figure(figsize=(8, 3), dpi=120)

            lightbl = (0.8, 0.9, 0.9)
            tab = plt.table(cellText=chars,
                            rowLabels=rows,
                            colLabels=columns,
                            rowColours=[lightbl] * 10,
                            colColours=[lightbl],
                            cellColours=cmap1(norm(AVG1)),
                            cellLoc='center',
                            loc='upper left')

            plt.axis('off')
            plt.title('This is average rating for each employe whom rate others')
            plt.show()


        elif employe_choice is 3:
            print("-------------------------------------------")
            print("This is average rating for each attribut")
            
            cur.execute('SELECT ROUND(AVG(rating),2)FROM Transactions GROUP BY attr_id ORDER BY attr_id ASC')
            AVG2 = cur.fetchall()
            for a2 in AVG2:
                print(a2)

            cur.execute('SELECT attr_name FROM Attributes')
            name = cur.fetchall()

            columns = print("This is average rating for each attribut")
            rows = name

            chars = AVG2

            cmap1 = colors.ListedColormap(['r','g'])
            rate = [0,7,11]
            norm = colors.BoundaryNorm(rate, cmap1.N)


            plt.figure(figsize=(8, 3), dpi=120)

            lightbl = (0.8, 0.9, 0.9)
            tab = plt.table(cellText=chars,
                            rowLabels=rows,
                            colLabels=columns,
                            rowColours=[lightbl] * 11,
                            colColours=[lightbl],
                            cellColours=cmap1(norm(AVG2)),
                            cellLoc='center',
                            loc='upper left')

            plt.axis('off')
            plt.title('This is average rating for each attribut')
            plt.show()
    

    yeslist = ["yes","y","yeah"] 
    conn = pg2.connect(database='Project',user='postgres',host='localhost',port='5432')
    cur = conn.cursor()

    cur.execute('SELECT * FROM Transactions')
    trans = cur.fetchall()
    for t in trans:
        print(t)

    cur.execute('SELECT * FROM Employee')
    emp = cur.fetchall()
    for e in emp:
        print(e)

    cur.execute('SELECT * FROM Attributes')
    attr = cur.fetchall()
    for at in attr:
        print(at)

    average_rating()  

    avg_rating = input("Do you want to see another average rating? Yes or no? ").lower()
    print("-----------------------------------------------------")

    if avg_rating in yeslist:
        main()
    else:
        quit()

main()
