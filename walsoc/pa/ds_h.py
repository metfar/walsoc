#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
#  ds_h.py
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
#  DataStore implementation: Simple file format INI or json.gz


	
try:
	ALIAS_H;
except NameError:
	from alias_h import * ;

try:
	STDIO_H;
except NameError:
	from stdio_h import *;

try:
	STRING_H;
except NameError:
	from string_h import *;

DS_H=TRUE;

INI="ini";
default="default";
defaultFilename="data.ini";
null=None;
br="\n";

import json;
import gzip;


def toserial(inp):
	return(json.dumps(inp,sort_keys=True));

def fromserial(inp):
	return(json.loads(inp));

def gzencode(inp,level=9):
	return(gzip.compress(str(inp).encode(),compresslevel=(level % 10)));

def gzdecode(inp):
	return(gzip.decompress(inp).decode());

def encode(inp):
	return(gzencode(toserial(inp)));

def decode(inp):
	return(fromserial(gzdecode(inp)));

def noencode(inp):
	return(inp);



class dataStore():
	
	def __init__(self,**args):
		self._voidSection={};
		self._voidStruct={default:self._voidSection};
		self._section=default;
		self._key=default;
		self._data=self._voidStruct;
		self._filename=defaultFilename;
		if("filename" in args):
			self._filename=args["filename"];
		if("data" in args):
			data=args["data"];
			for sect in data:
				self._data[toLower(sect)]=self._voidSection;
				for key in data[sect]:
					self._data[toLower(str(sect))][toLower(str(key))]=data[sect][key];
			
	def getData(self):
		return(self._data);
		
	def getSection(self,sect=null):
		if (sect==null):
			return(self._section);
		else:
			sect=toLower(str(sect));
			if(sect in self._data):
				return(self._data[sect]);
			else:
				raise(ValueError("Section %s not found!" % (sect)));
	
	def setSection(sect=default,select=True):
		try:
			sect=toLower(str(sect));
		except:
			sect=default;
		if(not(sect in self._data)):
			self._data[sect]=self._voidSection;
		self._section=sect;


	def filename(self,name=null):
		if(name==null):
			return(self._filename);
		else:
			self._filename=str(name);
		
	
	def set(self,value,key=null,section=null,onlyIfExists=False):
		if(section==null):
			section=self._section;
		else:
			self._section=section;
		
		if(key==null):
			key=self._key;
		else:
			self._key=str(key);
		
		if(not onlyIfExists):
			self.setSection(section);
		else:
			if(not(section in self._data)):
				return(False);
		self._data[self._section][self._key]=value;
		return(True);
	
	def setKey(self,key,section=null,onlyIfExists=False):
		if(section==null):
			section=self._section;
		else:
			self._section=section;
		
		if(not onlyIfExists):
			self.setSection(section);
		else:
			if(not(section in self._data)):
				return(False);
		self._data[self._section][self._key]=null;
		return(True);
	
	
	def get(self,key=null,section=null):
		if(section==null):
			section=self._section;
		else:
			self._section=section;
		
		if(key==null):
			key=self._key;
		else:
			self._key=str(key);
		
		if((not (section in self._data)) or (not(key in self._data[section]))):
			raise (ValueError("Value not found in section %s key %s!"%(str(section),str(key))));
		else:
			return(self._data[self._section][self._key]);
		
	
	def load(self,filename=null):
		#Filetypes supported INI, JSON, JSON.gz
		if not(filename==null):
			self.filename(str(filename));
		
		if(not fileExists(self.filename())):
			raise(IOError("File %s not found!" % (self.filename())));
		
		self._data=self._voidStruct;
		
		exts=self.filename().split(".");
		ext=toLower(exts[-1]);
		
		if (ext==INI):
			data = open(self.filename(),"rt").readlines();
			config=self._voidStruct;
			for f in data:
				tmp=f.strip();
				if (len(tmp)>0 and not (left(tmp,1) in ["#",'"""',"//",";"])):
					if (left(tmp,1)=="[" and "]" in tmp):
						section=toLower(substr(tmp,1,instr(tmp,"]")-1));
						if(not (section in config)):
							config[section]={};
					else:
						if("=" in tmp):
							label=str_replace(" ","_",left(tmp,instr(tmp,"=")));
						rightSide=substr(tmp,instr(tmp,"=")+1);
						
						j=is_In(["#",'"""',"//",";"],rightSide);
						
						if(j>=0):
							tmp=left(rightSide,j);
							
						if(label in config[section]):
							if ("=" in tmp and not ('"' in config[section][label])):
								config[section][label]=rightSide;
							else:
								if ('"' in config[section][label]):
									config[section][label]+="\n"+tmp;
									if ((config[section][label].count('"') % 2)==0):
										label="#";
						else:
							config[section][label]=rightSide;
			self._data=config;
		else:
			if(ext=="gz"):
				decompress=gzdecode;
				if(len(exts)>2):
					ext=exts[-2];
			else:
				decompress=noencode;
			data=open(self.filename(),"rb").read();
			self._data=fromserial(decompress(data));
			data="";
		
		self.review();
		return(self);#._data);

	def save (self,filename=null):
		#Filetypes supported INI, JSON, JSON.gz
		if (filename!=null):
			self.filename(str(filename));
		
		exts=self.filename().split(".");
		ext=toLower(exts[-1]);
		self.review();
		
		if (ext==INI):
			data = open(self.filename(),"wt");
			for sect in self._data:
				data.write("["+toLower(sect)+"]");
				for key in self._data[sect]:
					data.write(str_replace(" ","_",key)+"="+toserial(self._data[sect][key]));
		else:
			data = open(self.filename(),"wb");
			if(toLower(ext)=="gz"):
				compress=gzencode;
				#if(len(exts)>2):
				#	ext=exts[-2];
			else:
				compress=noencode;
			
			data.write(compress(toserial(self._data)));
		data.close();
	
	def review(self,which='"([{«<`',to='")]}»>`'):
		""" func review
		
		Close parentheses, brackets, braces, and quotes
		
		"""
		which=[f for f in which];
		to=[f for f in to];
		if(len(which)!=len(to)):
			m=min(len(which),len(to));
			which=which[:m];
			to=to[:m];
		
		for f in which:
			for sect in self._data:
				for key in self._data[sect]:
					inp=toLower(str(self._data[sect][key]));
					tmp=which.index(f);
					c=to[tmp];
					if( ((inp.count(f)+inp.count(c))%2)==1):
						try:
							self._data[sect][key]+=c;
							#print(to[tmp]);
						except:
							pass;
		
	def __repr__(self):
		name=self.filename();
		out=name+br+("="*len(name))+br;
		for sect in self._data:
			out+="["+toLower(sect)+"]"+br;
			for key in self._data[sect]:
				out+=str_replace(" ","_",str(key));
				out+="=";
				out+=str(self._data[sect][key]);
				out+=br;
		return(out);


def main(*argv):
	startName="one.sections.gz";
	print("Creating %s"%startName);
	p=dataStore(filename=startName,data={"default":{1:1,2:"{[(«pepe"}});
	p.save();
	print("Loading its data");
	p.load();
	print("Show its content");
	print(p);
	
	p.filename("two.sections.gz");
	print("Saving to",p.filename());
	p.save();
	print("Removing",p.filename());
	os.remove("two.sections.gz");
	

if __name__ == '__main__':
	import os;
	main();
