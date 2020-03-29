import requests
from bs4 import BeautifulSoup

# url = 'https://www.michigan.gov/coronavirus'
# url = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163-520743--,00.html'
url = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'
def getStats():
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')
        for table in tables:
            if 'Confirmed COVID-19 Cases by County' in str(table):
                data = {}
                for row in table.find_all('tr'):
                    if 'Confirmed COVID-19 Cases by County' not in str(row):
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
    string = 'Michigan 2019-nCoV (Covid-19)\nMore details at {}\n'.format(url)
    for k,v in data.items():
        if k != 'Total' and k != 'County':
            k = k.replace('**', '')
            string += '{}: **{}**, '.format(k,v)
    string = string.rstrip(', ') + '\nTotal: **{}**'.format(data.get('Total'))
    return string

if __name__ == "__main__":
    # print(getStats())
    print(getStatsString())
