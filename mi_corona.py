import requests
from bs4 import BeautifulSoup

url = 'https://www.michigan.gov/coronavirus'

def getStats():
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')
        for table in tables:
            if 'Positive for 2019-nCoV' in str(table):
                data = {}
                for row in table.find_all('tr'):
                    columns = row.find_all('td')
                    gross = '\xa0 '
                    key = str(columns[0].get_text()).replace(gross, '')
                    val = str(columns[1].get_text()).replace(gross, '')
                    data.update( {key:val} )
        return(data)
    else:
        return(None)

def getStatsString():
    data = getStats()
    string = 'Michigan 2019-nCoV (Covid-19)\n'
    for k,v in data.items():
        if k == 'Date' or k == 'Negative for 2019-nCoV' or k == 'Positive for 2019-nCoV':
            k = k.replace('**', '')
            string += '{}: **{}**\n'.format(k,v)
    return string

if __name__ == "__main__":
    print(getStatsString())
