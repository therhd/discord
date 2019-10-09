import discord
import config
import packt
import guestrant
import aiohttp
import io

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '!restart': # Should probably check user...
            await client.logout()

        if message.content == '!packtpub':
            await message.channel.send(packt.getDailyString())

        if message.content == '!guestrant':
            async with aiohttp.ClientSession() as session:
                async with session.get(guestrant.getCalendarImageURL()) as resp:
                    if resp.status != 200:
                        return await channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(file=discord.File(data, 'Calendar.gif'))

if __name__ == "__main__":
    client = MyClient()
    client.run(config.discordToken)