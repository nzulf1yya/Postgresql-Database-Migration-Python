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
        insertquery = """ INSERT INTO students (st_id, st_name, st_last) 
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows rows
        cursor.executemany(insertquery, info)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into students table")

    except (Exception, psycopg2.Error) as error:
        print("Insertion failed.Because:   {}".format(error))

    finally:
        if connection is not None:
            cursor.close()
            connection.close()

list = [ (1,'Konul', 'Gurbanova') , (2,'Leyla', 'Huseynova'), (3, 'Namiq', 'Hasanov')]
insertion(list)
