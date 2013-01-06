#!/usr/bin/env python

import yapbib.biblist as biblist
import sys

def parse_bibtex(bibtex_file):
	b=biblist.BibList()
	b.import_bibtex(bibtex_file,normalize=False)
	entries = []
	i = 0;
	items = sorted(b.get_items(), key=lambda i: i['year'])
	items.reverse()
	for entry in items:
		entry.html_style["_code"]= None
		html_bibtex = entry.to_html()
		html_bibtex+="\n<div class='bibtex' id='bibtex"+str(i)+"' >\n"
		html_bibtex+= "<pre> "+entry.to_bibtex() +"</pre>"
		html_bibtex+="\n</div>\n"
		entries.append(html_bibtex)
		i+=1
	return entries
	

if __name__ == '__main__':
	print parse_bibtex(sys.argv[1])[0]
	
