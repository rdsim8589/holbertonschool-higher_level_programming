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
        test = c.execute("SELECT cities.name\
        FROM cities INNER JOIN states \
        ON states.id = cities.state_id AND states.name = %s \
        ORDER BY cities.id ASC", (argv[4],))
        if test == 0:
            print("execute failed!")
        cities = []
        for row in c.fetchall():
            cities.append(row[0])
        print(", ".join(cities))
    except IndexError:
        print("Give 4 arguments in the format \
        |mysql user| |mysql password| |database name| |state name|")
    except Exception as e:
        print("EXECEPTION {:}".format(e))
