#!/usr/bin/python3
"""Module that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="username",
        passwd="password",
        db="database"
    )

    """Create a cursor object"""
    cursor = db.cursor()

    """Execute the SQL query"""
    cursor.execute("SELECT * FROM states ORDER BY states.id DESC")

    """Fetch the results"""
    result = cursor.fetchall()

    """print each row of the results"""
    for row in result:
        print(row)

    """Close the cursor and database"""
    cursor.close()
    db.close()
