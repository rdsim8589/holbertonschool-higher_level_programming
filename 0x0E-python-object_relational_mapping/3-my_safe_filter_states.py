#!/usr/bin/python3
"""
filter states by user input
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    import re

    try:
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
        c = db.cursor()
        state = re.sub(r'\W+', '', argv[4].split(";")[0])
        query = "SELECT * FROM states\
        WHERE name = '{:s}'\
        ORDER BY id ASC".format(state)
        test = c.execute(query)
        if test is 0:
            print("execute failed!")
        for row in c.fetchall():
            if row[1] == argv[4]:
                print(row)
        c.close()
        db.close()
    except IndexError:
        print("Give 4 arguments in the format \
        |mysql user| |mysql password| |database name|")
    except Exception as e:
        print("EXECEPTION {:}".format(e))
