import mysql.connector


config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost:3306',
  'database': 'users',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)