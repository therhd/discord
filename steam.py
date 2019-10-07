import config
import requests
import json
import pandas as pd

steamID = '76561198001353738'

def test():

    url = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={0}&steamid={1}&format=json'
    page = requests.get(url.format(config.steamAPIKey, steamID))
    if (page.status_code is 200):
        data = json.loads(page.content)
        df = pd.DataFrame(data['response']['games'])
        print(df.sort_values(by=['playtime_forever'], ascending=False))

        url2 = 'http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={0}&appid={1}'
        for index, game in df.iterrows():
            page = requests.get(url2.format(config.steamAPIKey, game['appid']))
            if (page.status_code is 200):
                data = json.loads(page.content)
                try:
                    print(data['game']['gameName'])
                except:
                    print('noname')

if __name__ == "__main__":
    test()
