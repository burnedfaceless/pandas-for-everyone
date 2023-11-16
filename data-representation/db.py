import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'lscloud',
    'password': 'lscloud',
    'database': 'lscloud'
}

try:
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wells WHERE organization_id = 1")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except mysql.connector.Error as error:
    print("Failed to get record from MySQL table: {}".format(error))




