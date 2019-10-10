import requests
import json
from bs4 import BeautifulSoup

url = 'https://humblebundle.com/'
productURL = 'https://www.humblebundle.com{0}?partner={1}'
partnerCode = 'rhd'

# Eventually rewrite so we're a class/object with an initialize function that sets its attributes
# For now, just make it work
# Also, rewrite to replace 'requests' with 'aiohttp'

def getBundles():
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        webpacks = soup.find_all('script')
        for webpack in webpacks:
            if(webpack.get('id') == 'base-webpack-json-data'):
                baseJson = json.loads(webpack.text)
        return(baseJson.get('navbar').get('productTiles'))
    else:
        return(None)

def getBundlesString():
    bundles = getBundles()
    uriList = []
    for bundle in bundles:
        if('monthly' not in bundle.get('bundle_machine_name')):
            uriList.append(productURL.format(bundle.get('product_url'), partnerCode))
    return('\n'.join(uriList))


if __name__ == "__main__":
    print(getBundlesString())
