import requests
from bs4 import BeautifulSoup

URL = 'https://www.centris.ca/fr/propriete~a-vendre~shefford?view=Thumbnail'

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' }

page = requests.get( URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

descriptionList = soup.find_all("a", "a-more-detail")
#descriptionList = soup.find_all(id="property-result")
firstLink = soup.find("a", "a-more-detail")
print(firstLink)
print(firstLink.find_next(attrs={"class": "price"}))
print(firstLink.find_next(attrs={"itemprop": "price"}).get('content'))

print(len(descriptionList))

#for mls in soup.find_all('a', "a-more-detail"):
#for mls in descriptionList:
#        print(mls.get('data-mlsnumber'))


#print(descriptionList)

#print(soup.prettify())
