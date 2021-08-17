import mariadb
# Module Imports

import mariadb
import sys


def connect():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="biometria"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    return cur


class Connection:
    pass
