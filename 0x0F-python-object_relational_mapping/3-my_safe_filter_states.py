#!/usr/bin/python3
"""module that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.(safer)"""

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

    query = "SELECT * \
        FROM states \
            WHERE BINARY name = %s ORDER BY states.id;"
    cursor.execute(query, (sys.argv[4],))

    """print the data fetched"""
    [print(row) for row in cursor.fetchall()]

    """close opened database and cursor"""
    cursor.close()
    db.close()
