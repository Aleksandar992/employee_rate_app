DATABASE_CONFIG = {
    'database': 'Project',
    'user': 'postgres',
    'host': 'localhost',
    'port': '5432'
}
import psycopg2 as pg2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors

print("Hello, welcome to the app for rating employee attributes in this company.")

conn = pg2.connect(database='Project',user='postgres',host='localhost',port='5432')
cur = conn.cursor()

cur.execute('SELECT first_name FROM Employee')
name = cur.fetchall()


cur.execute('SELECT attr_name FROM Attributes')
attribut = cur.fetchall()

cur.execute('SELECT Jack, Alex, Marry, Michel, Ray, Mia, Jack, Rachel, Ashley, Paul FROM Rating')
rating = cur.fetchall()


columns = name
rows = attribut


chars = rating

cmap1 = colors.ListedColormap(['r', 'orange', 'g'])
rate = [1,4,8,11]
norm = colors.BoundaryNorm(rate, cmap1.N)


plt.figure(figsize=(8, 3), dpi=120)

lightbl = (0.8, 0.9, 0.9)
tab = plt.table(cellText=chars,
                rowLabels=rows,
                colLabels=columns,
                rowColours=[lightbl] * 11,
                colColours=[lightbl] * 10,
                cellColours=cmap1(norm(rating)),
                cellLoc='center',
                loc='upper left')

plt.axis('off')
plt.show()
