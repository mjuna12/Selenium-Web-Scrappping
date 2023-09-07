import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.malkelapagading.com/directory?page='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
result = []

for page in range(1, 21):
    req = requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.findAll('div', 'work-process-sub')
    for i in items:
        name = i.find('h5', 'margin-two text-center').text
        try:
            place = i.find('p', {'class', 'text-uppercase no-margin-bottom'}).text
        except: place = ''
        try:
            floor = i.find('h6', 'no-margin-top margin-two-bottom').text
        except:
            floor = ''
        try:
            image_url = i.find('div', 'position-relative').find('img')['src']
        except:
            image_url= ''
        link_web = i.find('a', {'class': 'highlight-button-dark'})['href']
        print(name,place, floor, image_url, link_web)
        result.append([name, place, floor, image_url, link_web])

column = ['Name', 'Place', 'Floor', 'Image URL', 'Website']
writer = csv.writer(open('results/assignment_1.csv', 'w', newline=''))
writer.writerow(column)
for d in result: writer.writerow(d)

