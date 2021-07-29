import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Anuj 2265",
    database = "data"
)

mycursor = mydb.cursor()

def update(username,userlocation):
    name = username
    print(name)
    formula = ("UPDATE userinfo SET location = %s WHERE name = %s")
    mycursor.execute(f"SELECT EXISTS(SELECT * from userinfo WHERE name = '{name}')")
    myresults = mycursor.fetchall()
    y = myresults[0][0]
    print(y)
    if y == 0:
        return 0
    else:
        inputdata = (userlocation, username)
        mycursor.execute(formula, inputdata)
        mydb.commit()
        return 1
