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
if __name__ == "__main__":
    test()
