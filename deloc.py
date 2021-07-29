import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Anuj 2265",
    database = "data"
)

mycursor = mydb.cursor()

def rem(member):
    member = str(member)
    mycursor.execute(f"DELETE FROM `userinfo` WHERE `name` = '{member}'")
    mydb.commit()
    return 0 