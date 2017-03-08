#!/usr/bin/python3
"""
filter states by user input
"""
if __name__=="__main__":
    from sys import argv
    import MySQLdb
    import re

    try:
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
        c = db.cursor()
        state = ""
        print((argv[4],))
        for character in argv[4]:
            if character == ";":
                break
            state += character
        state = re.sub(r'\W+', '', state)
        query = "SELECT * FROM states\
        WHERE name = '{}'\
        ORDER BY id ASC".format(state)
        c.execute(query)
        for row in c.fetchall():
            print(row)
    except IndexError:
        print("Give 4 arguments in the format \
        |mysql user| |mysql password| |database name| |state name|")
    except Exception as e:
        print("EXECEPTION {:}".format(e))
