import dbconfig

def main():
    database = "./main.db"
    conn = dbconfig.create_connection(database)

    if conn is not None:
        # create tables here:
        # create_table(conn, sql_create_linkit_table) etc.
        pass
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()