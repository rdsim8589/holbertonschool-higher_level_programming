#!/usr/bin/python3
"""
This module list all cities
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
        c = db.cursor()
        query = "SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states \
        ON states.id = cities.state_id ORDER BY cities.id ASC"
        c.execute(query)
        for row in c.fetchall():
            print(row)
    except IndexError:
        print("Give 3 arguments in the format \
        |mysql user| |mysql password| |database name|")
    except Exception as e:
        print("EXECEPTION {:}".format(e))
