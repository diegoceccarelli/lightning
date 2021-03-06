#!/usr/bin/env python

import sys
import codecs
import os
import subprocess
from jinja2 import nodes
from jinja2.ext import Extension
from jinja2 import Environment, Undefined
import HTMLParser
from unidecode import unidecode
import bibtex2html
import re

_htmlparser = HTMLParser.HTMLParser()
unescape = _htmlparser.unescape


if __name__ == "__main__":
	input_file = sys.argv[1]
	f = open(input_file)
	output = subprocess.check_output(["dokuwiki/bin/render.php"],stdin=f)
	output_file=input_file+".html"
	o = open(output_file,"w")
	o.write(output);
	o.close()

def convert(text):
	global unescape
	o = open("/tmp/doku","w")
	text = unidecode(text)

	o.write(text)
	o.close()
	
	o = open("/tmp/doku","r")
	output = subprocess.check_output(["dokuwiki/bin/render.php"],stdin=o)
	output = re.sub('/dokuwiki/bin/lib/exe/detail.php?[^>]*media=(?P<file>[^">]+)', '/static/img/\g<file>', output)
	output = re.sub('/dokuwiki/bin/lib/exe/fetch.php?[^>]*media=(?P<file>[^">]+)', '/static/img/\g<file>', output)
	output = unidecode(output)
	output = add_bibtex(output)
	return output
	

def add_bibtex(content):
	bibtex=re.findall( r'@biblio[{]([^}]+)[}]',content)
	for b in bibtex:
		f = open("biblio/"+b)
		entries = bibtex2html.parse_bibtex("biblio/"+b)
		html = "<ol>\n"
		for e in entries:
			html+="<li>"+e+"</li>"
		html += "</ol>\n"
		text = "<div class='biblio' id='"+b+"'>\n"+html+"\n</div>"
		content = content.replace("@biblio{"+b+"}",text)
		print "readed ",len(entries), "bibtex entries"
	return content 


def doku(text):
	o = open("log","w")
	o.write(text)
	o.close()
	return convert(text)

class DokuwikiExtension(Extension):
	def __init__(self, environment):
		super(DokuwikiExtension, self).__init__(environment)
		environment.filters["doku"] = doku	
		