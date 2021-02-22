import psycopg2
#run students table multiple times, so some records inserted multiple times, to delete it, use this code
def deleterows(records):
    try:
        connection = psycopg2.connect(user="postgres",
                                         password="root",
                                         host="localhost",
                                         port="5432",
                                         database="stdb")
        cursor = connection.cursor()
        deletequery = """Delete from students where st_id = %s"""
        cursor.executemany(deletequery, records)
        connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Record Deleted")

    except (Exception, psycopg2.Error) as error:
        print("Error happened: ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

id = [(1, ), (2, ), (3, )]
deleterows(id)
