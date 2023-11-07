import pymysql
import platform

import runpy

system = platform.system()

def mysqlconnect():
    #To connect MySQL database. Change the database name as per requirement

    conn = pymysql.connect(

        host='localhost',

        user='root',

        password='root',
        db='AirlineDatabase',
        port = 8889
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
    runpy.run_path(path_name='Front/connexion.py')

