#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
#  enum_h.py
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

class Enum():
	def __init__(self,*Names):
		names=[];
		for f in Names:
			names.append(f);
		#if(type(names)!=type([])):
		if(len(names)<1):
			self.__names__=[
				"STARTING",
				"RUNNING",
				"PROCESSING",
				"CHECKING",
				"FINISHING",
				"TERMINATED"
				];
		else:
			self.__names__=names;
		_n_=0;
		for u in self.__names__:
			f=str(u);
			exec("self.v"+f+"="+str(_n_)+";");
			try:
				exec("self."+f+"="+str(_n_)+";");
			except:
				pass;
			_n_+=1;
		self.__sta__=0;
		self.__nst__=len(self.__names__);
		for f in range(0,len(self.__names__)):
			exec("""def get_"""+self.__names__[f]+"""(self):
					return(self.v"""+self.__names__[f]+");");
			exec("""def set_"""+self.__names__[f]+"""(self,x):
				try:
					self.v"""+self.__names__[f]+"""=x;
				except:
					pass;
				""");
			exec(self.__names__[f]+"= property(get_"+self.__names__[f]+",set_"+self.__names__[f]+");");
		
	
	
	def __name__(self):
		return(self.__names__[self.__sta__]);
	def  name (self,index):
		try:
			return(self.__names__[index]);
		except:
			return(null);
	
	def __repr__(self):
		return(str(self.__name__()));
	
	def __next__(self):
		if(self.__sta__+1 >=self.__nst__):
			raise (StopIteration);
		else:
			self.__sta__+=1;
		return(self.__name__());
	def __prev__(self):
		if(self.__sta__-1 < 0):
			raise (StopIteration);
		self.__sta__-=1;
		return(self.__name__());
	
	def  rnext(self):
		if(self.__sta__+1 >=self.__nst__):
			self.__sta__= 0;
		else:
			self.__sta__+=1;
		return(self.__name__());
	def  rprev(self):
		if(self.__sta__-1 < 0):
			self.__sta__=self.__nst__;
		self.__sta__-=1;
		return(self.__name__());
	next=__next__;
	prev=__prev__;
	def __iter__(self):
		return (iter(self.__names__));


	def __add__(self,num=1):
		mi=0 if num>0 else num;
		ma=0 if num<0 else num;
		for f in range(mi,ma):
			self.rnext();
		return(self.__repr__());
	
	def __sub__(self,num=1):
		mi=0 if num>0 else num;
		ma=0 if num<0 else num;
		for f in range(mi,ma):
			self.rprev();
		return(self.__repr__());

	def __getitem__(self, index):
		try:
			self.__names__[index];
			return(index);
		except:
			raise(IndexError);

def main(*argv):
	STATUS=Enum("STARTING","RUNNING","FINISHED");
	assert( Enum()[1]==Enum().RUNNING);
	print(STATUS.name(0));
	
	next(STATUS);
	print(STATUS);
	print(STATUS);
	for f in Enum():
		print(f);

	f=Enum();
	print("----------");
	print("Manually");
	print("----------");
	print(f);
	f+=4;
	print(f);
	print("----------");
	f=Enum();
	while(True):
		print(f);
		try:
			f.next();
		except StopIteration:
			break;
	print(f.STARTING);




if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
