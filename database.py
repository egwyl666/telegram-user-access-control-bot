import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY, user_id INTEGER, first_name TEXT, status TEXT)''')
        conn.commit()
        conn.close()
        print("Database and users table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database and users table: {e}")

def drop_database():
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        conn.commit()
        conn.close()
        print("Database deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting database: {e}")

# Function to check if a user is in the blacklist
def is_user_in_blacklist(user_id):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id FROM users WHERE user_id = ? AND status = ?", (user_id, 'blacklist'))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Function to check if a user is in the whitelist
def is_user_in_whitelist(user_id):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id FROM users WHERE user_id = ? AND status = ?", (user_id, 'whitelist'))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def add_to_blacklist(user_id, first_name):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Remove the user from the whitelist if they are there
    cursor.execute(
        "DELETE FROM users WHERE user_id = ? AND status = ?", (user_id, 'whitelist'))

    # Add the user to the blacklist
    cursor.execute("INSERT INTO users (user_id, first_name, status) VALUES (?, ?, ?)",
                   (user_id, first_name, 'blacklist'))

    conn.commit()
    conn.close()

def add_to_whitelist(user_id, first_name):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Remove the user from the blacklist if they are there
    cursor.execute(
        "DELETE FROM users WHERE user_id = ? AND status = ?", (user_id, 'blacklist'))

    # Add the user to the whitelist
    cursor.execute("INSERT INTO users (user_id, first_name, status) VALUES (?, ?, ?)",
                   (user_id, first_name, 'whitelist'))

    conn.commit()
    conn.close()

def update_user_status(user_id, status, first_name=None):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    if status == 'whitelist':
        cursor.execute(
            "DELETE FROM users WHERE user_id = ? AND status = ?", (user_id, 'blacklist'))
    elif status == 'blacklist':
        cursor.execute(
            "DELETE FROM users WHERE user_id = ? AND status = ?", (user_id, 'whitelist'))

    cursor.execute("INSERT INTO users (user_id, first_name, status) VALUES (?, ?, ?)",
                   (user_id, first_name, status))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # You can call this function to create the database when the module is run
    create_database()
