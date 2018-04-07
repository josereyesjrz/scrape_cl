from lxml import html
import requests

page = requests.get('http://www.comiclist.com/index.php/lists/comiclist-new-comic-book-releases-list-for-12-20-2017')
tree = html.fromstring(page.content)

pubs = tree.xpath('//b/u/text()')
titles = tree.xpath('//p/a/text()')

for i in pubs:
	if "PUBLISHER" not in i and "Games - " not in i and "Merchandise" not in i:
		print(i)