
#step 1
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
# url = "https://youtube.com"

#step 1 get the html

r = requests.get(url)
HTMLcontent = r.content
# print(HTMLcontent)

#step 2 parse the html
soup = BeautifulSoup(HTMLcontent, 'html.parser')
# print(soup)
print(soup.prettfy)


#step 4 Tree traversal















