import requests
import json
from bs4 import BeautifulSoup

url = 'https://humblebundle.com/'
productURL = 'https://www.humblebundle.com{0}?partner={1}'
partnerCode = 'rhd' # Move this over to environment variable later

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
            uriList.append(bundle_to_link(bundle))
    return('\n'.join(uriList))

def bundle_to_link(bundle):
    return productURL.format(bundle.get('product_url'), partnerCode)


if __name__ == "__main__":
    print(getBundlesString())
