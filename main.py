import discord
import packt
import os
import aiohttp
import guestrant
import io
import humble
import datetime
import asyncio
import time

discordToken = os.environ.get('discordToken')

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
        
        if message.content == '!humble':
            await message.channel.send(humble.getBundlesString())

        if message.content == '!guestrant':
            async with aiohttp.ClientSession() as session:
                async with session.get(guestrant.getCalendarImageURL()) as resp:
                    if resp.status != 200:
                        return await channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    restaurants = guestrant.getRestaurants()
                    await message.channel.send('!guestrant menu [restaurant]\nChoose from list: {}'.format(str(restaurants)[1:-1].replace("'", "")), file=discord.File(data, 'Calendar.gif'))
        
        if message.content == '!guestrant menu':
            restaurants = guestrant.getRestaurants()
            await message.channel.send('!guestrant menu [restaurant]\nChoose from list: {}'.format(str(restaurants)[1:-1].replace("'", "")))

        if len(message.content.split(' ')) == 3 and message.content.split(' ')[0] == '!guestrant' and message.content.split(' ')[1] == 'menu':
            arg = message.content.split(' ')[2]
            restaurants = guestrant.getRestaurants()
            if arg in restaurants:
                            async with aiohttp.ClientSession() as session:
                                async with session.get(guestrant.getMenuURL(arg)) as resp:
                                    if resp.status != 200:
                                        return await channel.send('Could not download file...')
                                    data = io.BytesIO(await resp.read())
                                    restaurants = guestrant.getRestaurants()
                                    await message.channel.send(file=discord.File(data, '{}-Menu.gif'.format(arg)))
            else:
                await message.channel.send('Whoops, **{0}** was not in my list. Try again. Valid restaurants: {1}'.format(arg, str(restaurants)[1:-1].replace("'", "")))


async def water():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(643828501035876363)
        now = datetime.datetime.now()
        if now.hour > 6 and now.hour < 18:
            await channel.send('DRINK WATER')
        await asyncio.sleep(2*60*60)



if __name__ == "__main__":
    client = MyClient()
    water_task = client.loop.create_task(water())
    client.run(discordToken)