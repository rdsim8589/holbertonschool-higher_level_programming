#!/usr/bin/python3
"""
This the select state module
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
        c.execute("""SELECT * FROM states ORDER BY id ASC""")
        for row in c.fetchall():
            print(row)
    except IndexError:
        print("Give 3 arguments in the format \
        |mysql user| |mysql password| |database name|")
    except Exception as e:
        print("EXECEPTION {}", e)
