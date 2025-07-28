import discord
def print_heading():
    heading = """
    #############################################
    #                                           #
    #               BYPASS CITY                 #
    #                                           #
    #############################################
    """
    print(heading)

if __name__ == "__main__":
    print_heading()
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
