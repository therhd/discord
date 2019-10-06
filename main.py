import discord
import config
import packt

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(message)
        
        if message.author == self.user:
            return

        if message.content == '!packtpub':
            await message.channel.send('\n' + packt.getDailyString())

if __name__ == "__main__":
    client = MyClient()
    client.run(config.discordToken)