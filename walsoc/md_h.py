#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  md_h.py
#  
#  Copyright 2020 William Martinez Bas <metfar@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from all_h import *;
from pprint import pprint;

#constants
off=OFF=False;
on=ON=True;
TAGS="""
		form, input, label, select, textarea, button,
		fieldset, legend, datalist, output, option, 
		optgroup, h1, h2, h3, h4, h5, h6, 
		p, hr, a, ul, ol, img, div, span,
		table,theader,td,tr,br,script""";
STARTHTML="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html lang="en-CA">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>${title}</title>
        <meta name="Keywords" content="${keywords}" />
		<meta name="description" content="${description}" />
        <meta name="author" content="${author}" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        <link rev="made" href="mailto:${author_email}" />
        <link rel="icon" type="image/x-icon" sizes="48x48" href="favicons/favicon.ico?v=${version}" />
        <link rel="apple-touch-icon" sizes="180x180" href="favicons/apple-touch-icon.png?v=${version}">
        <link rel="icon" type="image/png" sizes="48x48" href="favicons/favicon-48x48.png?v=${version}">
        <link rel="icon" type="image/png" sizes="32x32" href="favicons/favicon-32x32.png?v=${version}">
        <link rel="icon" type="image/png" sizes="16x16" href="favicons/favicon-16x16.png?v=${version}">
        <link rel="shortcut icon" href="favicons/favicon.ico?v=${version}">
        <meta name="msapplication-TileColor" content="#538457">
        <meta name="theme-color" content="#538457">
        <meta name="google-site-verification" content="${site_verification}" />
        <meta name="article:author" content="${article_author}" />
        <meta property="og:image" sizes="300x300" content="imgs/preview.png" />
        <meta property="og:title" content="metfar's password generator" />
        <meta property="og:url" content="${url}" />
        <meta property="og:type" content="utility" />
        <meta property="og:description" content="${description}" />
        <link rel="stylesheet" href="css/reset.css" />
        <link rel="stylesheet" href="css/fonts.css" />
		
    </head>
    <body>
""";
ENDHTML="""
	</body>
</html>

""";
#variables
debug=off;


def DBG():
	global debug;
	try:
		debug;
	except:
		debug=OFF;
	return(debug);

def filt(inString,what="\t\r\n ",which=""):
	tmp=inString;
	n=0;
	for f in what:
		if(len(which)>n):
			tmp=tmp.replace(f,which[n]);
		else:
			tmp=tmp.replace(f,"");
		n+=1;
	return(tmp);



tags=filt(TAGS).split(",");

for f in tags:
	what=(f+'="'+allTrim(f)+'";');
	if(DBG()):
		print(what);
	exec(what);

def startHTML(**vargs):
	global STARTHTML;
	for f in vargs:
		thisTag='${'+str(f)+'}';
		try:
			if(thisTag in STARTHTML):
				STARTHTML=STARTHTML.replace(thisTag,str(vargs[thisTag]));
		except:
			pass;
			
	return(STARTHTML);

def endHTML():
	return(ENDHTML);
	
def onlyTag(*vargs):
	args=list(vargs);
	kind=args.pop(0);
	attributed="";
	for f in args:
		attributed+=f;
	return("<"+kind+" "+attributed+" />");

def startTag(*vargs):
	args=list(vargs);
	kind=args.pop(0);
	attributed="";
	for f in args:
		attributed+=f;
	
	return("<"+kind+" "+attributed+">");

def endTag(kind):
	return("</"+kind+">");
	
def processString(inString,kind="",level=0):
	strong=OFF;
	emphasis=OFF;
	bold=OFF;
	italic=OFF;
	strikethrough=OFF;
	line="";
	if(kind=="li"):
		line+=("\t"*level)+startTag(kind);
	
	#for f in range(len(inString)):
	line+=inString;
	return(inString);

def startsWith(which,where):#where starts with at least one which
	if(type(which)!=type(list())):
		which=list(which);
	out=False;
	for f in which:
		if (where.startswith(f)):
			out=True;
	return(out);

def toList(what):
	out=[];
	for f in what:
		out.append(f);
	return(out);

def toString(what):
	try:
		return("".join(what));
	except:
		return(str(what));
	
def lCharTrim(which,where):
	out=[];
	n=0;
	what=toList(where);
	which=toList(which);
	for f in what:
		if(not (f in which)):
			break;
		else:
			n+=1;
	if(n<len(what)):
		for f in range(n,len(what)):
			out.append(what[f]);
	
	return("".join(out));


def rCharTrim(which,where):
	which=toList(which);
	which.reverse();
	out=lCharTrim(which,where);
	out=toList(out);
	out.reverse();
	return("".join(out));
	
def countStarting(what,charac=" "):
	try:
		return(len(what)-len(lCharTrim(charac,what)));
	except:
		return(0);
		


startHTML(	author="William Martinez Bas",
			title="Markdown Example",
			description="Example",
			keywords="example,all_h,md_h,markdown",
			url="http://metfar.co",
			version=0.1,
			article_author="William Martinez Bas",
			author_email="metfar@gmail.com",
			made="William Martinez Bas <metfar@gmail.com>");
			
def main(args):
	lastLevel=-1;
	level=-1;
	fileName="data/example.md";
	if(not exists(fileName)):
		print(fileName+" does not exist!");
		exit(1);
	
	doc=file_get_contents(fileName);
	doc=doc.split("\n");
	nxt=0;
	lim=len(doc);
	canHR=on;
	print(startHTML());
	for f in doc:
		nxt+=1;
		if 	(canHR and f.startswith("---")):
			print(onlyTag(hr));
		elif(lTrim(f).startswith("#") ):
			st=lTrim(f);
			siz=countStarting(st,"#");
			print(	startTag("h"+str(siz)),
					processString(st[siz:]),
					endTag("h"+str(siz)));
		elif(nxt<lim and filt(doc[nxt]).startswith("==") ):
			st=lTrim(f);
			siz=1;
			print(	startTag("h"+str(siz)),
					processString(st[siz:]),
					endTag("h"+str(siz)));
			canHR=off;
		elif(not canHR and filt(f).startswith("==") ):
			print(onlyTag(br),lCharTrim(" =",f));
			
		elif(startsWith(["+","-","*"],lTrim(f))):
			level=countStarting(f)//2;
			if(lastLevel<level):
				print(("\t"*lastLevel)+"<ul>",end="\t");
			print(processString(lTrim(f)[1:],"li",level));
			canHR=off;
			
		elif(len(filt(f))==0):
			print(onlyTag(br));
			canHR=on;
		else:
			print(f);
			canHR=off;
		
		if(lastLevel>level):
			print(("\t"*level)+"</ul>");
		
		lastLevel=level;
	
	print(endHTML());
	return(0);

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
