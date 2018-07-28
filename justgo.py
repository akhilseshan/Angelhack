from django.db import connection

def my_custom_sql(self):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bus_details where from_=%s",[self.id])
    row = cursor.fetchall()
    return row
