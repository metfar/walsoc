#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  colio_h.py
#  
#  Copyright 2020 wmartinez <metfar@gmail.com>
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

null=NULL=Null=None;
dbg=False;

ESC=chr(0x1b);
from string_h import *;
import pickle;
from glob import glob;


_SPACE=" ";

def rep(n,charact=null):
	out="";
	if(charact==null):
		charact=_SPACE;
	try:
		out=charact * n;
	except:
		pass;
	return(out);

def spc(n=1):
	return(rep(n));
	




def locate(y,x):
	print(ESC+"["+str(y+1)+";"+str(x+1)+"H",end="");

def gotoxy(x,y):
	locate(y,x);

def clrscr():
        print(ESC+"[2J",end="");
        locate(0,0);


def _defineColours():
	global PALETTE,COLNAMES,COLOURS;
	COLOURS={};
	PALETTE=[ 
						0,# — black 	
						1,# — maroon
						2,# — green 	
						3,# — olive 	
						4,# — navy 	
						5,# — purple 	
						6,# — teal 	
						7,# — silver 	
						8,# — gray
						9,# — red
						10,# — lime
						11,# — yellow
						12,# — blue
						13,# — fuchsia
						14,# — aqua
						15# — white 
					];
	COLNAMES=[	
						"black",
						"maroon", 
						"green", 
						"olive", 
						"navy", 
						"purple", 
						"teal", 
						"silver", 
						"gray", 
						"red", 
						"lime", 
						"yellow", 
						"blue", 
						"fuchsia", 
						"aqua", 
						"white"
						];
	for f in range(0,len(PALETTE)):
		COLOURS[COLNAMES[f]]=PALETTE[f];
	
	return(COLOURS);


_defineColours();
def ink(i=null):
	global INK;
	if(i==null):
		return(INK);
	
	try:
		INK;
	except:
		INK=0;
	if(type(i)==type(0)):
		INK=i;
	else:
		if(type(i)==type("home")):
			if(i.lower() in COLNAMES):
				INK=COLNAMES.index(i);
	if(INK>7):
		i=INK-8;
		UF=";1";
	else:
		i=INK;
		UF=";22";
	print(ESC+"[3"+str(i)+UF+"m",end="");
	return(INK);
	
def paper(p=null):
	global PAPER;
	if(p==null):
		return(PAPER);
	
	try:
		PAPER;
	except:
		PAPER=7;
	
	if(type(p)==type(0)):
		PAPER=p;
	else:
		if(type(p)==type("home")):
			if(p.lower() in COLNAMES):
				PAPER=COLNAMES.index(p);
	if(PAPER>7):
		i=PAPER-8;
		UF="";
	else:
		i=PAPER;
		UF=";1";
	
	print(ESC+"[4"+str(i)+"m",end="");
	return(PAPER);
	

def color(i=0,p=7):
	ink(i);
	paper(p);
	#print(ESC+"[4"+str(p)+";3"+str(i)+"m",end="");


if(dbg):
	import pygame;
	from pygame.locals import *;
	from pprint import pprint;
	pygame.init();
	ran=160;
	width,height=pygame.display.Info().current_w-ran,pygame.display.Info().current_h-ran;
	screen = pygame.display.set_mode((width,height));





from kb_h import *;

def getkey():
	key="";
	while key=="":
			key=inkey();
	return(key);

def main(args):
	grilla=[10,10];#x,y
	grid={};
	row=rep(grilla[0]);#gr_sz);
	def ch(txt=" "):
		return(" " if txt==_SPACE else "X");

	for f in range(grilla[1]):
		grid[f]=row;

	x,y=0,0;
	goOut=False;
	key="";
	sx,sy=2,2;
	while(not goOut):
		color(7,0);
		clrscr();

		for f in range(len(grid)):
			for n in range(len(grid[f])):
				#color(7,0);
				#gotoxy(f*2+sy,n*2+sx);
				#print("+-+",end="");
				c=ch(grid[f][n]);
				if(c=="X"):
					color(3,3);
				else:
					color(3,0);
					c=".";
				gotoxy(n*2+sx,f+1+sy);
				print(c*2,end="");
				#color(7,0);
				#print("|",end="");
		#for f in range(len(grid[0])):
		#	gotoxy(len(grid)*2+sy,f*2+sx);
		#	print("+-+",end="");
		

		gotoxy(x*2+sx,y+1+sy);
		c=ch(grid[y][x]);
		if(c=="X"):
			#color(3,6);
			ink(14);
			paper(1);
		else:
			color(3,5);
		print(c*2,end="");
		
		gotoxy(grilla[0]*2+2+sx, grilla[1]*2+2+sy);
		print("("+str(x)+","+str(y)+"):"+str(key));
		color(7,0);
		key=getkey();
		
		gotoxy(3,21); print(key);
		if(key==ESCAPE or key=="q"):
			goOut=True;
			Exit();
			"""
			if(ord(key)==0xe0):
				gotoxy (1,1); print("Cero");
				key=getch();
			"""
		if(key==RIGHT_ARROW and x<grilla[0]-1):
			x+=1;
		if(key==LEFT_ARROW and x>0):
			x-=1;
		if(key==DOWN_ARROW and y<grilla[1]-1):
			y+=1;
		if(key==UP_ARROW and y>0):
			y-=1;
		if(key==SPACE):
			cha="1" if(grid[y][x]==_SPACE) else " ";
			grid[y]=left(grid[y],x)+cha+right(grid[y],len(grid[y])-x-1);
		if(key=="s"):
			color(0,7);
			clrscr();
			print("Name?");
			a=input();
			try:
				arch = open(a+".udg", 'wb');
				pickle.dump(grid, arch);
				arch.close();
				gotoxy(1,21);
				print("Saved to file "+a+"!");
			except:
				print("The graphic could not be saved as "+a+".udg!");
			getch();
		if(key=="l"):
			o=[]+glob("*udg");
			clrscr();
			for f in o:
				if(os.path.isfile(f)):
					print(f);
			print();
			print("Name?");
			a=input();
			try:
				arch = open(a+".udg", 'rb');
				grid=pickle.load( arch);
				arch.close();
				gotoxy(1,21);
				print("File "+a+" loaded!");
			except:
				print("The file "+a+".udg could not be loaded!");
			getch();
			

EXIT=Exit;

if __name__ == '__main__':
	color(7,0);
	clrscr();
	sys.exit(main(sys.argv))

