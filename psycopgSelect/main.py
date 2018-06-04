#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
psycopg select sample code
main function
"""

import psycopg2



DBNAME = 'dbname'
USER = 'user'
PASSWORD = 'password'
HOST = 'localhost'
PORT = 50001



# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

	try:
		connection = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (DBNAME, USER, PASSWORD, HOST, PORT,))
		cursor = connection.cursor()

		cursor.execute('SELECT * FROM "TestTable" WHERE "id" = 1000 ORDER BY "id"')
		rows = cursor.fetchall()
		for row in rows:
			print(row)

		cursor.close()
		connection.close()

	except (psycopg2.OperationalError) as e:
		print(e)

	return 0
