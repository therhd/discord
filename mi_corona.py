import requests
from bs4 import BeautifulSoup

url = 'https://www.michigan.gov/coronavirus'

def getStats():
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')
        for table in tables:
            if 'Daily Confirmed COVID-19 Cases by County' in str(table):
                data = {}
                for row in table.find_all('tr'):
                    print(str(row))
                    if 'Daily Confirmed COVID-19 Cases by County' not in str(row):
                        columns = row.find_all('td')
                        if len(columns) > 0:
                            gross = '\xa0 '
                            key = str(columns[0].get_text()).replace(gross, '')
                            val = str(columns[1].get_text()).replace(gross, '')
                            key = key.replace('\n', '')
                            val = val.replace('\n', '')
                            data.update( {key:val} )
        return(data)
    else:
        return(None)

def getStatsString():
    data = getStats()
    string = 'Michigan 2019-nCoV (Covid-19)\n'
    for k,v in data.items():
        if k != 'Total' and k != 'County':
            k = k.replace('**', '')
            string += '{}: **{}**, '.format(k,v)
    string = string.rstrip(', ') + '\nTotal: **{}**'.format(data.get('Total'))
    return string

if __name__ == "__main__":
    # print(getStats())
    print(getStatsString())
