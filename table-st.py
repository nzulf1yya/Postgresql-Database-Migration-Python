import psycopg2
from conf import config
from alembic import op
import sqlalchemy as sqlalchemy

connection = None
connection = psycopg2.connect(
    database='stdb',
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)
print("connected")



# cur.execute("""
# CREATE TABLE Interests(
# STUDENT_ID INT,
# INTEREST CHAR(15)
# ),
# Students(
# ST_ID INT,
# ST_NAME CHAR(15)
# ST_LAST CHAR(15)
# )
# """)

## create students and interests sample tables
def student_info():
    commands = (
        """
        CREATE TABLE students (
        st_id integer,
        st_name char(15),
        st_last char(15)
        )
        """,
        """
        CREATE TABLE interests (
        student_id integer,
        interest char(15)
        )
        """)

    try:
        cursor = connection.cursor()
        for commandd in commands:
            cursor.execute(commandd)
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if connection is not None:
            print("Sucessfully created")

if __name__ == '__main__':
    student_info()























