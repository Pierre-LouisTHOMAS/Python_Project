import pymysql


def mysqlconnect():

#To connect MySQL database. Change the database name as per requirement

conn = pymysql.connect(

host='localhost',

user='root',

password="",

db='myproject',

)

#Change the name of the table as per requirement

cur = conn.cursor()

cur.execute("select * from customer")

output = cur.fetchall()

print(output)



# To close the connection

conn.close()





# Driver Code

if __name__ == "__main__":

mysqlconnect()