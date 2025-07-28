Install the discord.py library: If you haven’t already installed discord.py, you can do so using pip. Open your terminal or command prompt and run the following command:

Copypip install discord.py
Create your bot on Discord Developer Portal:

Go to the Discord Developer Portal.
Click on "New Application".
Name your application and click "Create".
On the left sidebar, go to the "Bot" tab and click "Add Bot".
After creating the bot, you'll find the Token. Copy this token as you'll need it in your bot script.
Create the bot script: Below is a simple bot script that logs in and prints a message when it's ready. It also includes the construction of an invite link.

Copyimport discord

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    invite_link = discord.utils.oauth_url(client.user.id, permissions=discord.Permissions(permissions=8))
    print(f'Invite your bot using this link: {invite_link}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
Run your bot:

Save the script to a file, for example, my_discord_bot.py.
Open your terminal or command prompt, navigate to the folder where your script is located, and run:
Copypython my_discord_bot.py
Invite your bot: After running the script, you should see an invite link printed in the terminal. Use that link to invite your bot to your Discord server.

Important Notes:
Ensure that the bot has the necessary permissions in your server when you generate the invite link.
You can customize the bot's functionality by adding more commands and events as needed.
Make sure to keep your bot token secure and never share it publicly.