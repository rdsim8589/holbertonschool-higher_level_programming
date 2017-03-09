#!/usr/bin/python3
"""
filter states by user input
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             port=3306)
        c = db.cursor()
        test = c.execute("SELECT * FROM states\
        WHERE name = %s\
        ORDER BY id ASC", (argv[4],))
        while test > 0:
            test = test - 1
            print(c.fetchone())
        c.close()
        db.close()
    except IndexError:
        print("Give 4 arguments in the format \
        |mysql user| |mysql password| |database name|")
    except Exception as e:
        print("EXECEPTION {:}".format(e))
