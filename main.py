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
# all_links = set()
# for link in anchors:
# 	if(link != '#'):
# 		link = 'https://codewithharry.com'+link.get('href')
# 		all_links.add(link)
# 		print(link)


#get all the links on the page
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
	if(link.get('href') != '#'):
		linkText = 'https://codewithharry.com'+link.get('href')
		all_links.add(link)
		# print(linkText)



#comments
# markub = '<p><! -- this a comment -- ></p>'
# soup2 = BeautifulSoup(markub)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))



__next = soup.find(id='__next')
# print(__next)
# print(__next.children)
# print(__next.contents)
# for elem in __next.contents:
# 	print(elem)

# for elem in __next.children:
# 	print(elem)




# for item in __next.strings:
# 	print(item)



# for item in __next.stripped_strings:
# 	print(item)


# print(__next.parent)
# print(__next.parents)


# for item in __next.parents:
	# print(item)
	# print(item.name)





# print(__next.next_sibling)
# print(__next.previous_sibling)


elem = soup.select('footer')
print(elem)