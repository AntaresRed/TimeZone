import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Anuj 2265",
    database = "data"
)

mycursor = mydb.cursor()

def location(username):
    username = str(username)
    mycursor.execute(f"SELECT location FROM userinfo WHERE name = '{username}'")
    myresults = mycursor.fetchall()
    print(myresults)
    for row in myresults:
        loc = row[0]
        loc = str(loc)
        return loc
        