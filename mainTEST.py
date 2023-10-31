import pymysql
import platform

system = platform.system()

def mysqlconnect():
    #To connect MySQL database. Change the database name as per requirement

    if system == "Darwin":
        #print("Vous êtes sur un Mac.")
        port = 8889
    elif system == "Windows":
        #print("Vous êtes sur Windows.")
        port = 3306

    conn = pymysql.connect(

        host='localhost',

        user='root',

        password='root',

        db='AirlineDatabase',


    )

    #Change the name of the table as per requirement

    cur = conn.cursor()

    cur.execute("SELECT * FROM Client")

    output = cur.fetchall()

    print(output)


    # To close the connection

    conn.close()


if __name__ == "__main__":
    mysqlconnect()
