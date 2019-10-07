import discord
import packt
import os

discordToken = os.environ.get('discordToken')
if (discordToken is None):
    import config
    discordToken = config.discordToken

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '!packtpub':
            await message.channel.send(packt.getDailyString())

if __name__ == "__main__":
    client = MyClient()
    client.run(discordToken)