import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.guestraunt.com/{}'
url = 'https://www.guestraunt.com/arborlakes'

# Eventually rewrite so we're a class/object with an initialize function that sets its attributes
# For now, just make it work
# Also, rewrite to replace 'requests' with 'aiohttp'

def getCalendarImageURL():
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            if('calendar' in image['alt'].lower()):
                return(image['src'])
    else:
        return(None)

def getCalendarImageBIN():
    url = getCalendarImageURL()
    response = requests.get(url)
    if(response.status_code == 200):
        return(response.content)
    else:
        return(None)

def getRestaurants():
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        restaurants = soup.find_all('a')
        uris = []
        for res in restaurants:
            classTags = res.get('class')
            if(type(classTags) is list):
                for c in classTags:
                    if(c == 'sqs-block-button-element--small'):
                        uris.append(res['href'][1:]) # [1:] to strip leading / off
        return(uris)
    else:
        return(None)

def getMenuURL(restaurant):
    response = requests.get(baseurl.format(restaurant))
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            if(image.get('src') is not None):
                if('.gif' in image.get('src').lower()):
                    return(image.get('src'))
        for image in images:
            if('menu' in image.get('alt').lower()):
                return(image.get('src'))
    else:
        return(None)

if __name__ == "__main__":
    print(getMenuURL('ahmos'))