Introduction -

This project is a simple and interactive Discord bot developed using Python. The bot is designed to respond to user messages in a Discord server and perform basic actions such as greeting users and sending random memes.

The main purpose of this project is to understand how Python can be used to create real-time applications that communicate with online platforms like Discord. It also demonstrates the use of external APIs and event-driven programming.

Objectives -

The objectives of this project are:

1. To learn how Discord bots work
2. To understand how to connect Python programs with Discord
3. To use an external API to fetch real-time data
4. To implement message-based commands
5. To build a fun and interactive application

Features -

The bot provides the following features:

1. Responds with a greeting when the user types hello
2. Sends a random meme when the user types meme
3. Connects to Discord using a secure bot token
4. Works in real time while the program is running

Technologies Used -

1. Python
2. discord.py library
3. requests library
4. JSON
5. Discord Developer Portal

Working of the Bot -

1. The bot continuously listens for messages in a Discord server. When a user sends a message:
2. Discord sends the message event to the bot
3. The bot checks who sent the message
4. The bot checks the content of the message
5. If the message starts with hello, the bot sends a greeting
6. If the message starts with meme, the bot fetches a random meme using an online API and sends it

This process happens instantly and allows the bot to interact with users in real time.

Installation and Execution -

Step 1: Install Required Libraries

pip install discord.py requests

Step 2: Create a Bot in Discord

a. Create a new application in Discord Developer Portal
b. Add a bot to the application
c. Copy the bot token
d. Enable Message Content Intent
e. Invite the bot to your server

Step 3: Add Token in Code

Replace the token in the program file:

client.run('YOUR_TOKEN_HERE')

Step 4: Run the Program

python bot.py


If successful, the terminal will display:
Logged on as BotName!

Commands Used -
Command	Function
hello - Bot sends a greeting
meme - Bot sends a random meme

Conclusion -

The Meme & Greeting Discord Bot is a simple yet effective project that demonstrates the integration of Python with Discord. It provides interactive features and serves as a beginner-friendly introduction to bot development and API usage. This project lays the foundation for more advanced bots and automation systems in the future.