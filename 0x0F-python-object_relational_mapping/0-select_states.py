#!/usr/bin/python3
"""Module that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

"""Connect to the database"""
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    """Create a cursor object"""
    cursor = db.cursor()

    """Execute the SQL query"""
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    """Fetch the results"""
    result = cursor.fetchall()

    """print each row of the results"""
    for row in result:
        print(row)

    """Close the cursor and database"""
    cursor.close()
    db.close()
