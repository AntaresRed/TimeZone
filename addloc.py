import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Anuj 2265",
    database = "data"
)

mycursor = mydb.cursor()
formula = "INSERT INTO userinfo (name,location) VALUES (%s,%s)"
def add(username,userlocation):
    y = 0
    mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'data'")
    myresults = mycursor.fetchall()
    for x in myresults:
        if x[0]==0:
            mycursor.execute("CREATE TABLE userinfo (name VARCHAR(50), location VARCHAR(50))")
            inputdata = (username,userlocation)
            mycursor.execute(formula,inputdata)
            mydb.commit()
            return 1
        else:
            name = username
            mycursor.execute(f"SELECT EXISTS(SELECT * from userinfo WHERE name = '{name}')")
            myresults = mycursor.fetchall()
            y = myresults[0][0]
            print(y)
            y = int(y)
            if y == 1:
                return 0
            else:
                inputdata = (username,userlocation)
                mycursor.execute(formula,inputdata)
                mydb.commit()
                return 1



    