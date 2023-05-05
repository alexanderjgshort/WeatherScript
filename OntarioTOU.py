from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.oeb.ca/consumer-information-and-protection/electricity-rates').text
soup = BeautifulSoup(html_text, 'lxml')

data = soup.find_all('td')

for i in range(1,4):

    print(data[(i * 4) - 4].text)                          #TOU Price Periods
    print(data[(i * 4) - 1].text)                          #TOU Prices (cents/kWh)
    print('Summer:')
    print(data[(i * 4) - 2].text.replace('\t',''))         #Times (Summer)
    print('Winter:')
    print(data[(i * 4) - 3].text.replace('\t',''))         #Times (Winter)
    print()
    a = i*4

for j in range(1,5):

    print(data[(j * 3) + a - 3].text)                       #ULO Price Periods
    print(data[(j * 3) + a - 2].text)                       #Times (All Year)
    print(data[(j * 3) + a - 1].text)                       #ULO Prices (cents/kWh)
    print()
