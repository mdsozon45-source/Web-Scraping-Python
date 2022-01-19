#step 1
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
url = "https://codewithharry.com"
# url = "https://phonevalidator.com/"
# url = "https://youtube.com"

#step 1 get the html

r = requests.get(url)
HTMLcontent = r.content
# print(HTMLcontent)

#step 2 parse the html
soup = BeautifulSoup(HTMLcontent, 'html.parser')
# print(soup)
# print(soup.prettify)
# print(soup.prettify)


#step 4 Tree traversal

# Commonly used types of objects
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# title = soup.title
# print(type(soup))
# # print(title)
# print(type(title))
# print(type(title.string))

#get the title of the html page

title = soup.title



#get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

#get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)


#Get frist element in the html page
print(soup.find('p'))
# print(soup.find('p')['class'])

#Get class of any element in the html page
print(soup.find('p')['class'])


#find all the element with class lead
print(soup.find_all('p',class_='lead'))



#get the text from the tages/soup
print(soup.find('p').get_text())
# all_links

#get all the links on the page
# anchors = soup.find_all('a')
all_links = set()
for link in anchors:
	if(link != '#'):
		link = 'https://codewithharry.com'+link.get('href')
		all_links.add(link)
		print(link)
