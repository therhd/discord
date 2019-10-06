import steam as st
import config

def test():
    steamAPI = st.WebAPI(config.steamAPIKey)
    steamAPI.call('ISteamUser.ResolveVanityURL', vanityurl='valve', url_type=2)
    steamAPI.IsteamUser.ResolveVanityURL(vanityurl='valve', url_type=2)
    steamAPI.ISteamUser.ResolveVanityURL_v1(vanityurl='valve', url_type=2)

if __name__ == "__main__":
    test()