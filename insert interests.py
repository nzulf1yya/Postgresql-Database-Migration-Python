import psycopg2
#code to insert data into students table
def insertion(info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="localhost",
                                      port="5432",
                                      database="stdb")
        cursor = connection.cursor()
        insertquery = """ INSERT INTO interests (st_id, interest) 
                           VALUES (%s,%s) """

        # executemany() to insert multiple rows
        cursor.executemany(insertquery, info)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into interests table")

    except (Exception, psycopg2.Error) as error:
        print("Insertion failed.Because:   {}".format(error))

    finally:
        if connection is not None:
            cursor.close()
            connection.close()

list = [ (1,'literature' ) , (1,'math'), (2, 'coding'),(3,'chemistry' ) , (2,'dancing'), (3, 'singing')]
insertion(list)