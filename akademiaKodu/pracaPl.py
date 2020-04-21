import requests as r
from bs4 import BeautifulSoup
url = "https://www.pracuj.pl/praca/python;kw/warszawa?rd=0"
page = r.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
print(soup.title.text)
element = soup.find('span', class_='results-header__offer-count-text-number')
print('Python jobs in Warsaw are ', element.text)