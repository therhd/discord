import requests
import json

offersURL = 'https://services.packtpub.com/free-learning-v1/offers?dateFrom=2019-10-06T00:00:00.000Z&dateTo=2019-10-07T00:00:00.000Z'
summaryURL = 'https://static.packt-cdn.com/products/{}/summary'
saleURL = 'https://www.packtpub.com/free-learning'

def getDaily():
    offersReq = requests.get(offersURL)
    offers = json.loads(offersReq.content)
    summary = json.loads(requests.get(summaryURL.format(offers['data'][0]['productId'])).content)
    return({'summary': summary, 'sale': offers['data'][0]})

def getDailyString():
    deal = getDaily()
    return('Today\'s free item is: {0}\n{1}\nExpires at {2}\n{3}'.format(deal['summary']['title'], deal['summary']['oneLiner'], deal['sale']['expiresAt'], saleURL))

if __name__ == "__main__":
    print(getDailyString())