import pymysql

def get_db_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Erreur lors de la connexion à la base de données MySQL: {e}")
        return None
