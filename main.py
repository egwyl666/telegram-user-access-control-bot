import telebot
from telebot import types
import sqlite3
import database
from user import get_users
from bot import bot

database.create_database()

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    # Check if the user is in the whitelist or if it's a new user
    if database.is_user_in_whitelist(user_id) or not database.is_user_in_blacklist(user_id):
        bot.send_message(user_id, "Welcome!")

        # Code here is only accessible to new users and those on the whitelist
        if not database.is_user_in_whitelist(user_id):
            database.add_to_whitelist(user_id, first_name)
            print(f"Adding a user to the whitelist: user_id={user_id}, first_name={first_name}") #Optional (You can remove it)

        chat_id = message.chat.id

        audio = open('./example.mp3', 'rb')
        bot.send_audio(chat_id, audio)
        audio = open('./example.mp3', 'rb')
        bot.send_audio(chat_id, audio)

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton(text="Example1")
        button2 = types.KeyboardButton(text="Example2")

        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, "Choose your music", reply_markup=keyboard)
    else:
        clear_chat(message)
        bot.send_message(user_id, "You are not authorised to use the bot")

# /clear command
@bot.message_handler(commands=['clear'])
def clear_chat(message):
    # Get the chat ID
    chat_id = message.chat.id
    # Get the ID of the last message in the chat
    last_message_id = message.message_id
    # Delete every message in the chat starting from the last and moving to the first
    while last_message_id > 1:
        try:
            bot.delete_message(chat_id, last_message_id)
            last_message_id -= 1
        except Exception as e:
            break

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Example1")
    button2 = types.KeyboardButton(text="Example2")
    keyboard.add(button1, button2)

# Handler for /showmeusers command
@bot.message_handler(commands=['showmeusers'])
def handle_show_users(message):
    user_id = message.from_user.id
    users = get_users()
    user_list = "User List:\n"
    for user in users:
        user_list += f"ID: {user[0]}, Name: {user[2]}, Status: {user[1]}\n"
    bot.send_message(user_id, user_list)

@bot.message_handler(commands=['addtowhitelist'])
def add_to_whitelist_command(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Please write the user ID you want to add to the whitelist:")
    bot.register_next_step_handler(message, lambda message: add_to_whitelist(message, user_id))

def add_to_whitelist(message, user_id):
    try:
        user_id_to_add = int(message.text)
        user = bot.get_chat_member(user_id_to_add, user_id_to_add)
        first_name = user.user.first_name
        database.add_to_whitelist(user_id_to_add, first_name)
        bot.send_message(message.chat.id, f"User ID {user_id_to_add} ({first_name}) added to the whitelist.")
    except ValueError:
        bot.send_message(message.chat.id, "Invalid ID. Please enter a valid ID as a number.")

@bot.message_handler(commands=['addtoblacklist'])
def add_to_blacklist_command(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, "Please write the user ID you want to add to the blacklist:")
    bot.register_next_step_handler(message, lambda message: add_to_blacklist(message, user_id, first_name))

def add_to_blacklist(message, user_id, first_name):
    try:
        user_id_to_add = int(message.text)
        user = bot.get_chat_member(user_id_to_add, user_id_to_add)
        first_name = user.user.first_name
        database.add_to_blacklist(user_id_to_add, first_name)
        bot.send_message(message.chat.id, f"User ID {user_id_to_add} ({first_name}) added to the blacklist.")
    except ValueError:
        bot.send_message(message.chat.id, "Invalid ID. Please enter a valid ID as a number.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
