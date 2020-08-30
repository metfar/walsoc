#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  set_h.py
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
for f in "asc,alias,string,enum,math,stdio".split(","):
	exec("from "+f+"_h import *");

SETSEP=",";
SETINIT="{";
SETEND="}";



class Set:
	content=[];
	def __init__(self,*vargs):
		self.content=[];
		out=false;
		for f in vargs:
			if(not (f in self.content)):
				self.content.append(f);
				out=true;
		if(out):
			try:
				self.content.sort();
			except:
				out=[];
				for f in self.content:
					out.append(str(f));
				self.content=out.sort();


	def add(self,*vargs):
		out=false;
		if(type(vargs)==type((1,2))):
			args=list(vargs);
		else:
			args=vargs;
	
		for f in args:
			if(not(f in self.content)):
				self.content.append(f);
				out=true;
		if(out):
			try:
				self.content.sort();
			except:
				out=[];
				for f in self.content:
					out.append(str(f));
				self.content=out;
				self.content.sort();

	
	def includes(self,x):
		return(x in self.content);
		

	
	def getContent(self):
		out=SETINIT;
		flg=false;
		for f in self.content:
			if(flg):
				out+=SETSEP;
			else:
				flg=true;
				
			out+=str(f);
		out+=SETEND;
		return(out);
	
	def to_a(self):
		out=self.content.copy();
		return(out);
	
	def to_s(self):
		return(self.getContent());
	
	def length(self):
		return(len(self.content));
	
	def __str__(self):
		return(self.to_s());
		
	def __len__(self):
		return(self.length());

	def remove(self,x):
		out=self.content.copy();
		if(x in out):
			out.pop(out.index(x));
		elif(str(x) in out):
			out.pop(out.index(str(x)));
		else:
			xraise("KeyError: "+str(x));
		self.content=out.copy();
	
	def discard(self,x):
		if(x in self.content):
			self.remove(x);
			return(true);
		else:
			return(false);
	
	def clear(self):
		try:
			self.content=[];
			return(true);
		except:
			return(false);
	
	def isSubset(self,t):
		out=true;
		for f in self.content:
			if(not t.includes(f)):
				out=false;
				break;
		return(out);
	
	def isSuperset(self,t):
		out=true;
		for f in t.to_a():
			if(not self.includes(f)):
				out=false;
				break;
		return(out);
	
	def copy(self):
		out=Set();
		for f in self.content:
			if(not out.includes(f)):
				out.add(f);
		return(out);
	
	def union(self,t):
		out=self.copy();
		for f in t.to_a():
			if(not (out.includes(f))):
				out.add(f);
		
		return(out);
	
	
	def difference(self,t):
		out=self.copy();
		toTake=t.to_a();
		for f in toTake:
			if(out.includes(f)):
				out.remove(f);
		
		return(out);
	
	def sub(self,t):
		return(self.difference(t));
	
	def intersection(self,t):
		out=Set();
		for f in t.to_a():
			if(self.includes(f)):
				out.add(f);
				
		return(out);
	
	def symmetric_difference(self,t):
		out=self.union(t);
		dif=self.intersection(t);
		for f in dif.to_a():
			out.remove(f);
		
		return(out);
	
	
	def isEmpty(self):
		return(len(self.content)<1);
	
	
	def equals(self,t):
		a=self.intersection(t);
		return(a.length()==t.length() and a.length()==self.length());
	
	def isStrictSubset(self,t):
		return(self.isSubset(t) and (not self.equals(t)));
	
	
	def update(self,t):
		out=self.copy();
		for f in t.to_a():
			if(not out.includes(f)):
				out.add(f);
				
		self.content=out.to_a();
		return(out);
	
	
	def intersection_update(self,t):
		out=Set();
		for f in t.to_a():
			if(self.includes(f)):
				out.add(f);
		
		self.content=out.to_a();
		return(out);
	
	def difference_update(self,t):
		o=self.difference(t);
		self.content=o.to_a();
		return(self.content);
	
	def symmetric_difference_update(self,t):
		o=self.symmetric_difference(t);
		self.content=o.to_a();
		return(self.content);
	
	def pop(self):
		if(self.length()<1):
			print("KeyError: ",end="");
			return(null);
		else:
			o=self.content[-1];
			self.discard(o);
			return(o);

def set(*vargs):
	out=Set();
	for f in vargs:
		out.add(f);
	return(out);

def main(*argv):
	echo(APP+LOADED);
	echo (is_defined("APP"));
	a=set(1,2,13,5,2,7,"casa");
	echo(typeOf(a));
	echo(len(a));
	echo(a);
	a.remove(2);
	echo(a);
	a.add("la");
	a.add("Casa","roja");
	echo(a.getContent());
	b=set();
	echo(b);
	echo("A:");
	echo(a);
	b=set("la","casa");
	echo("B:");
	echo(b);
	
	echo("A = A?");
	echo(a.equals(a));
	echo("B ⊂ A?");
	echo (b.isStrictSubset(a) );
	echo("A ⊆ B?");
	echo(a.isSubset(b));
	echo("A is superset of B?");
	echo(a.isSuperset(b));
	echo("B is superset of A?");
	echo(b.isSuperset(a));
	echo("A U B?");
	echo(a.union(b));
	echo("A ∩ B?");
	echo(a.intersection(b));
	echo("A - B?");
	echo(a.difference(b));
	echo("{}=∅ ?");
	echo(set().isEmpty());
	c=set(1,2);
	d=set(2,3,4);
	c.update(d);
	echo(c);
	c.intersection_update(d);
	echo(c);
	c.difference_update(set(2,4));
	echo(c);
	echo(c.pop());
	echo(c.pop());
	echo(typeOf(set()));
	return(0);
	
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
