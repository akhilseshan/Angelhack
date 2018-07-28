from django.db import connection

def my_custom_sql(self):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts_account where id=%s",[self.id])
    row = cursor.fetchall()
    return row
