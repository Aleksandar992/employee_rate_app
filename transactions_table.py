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
import array

print("In next table we showed with which rating any employee rate others")

conn = pg2.connect(database='Project',user='postgres',host='localhost',port='5432')
cur = conn.cursor()

column = ['employe_id_who_rates', 'employe_id_whom_rate', 'attr_id', 'rating']


cur.execute('SELECT transaction FROM Transactions')
transaction = cur.fetchall()

cur.execute('SELECT employe_id_who_rates, employe_id_whom_rate, attr_id, rating FROM Transactions')
show_transactions = cur.fetchall()


columns = column
rows = transaction

chars = show_transactions


plt.figure(figsize=(8, 5), dpi=120)

lightbl = (0.8, 0.9, 0.9)
tab = plt.table(cellText=chars,
                rowLabels=rows,
                colLabels=columns,
                rowColours=[lightbl] * 20,
                colColours=[lightbl] * 4,
                cellLoc='center',
                loc='upper left')

plt.axis('off')
plt.show()
