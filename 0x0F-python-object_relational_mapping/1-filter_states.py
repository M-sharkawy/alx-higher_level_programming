#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa."""

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

    cursor.execute("SELECT * FROM states ORDER BY states.id;")

    [print(row) for row in cursor.fetchall() if row[1][0] == "N"]

    cursor.close()
    db.close()
