#!/usr/bin/python3
"""module that takes in the name of a state
as an argument and lists all cities of that state"""

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

    query = "SELECT c.id, c.name AS city_name, \
        s.%s AS state_cities \
            FROM cities c \
                LEFT JOIN states s ON c.state_id = s.id ORDER BY c.id;"
    cursor.execute(query, (sys.argv[4],))

    """print the data fetched"""
    [print(row) for row in cursor.fetchall()]

    """close opened database and cursor"""
    cursor.close()
    db.close()
