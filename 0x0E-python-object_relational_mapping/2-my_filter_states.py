#!/usr/bin/python3
"""
filter states by user input
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
        c = db.cursor()
        query = "SELECT * FROM states\
        WHERE name = '{}'\
        ORDER BY id ASC".format(argv[4])
        c.execute(query)
        for row in c.fetchall():
            print(row)
    except IndexError:
        print("Give 4 arguments in the format \
        |mysql user| |mysql password| |database name| |state name|")
    except Exception as e:
        print("EXECEPTION {}", e)
