#!/usr/bin/env python3

from lxml import html
import requests
from configargparse import ArgParser

p = ArgParser()

p.add('url', help='ComicList weekly release URL')

args = p.parse_args()

page = requests.get(args.url)
tree = html.fromstring(page.content)

pubs = tree.xpath('//b/u/text()')
content = tree.xpath('//b/u/text()|//p/a/text()')

for i in range(8,len(content)):
	# if "PUBLISHER" not in content[i] and "Games - " not in content[i] and "Merchandise" not in content[i] and "Cards - " not in content[i]:
	if content[i] not in pubs:
		print(content[i])
	else:
		print("\n", content[i], sep='')