# Telegram User Access Control Bot

This Python bot is designed to manage user access on messaging platforms, specifically for Telegram. It uses SQLite for database management to handle user statuses, categorizing them into whitelists and blacklists.

## Features

- **User Management**: Allows the bot to add users to either a whitelist or a blacklist to control access to various bot functions.
- **Dynamic User Status Update**: Users can be dynamically added to or removed from lists during runtime.
- **Audio Messaging**: Supports sending audio messages to users.
- **Interactive Commands**: Users can interact with the bot using commands like `/start`, `/clear`, `/addtowhitelist`, and `/addtoblacklist`.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- SQLite3

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/telegram-user-access-control-bot.git
   cd telegram-user-access-control-bot
    ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
    ```

### Usage
## To run the bot, use the following command:

```bash
python main.py
```
Ensure you have set up the necessary bot tokens and database before running in `bot.py`:

```python
import telebot

TOKEN = 'token'

bot = telebot.TeleBot(TOKEN)
```

## Commands

>/start: Starts interaction with the bot and checks user status.

>/addtowhitelist: Adds a user to the whitelist.

>/addtoblacklist: Adds a user to the blacklist.

>/clear: Clears all messages from the chat.

>/showmeusers: Shows a list of all users and their statuses.

# Contributing

Contributions to the Telegram User Access Control Bot are welcome! Here are some ways you can contribute:

+ Report bugs and suggest features.
+ Review the source code and enhance code quality.
+ Document code or write tutorials for the project.

# License
This project is licensed under the MIT License - see the LICENSE file for details.