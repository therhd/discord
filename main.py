import discord
import packt
import os
import aiohttp
import guestrant
import io
import humble
import datetime
import asyncio
import giphy_client
import random
import mi_corona

discordToken = os.environ.get('discordToken')
giphyToken = os.environ.get('giphyToken')

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

        if message.content == '!corona':
            await message.channel.send(mi_corona.getStatsString())

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
    phrases = [{'text': 'Water drink', 'language': 'afrikaans'}, {'text': 'Pini ujë', 'language': 'albanian'}, {'text': 'ውሃ ጠጣ', 'language': 'amharic'}, {'text': 'اشرب ماء', 'language': 'arabic'}, {'text': 'Ջուր խմել', 'language': 'armenian'}, {'text': 'içki su', 'language': 'azerbaijani'}, {'text': 'Edan ura', 'language': 'basque'}, {'text': 'Піць ваду', 'language': 'belarusian'}, {'text': 'জলপান করা', 'language': 'bengali'}, {'text': 'Pijte vodu', 'language': 'bosnian'}, {'text': 'Пия вода', 'language': 'bulgarian'}, {'text': 'Beure aigua', 'language': 'catalan'}, {'text': 'Inom ug tubig', 'language': 'cebuano'}, {'text': 'Kumwa madzi', 'language': 'chichewa'}, {'text': '喝水', 'language': 'chinese (simplified)'}, {'text': '喝水', 'language': 'chinese (traditional)'}, {'text': 'acqua dolce', 'language': 'corsican'}, {'text': 'Piti vodu', 'language': 'croatian'}, {'text': 'Pít vodu', 'language': 'czech'}, {'text': 'Drik vand', 'language': 'danish'}, {'text': 'Drink water', 'language': 'dutch'}, {'text': 'Drink water', 'language': 'english'}, {'text': 'Trinki akvon', 'language': 'esperanto'}, {'text': 'Juua vett', 'language': 'estonian'}, {'text': 'Uminom ng tubig', 'language': 'filipino'}, {'text': 'Juoda vettä', 'language': 'finnish'}, {'text': 'Eau potable', 'language': 'french'}, {'text': 'Drinkwetter', 'language': 'frisian'}, {'text': 'beber auga', 'language': 'galician'}, {'text': 'სასმელი წყალი', 'language': 'georgian'}, {'text': 'Wasser trinken', 'language': 'german'}, {'text': 'Πίνουν νερό', 'language': 'greek'}, {'text': 'પાણી પીઓ', 'language': 'gujarati'}, {'text': 'Bwè dlo', 'language': 'haitian creole'}, {'text': 'sha ruwa', 'language': 'hausa'}, {'text': 'E inu i ka wai', 'language': 'hawaiian'}, {'text': 'לשתות מים', 'language': 'hebrew'}, {'text': 'पानी प', 'language': 'hindi'}, {'text': 'Haus dej dej', 'language': 'hmong'}, {'text': 'Vizet inni', 'language': 'hungarian'}, {'text': 'Drekka vatn', 'language': 'icelandic'}, {'text': 'ọṅụṅụ mmiri', 'language': 'igbo'}, {'text': 'Minum air', 'language': 'indonesian'}, {'text': 'uisce Dí', 'language': 'irish'}, {'text': 'Bere acqua', 'language': 'italian'}, {'text': '水を飲む', 'language': 'japanese'}, {'text': 'banyu ngombe', 'language': 'javanese'}, {'text': 'ನೀರು ಕುಡಿ', 'language': 'kannada'}, {'text': 'Су ішу', 'language': 'kazakh'}, {'text': 'ផឹកទឹក', 'language': 'khmer'}, {'text': '음료 물', 'language': 'korean'}, {'text': 'Avê vexwe', 'language': 'kurdish (kurmanji)'}, {'text': 'Суу ичүү', 'language': 'kyrgyz'}, {'text': 'ນ້ໍາດື່ມ', 'language': 'lao'}, {'text': 'Et aquam non bibens', 'language': 'latin'}, {'text': 'Dzert ūdeni', 'language': 'latvian'}, {'text': 'Gerk vandenį', 'language': 'lithuanian'}, {'text': 'drénken Waasser', 'language': 'luxembourgish'}, {'text': 'Пијте вода', 'language': 'macedonian'}, {'text': 'Misotroa rano', 'language': 'malagasy'}, {'text': 'Minum air', 'language': 'malay'}, {'text': 'വെള്ളം കുടിക്കു', 'language': 'malayalam'}, {'text': 'ilma Ixrob', 'language': 'maltese'}, {'text': 'inu wai', 'language': 'maori'}, {'text': 'पाणी पि', 'language': 'marathi'}, {'text': 'Ус уух', 'language': 'mongolian'}, {'text': 'သောက်စရာရေ', 'language': 'myanmar (burmese)'}, {'text': 'पानी पिउ', 'language': 'nepali'}, {'text': 'drikk vann', 'language': 'norwegian'}, {'text': 'د څښلو اوبه', 'language': 'pashto'}, {'text': 'آب نوشیدنی', 'language': 'persian'}, {'text': 'Pij wodę', 'language': 'polish'}, {'text': 'Beber água', 'language': 'portuguese'}, {'text': 'ਪੀਣ ਦਾ ਪਾਣੀ', 'language': 'punjabi'}, {'text': 'Bea apă', 'language': 'romanian'}, {'text': 'Пить воду', 'language': 'russian'}, {'text': 'vai inu', 'language': 'samoan'}, {'text': 'deoch uisge', 'language': 'scots gaelic'}, {'text': 'Пити воду', 'language': 'serbian'}, {'text': 'seno metsi', 'language': 'sesotho'}, {'text': 'Drink mvura', 'language': 'shona'}, {'text': 'پاڻي پيء', 'language': 'sindhi'}, {'text': 'ජලය පානය කරන්න', 'language': 'sinhala'}, {'text': 'Piť vodu', 'language': 'slovak'}, {'text': 'Piti vodo', 'language': 'slovenian'}, {'text': 'Cab biyo', 'language': 'somali'}, {'text': 'Beber agua', 'language': 'spanish'}, {'text': 'cai inuman', 'language': 'sundanese'}, {'text': 'Kunywa maji', 'language': 'swahili'}, {'text': 'Drick vatten', 'language': 'swedish'}, {'text': 'об бинӯшед', 'language': 'tajik'}, {'text': 'தண்ணீர் குடி', 'language': 'tamil'}, {'text': 'పానీయం నీటి', 'language': 'telugu'}, {'text': 'ดื่มน้ำ', 'language': 'thai'}, {'text': 'Su iç', 'language': 'turkish'}, {'text': 'Пити воду', 'language': 'ukrainian'}, {'text': 'پانی پیو', 'language': 'urdu'}, {'text': 'Ichkilik suv', 'language': 'uzbek'}, {'text': 'Uống nước', 'language': 'vietnamese'}, {'text': 'dŵr yfed', 'language': 'welsh'}, {'text': 'sela', 'language': 'xhosa'}, {'text': 'טרונק וואסער', 'language': 'yiddish'}, {'text': 'mimu omi', 'language': 'yoruba'}, {'text': 'Phuza amanzi', 'language': 'zulu'}, {'text': 'Uminom ng tubig', 'language': 'Filipino'}, {'text': 'לשתות מים', 'language': 'Hebrew'}]
    trigger_times = [9, 12, 14, 16]
    # Rotate trigger_times for first run
    await client.wait_until_ready()
    while not client.is_closed():
        # Wrap this into a function next time you re-use it.
        now = datetime.datetime.now()
        next_t = None
        for time in trigger_times:
            if time > now.hour:
                next_t = datetime.datetime(year=now.year, month=now.month, 
                                day=now.day, hour=time, minute=0, second=0)
                break
        if next_t == None:
            tomorrow = datetime.timedelta(1) + now
            next_t = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=trigger_times[0], minute=0, second=0)
        sleep_time = (next_t - now).seconds + 20
        await asyncio.sleep(sleep_time)
        if datetime.datetime.now().weekday() < 5:
            g_api = giphy_client.DefaultApi()
            response = g_api.gifs_search_get(giphyToken, 'water', limit=50, rating='g')
            gif = random.choices(response.data)
            channel = client.get_channel(643828501035876363)
            phrase = random.choice(phrases)
            await channel.send('{} ({})\n{}'.format(phrase.get('text'), phrase.get('language'), gif[0].url))

async def packt_check():
    await client.wait_until_ready()
    old_deal = packt.getDailyString() # Check it immediately, since I restart the bot for code changes often. 
    while not client.is_closed():
        curr_deal = packt.getDailyString()
        if old_deal != curr_deal:
            old_deal = curr_deal
            channels = [client.get_channel(632020894604328970), client.get_channel(630078078349213707)]
            for channel in channels:
                await channel.send(curr_deal)
        await asyncio.sleep(60*60)

async def humble_check():
    await client.wait_until_ready()
    known_bundles = humble.getBundles() # Check it immediately, since I restart the bot for code changes often. 
    while not client.is_closed():
        for bundle in humble.getBundles():
            if bundle not in known_bundles:
                known_bundles.append(bundle)
                channels = [client.get_channel(632020894604328970), client.get_channel(630078078349213707)]
                for channel in channels:
                    await channel.send(humble.bundle_to_link(bundle))
        await asyncio.sleep(60*60)

async def corona_check():
    await client.wait_until_ready()
    known_stats = mi_corona.getStatsString()
    while not client.is_closed():
        curr_stats = mi_corona.getStatsString()
        if known_stats != curr_stats:
            known_stats = curr_stats
            channels = [client.get_channel(632020894604328970), client.get_channel(630078078349213707), client.get_channel(687819067985625197)]
            for channel in channels:
                await channel.send(curr_stats)
        await asyncio.sleep(60*60)

if __name__ == "__main__":
    client = MyClient()
    water_task = client.loop.create_task(water())
    packt_task = client.loop.create_task(packt_check())
    corona_task = client.loop.create_task(corona_check())
    # humble_task = client.loop.create_task(humble_check())
    client.run(discordToken)