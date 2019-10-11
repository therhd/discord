import requests
import json
import datetime

offersURL = 'https://services.packtpub.com/free-learning-v1/offers?dateFrom={0}T00:00:00.000Z&dateTo={1}T00:00:00.000Z'
summaryURL = 'https://static.packt-cdn.com/products/{}/summary'
saleURL = 'https://www.packtpub.com/free-learning'

def getDaily(date = datetime.datetime.now(datetime.timezone.utc)):
    end = date + datetime.timedelta(hours=24)
    URL = offersURL.format(date.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))

    offersReq = requests.get(URL)
    offers = json.loads(offersReq.content)
    try:
        summary = json.loads(requests.get(summaryURL.format(offers['data'][0]['productId'])).content)
        return({'summary': summary, 'sale': offers['data'][0]})
    except:
        return(False)

def getDailyString():
    deal = getDaily()
    if (deal is not False):
        return('Today\'s free item is: {0}\n{1}\nExpires at {2}\n{3}'.format(deal['summary']['title'], deal['summary']['oneLiner'], deal['sale']['expiresAt'], saleURL))
    else:
        return('Was not able to check')

def getFuture(days = 7):
    for i in range(1, days + 1):
        date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=(i * 24))
        end = date + datetime.timedelta(hours=24)
        deal = getDaily(date)
        if (deal is not False):
            print('{0} T00:00Z - {1} T00:00Z: {2}'.format(date.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), deal['summary']['title']))

if __name__ == "__main__":
    print(getDailyString())
    getFuture(7)