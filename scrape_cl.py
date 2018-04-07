from lxml import html
import requests
from configargparse import ArgParser
from shlex import quote

p = ArgParser()

p.add('url', help='ComicList weekly release URL')

args = p.parse_args()

page = requests.get(args.url)
tree = html.fromstring(page.content)

pubs = tree.xpath('//b/u/text()')
titles = tree.xpath('//p/a/text()')

for i in pubs:
	if "PUBLISHER" not in i and "Games - " not in i and "Merchandise" not in i and "Cards - " not in i:
		print(i)