#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stdio_h.py
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
#  STDIO_H
#	
#	Standard Input and Output Library (stdio.h-like). I/O library.
#	
#	Streams handled as pointers to FILE objs.
#	A pointer to a FILE object uniquely identifies a stream, 
#	and is used as a parameter in the operations involving that stream.

#	Standard streams: stdin, stdout and stderr.
	
try:
	ALIAS_H;
except NameError:
	from alias_h import * ;
STDIO_H=TRUE;

import sys,io,os,shutil;
from pprint import pformat;
import urllib.request;

stderr=sys.stderr;
stdin=sys.stdin;
stdout=sys.stdout;
SEP=" ";
LF="\n";
TB=2;
TAB=SEP*TB;

def printR(*args):
	"""
		printR
				Prints out mixed type data, in a general way,
				it seems to be similar to php-print_r.
				
		
		printR("Something",[1,2])
				
				returns
						'Something'
						  1
						  2
		
		print_r(["la casa roja",[1,2],{"a":1,"b":2}],"Upsi")
		
				returns
						'la casa roja'
						  [1, 2]
						  {:a=>1, :b=>2}
						'Upsi'
		
	"""
	global stdout,SEP,LF;
	out="";
	n=0;
	for a in args:
		if(typeOf(a)=="list" or typeOf(a)=="dict"):
			for f in a:
				out+=TAB+pformat(f)+LF;
		else:
			out+=pformat(a)+LF;
	print(out, end='\n', file=stdout, flush=True);
	return(out);

print_r=printR;

"""
File Functions
--------------

Example:
========
fp = fopen('date.txt', 'w')
fprintf(fp,"%04d-%02d-%02d",2002,6,11);
fclose(fp);

"""

def fopen(File,Mode):
	""" 
	File Functions
	==== =========
	
	fopen (Filename,Mode)
					 returns pointer to file
	
	Filename 	Path and filename
	
	MODE
	-----
	r - Read 
	a - Append 
	w - Write 
	x - Create - returns error if the file exist
	t - Text
	b - Binary

		
	Example:
	========
	fp = fopen('date.txt', 'wt')

	"""
	return(open(File, Mode));

def fclose(handle):
	""" 
	File Functions
	==== =========
	
	fclose (FilePointer) 
	
	Example:
	========
	
	fclose(fp);

	"""
	handle.close();

def fprintf(*vargs):
	""" 
	File Functions
	--------------
	
	fprintf (FilePointer, FORMAT [,arg1,arg2,...])
	
	FilePointer
	
	FORMAT
	%d	integer with sign
	%i	integer with sign
	%u	unsigned int
	%o	octal
	%x	hexadecimal lowercase
	%X	hexadecimal uppercase
	%f	floating point
	%lf	double float
	%e 	scientific notation lowercase
	%E 	scientific notation upppercase
	%c 	character
	%s 	string
	
	
	Example:
	========

	fprintf C-Style function 
	
	
	
	"""
	global stdout,stderr;
	args=list(vargs);
	try:
		Arch=args.pop(0);
		assert(isinstance(Arch, io.TextIOBase) or isinstance(Arch, io.BufferedIOBase)), "Wrong file handler";  
		Format=args.pop(0);
		print(Format % tuple(args), file=Arch,end="");
	except:
		xraise("Error on fprintf!");




def printf(*vargs):
	""" 
	File Functions
	--------------
	
	printf (FORMAT [,arg1,arg2,...])
	
	"""
	global stdout,stderr;
	out="";
	args=list(vargs);
	try:
		Format=args.pop(0);
		out=(Format % tuple(args));
	except:
		xraise("Error on printf!");
	
	print(out,sep=' ', end='', file=stdout, flush=False);
	return(out);

def fread(fp,length=null):
	"""
	File Functions
	--------------
	
	buffer = fread(fp,c);
	
	Equivalent in C-language to: fread(buffer, 1, strlen(c), fp);
	
	
	"""
	if(length==null):
		try:
			return(fp.read());
		except:
			return(null);
	else:
		try:
			return(fp.read(length));
		except:
			return(null);


def dirExists(name):
    """
    File Functions
    --------------
    
    dirExists('/tmp')
            returns true if it exists and it is a directory
    """
    if(os.path.exists(name)):
        return(os.path.isdir(name));
    else:
        return(false);


def fileExists(name):
    """
    File Functions
    --------------
    
    fileExists('/tmp')
            returns true if it exists as a file
    """
    if(os.path.exists(name)):
        return(os.path.isfile(name));
    else:
        return(false);

def readlink(name):
    """
    File Functions
    --------------
    readlink('/home/user/tmp.tmp')
    
            returns target name if it has or null
    """ 
    if(os.path.islink(name)):
        tmp=os.readlink(name);
        return(tmp);
    else:
        return(null);
        
def linkExists(name):
    """
    File Functions
    --------------
    
    linkExists('/tmp')
            returns true if it exists and target too
    """
    if(os.path.islink(name)):
        tmp=os.readlink(name);
        return(exists(tmp));
    else:
        return(false);

def exists(name):
    """
    File Functions
    --------------
    
    exists('/tmp')
            returns true if it exists as file/dir/link
    """
    if      (name==null):
            return(false);
            
    elif    (fileExists(name)):
            return(true);
            
    elif    (dirExists(name)):
            return(true);
            
    elif    (os.path.islink(name)):
            return(true);
    else:
            return(false);


def file_get_contents(url,length=null):
	"""
		File Functions
		--------------
		
		file_get_contents('https://www.google.com/index.html')
		or
		file_get_contents('/tmp/myFile.txt')
		
		
		"""
	out=null;
	if(url.startswith("https:") or url.startswith("https:")):
		if(length==null):
			try:
				out=urllib.request.urlopen(url).read();
			except:
				pass;
		else:
			try:
				out=urllib.request.urlopen(url).read(length);
			except:
				pass;
	else:
		if(fileExists(url)):
			try:
				tmp=fopen(url,"r");
				if(length==null):
					out=tmp.read();
				else:
					out=tmp.read(length);
				fclose(tmp);
			except:
				pass;
	return(out);

def	rm (name):
	"""
	File Functions
	--------------
	
	rm('/tmp/myFile.txt')
			if it deletes the file, it will return true
	
	"""
	if(fileExists(name)):
		try:
			os.unlink(name);
			return(true);
		except:
			return(false);
	return(false);


def rmdir(name,force=false):
	"""
	File Functions
	--------------
	
	rmdir('/tmp/dir01')
			if it is an empty directory,
			and it is being removed, it will return true
			
	rmdir('/tmp/dir01',true)
			if it is being removed, empty or not,
			it will return true
	
	"""
	if(dirExists(name)):
		try:
			os.rmdir(name);
			return(true);
		except:
			if(not force):
				return(false);
			else:
				try:
					shutil.rmtree(name,true);
					return(true);
				except:
					pass;
	return(false);

def mkdir(name):
	"""
	File Functions
	--------------
	
	mkdir('tmp')
					makes directory tmp
	"""
	try:
		os.mkdir(name);
		return(true);
	except:
		return(false);

def chdir(name):
	"""
	File Functions
	--------------
	
	chdir('tmp')
					change directory to tmp
	"""
	try:
		os.chdir(name);
		return(true);
	except:
		return(false);

def ls(dirname=".",contains="",startsWith="",endsWith=""):
	"""
	File Functions
	--------------
	
	ls(dirname='tmp')
					returns the ls of directory tmp
	ls(dirname='tmp',contains='a')
					list files/directories in tmp containing a
	ls(dirname='tmp',contains='a',startsWith='n',endsWith='py')
					list files/directories in tmp with all conditions
					
	
	
	"""
	try:
		o=os.listdir(dirname);
	except:
		o=[];
	out=[];
	for f in o:
		add=True;
		if(len(contains)>0 and not(contains in f)):
			add=False;
		if(len(startsWith)>0 and not(f.startswith(startsWith))):
			add=False;
		if(len(contains)>0 and not(f.endswith(endsWith))):
			add=False;
		if(add):
			out.append(f);
	return(out);
		
def touch(name):
	"""
	File Functions
	--------------
	
	touch('file.txt')
	
	"""
	try:
		os.utime(name, None);
		return(True);
	except:
		return(False);


def main(args):
	
	print_r('Something',[1,2]);
	print_r(["la casa roja",[1,2],{"a":1,"b":2}],"Upsi");
	arch=fopen("tmp.tmp","wt");
	for f in xrange(10):
		fprintf(arch,"%03d\n",f);

	fclose(arch);
	
	arch=fopen("tmp.tmp","rt");
	printf("%s",fread(arch));
	fclose(arch);
	printR("file_get_contents('pepe')",file_get_contents("pepe"),"-------");
	printR("file_get_contents('tmp.tmp')",file_get_contents("tmp.tmp"),"-------");
	rm("tmp.tmp");
	printR(ls());
	return(0);

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
