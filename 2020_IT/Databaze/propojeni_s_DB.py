import mysql.connector
mydb = mysql.connector.connect(
    host="dbs.spskladno.cz",
    user="student22",
    passwd="spsnet",
    database="vyuka22"
)

mycursor = mydb.cursor()
sql_select = "SELECT name FROM `IT2020_Ucitel`;"
mycursor.execute(sql_select)

while True:
    ziskano = mycursor.fetchone()
    if ziskano is None:
        break
    jmeno = ziskano[0]
    print("ucitel se jmenuje ", jmeno)

mycursor.close()
mydb.close()