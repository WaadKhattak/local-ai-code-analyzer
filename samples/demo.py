import sqlite3
import os

def login(user_input_username, user_input_password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input_username}' AND password = '{user_input_password}'"
    cursor.execute(query)
    return cursor.fetchone()

def execute_command(command):
    os.system("ping " + command)
