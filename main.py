import sys
import mariadb
from credentials import cur, conn

ins_room_name = input("Please insert the room name: ")

def insert_room(room_name):
    try:
        sql_query=("insert into rooms (name) values (%s);")
        sql_data = (room_name,)
        cur.execute(sql_query, sql_data)
        conn.commit()
    except mariadb.Error as e:
        print(f"Error adding entry to database: {e}")
    finally:
        if conn:
            conn.close()

insert_room(ins_room_name)