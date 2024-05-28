import telebot
import sqlite3


def get_users():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, status, first_name FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
