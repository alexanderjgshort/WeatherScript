from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.oeb.ca/consumer-information-and-protection/electricity-rates').text
soup = BeautifulSoup(html_text, 'lxml')

data = soup.find_all('td')

for i in range(1,4):

    print(data[(i * 4) - 4].text)                          #Peak title
    print(data[(i * 4) - 1].text)                          #Rate (cents/kWh)
    print('Summer:')
    print(data[(i * 4) - 2].text.replace('\t',''))         #Time (Summer)
    print('Winter:')
    print(data[(i * 4) - 3].text.replace('\t',''))         #Time (Winter)
    print()