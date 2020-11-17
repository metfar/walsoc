#!/usr/bin/ruby 
#
#  math_h.rb
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

require "./alias_h";
include Alias_H;
require "./string_h";
include String_H;
require 'io/console';
require 'timeout';

$inStd=IO.new STDIN.fileno;
$outStd=IO.new STDOUT.fileno;
$errStd=IO.new STDERR.fileno;
$pi=3.1415927;
def timer();
	begin;
		return(Gosu.milliseconds/200);
	rescue;
	end;
end;
def draw_circle(x,y,r,c,z=2);
	for f in range(0,180,2);
		ix=cos(f)*r;
		iy=sin(f)*r;
		draw_rect(x-ix,y-iy,2*ix,2*iy,c,z,mode=:default);
	end;
end;
def draw_cfa(x,y,r,c,z=2);
	for f in range(0,360,1);
		ix=cos(f)*r;
		iy=sin(f)*r;
		ix2=cos(f+1)*r;
		iy2=sin(f+1)*r;
		
		draw_line(x+ix,y+iy,c,x+ix2,y+iy2,c,z,mode=:default);
	end;
end;

module Colio_H
	ESC="\e";
	_SPACE=" ";
	def input(text=nil); #text input (BASIC-like)
        if(text!=nil); then
                print(text);
        else;
                print("?");
        end;
        print(" ");
        return(gets.chomp);
	end;
	def min(a,b);
		if(a<b); then
			return(a);
		else;
			return(b);
		end;
	end;
	def pointInCircle(x,y,cx,cy,r,precision=30);
		dx2=(cx-x)**2;
		dy2=(cy-y)**2;
		return( (dx2+dy2)<=((r+precision)**2) ); 
	end;
	def toggle(x);
		if(x); then
			return(false);
		end;
		return(true);
	end;
	def arad(x);
		return(x*$pi/180);
	end;

	def adeg(x);
		return(x*180/$pi);
	end;

	def cos(x);
		return(Math.cos(arad(x)));
	end;

	def sin(x);
		return(Math.sin(arad(x)));
	end;
	def tan(x);
		return(Math.tan(arad(x)));
	end;
	alias :tg :tan;

	def acos(x);
		return(adeg(Math.acos(x)));
	end;

	def asin(x);
		return(adeg(Math.asin(x)));
	end;

	def atan(x);
		return(adeg(Math.atan(x)));
	end;	
	def max(a,b);
		if(a>b); then
			return(a);
		else;
			return(b);
		end;
	end;
	def abs(x);
		if	(x<0); then 
			out=-x;
		else;
			out=x;
		end;
		return(x);
	end;
	def sgn(x);
		if(x<0); then
			out=-1;
		else;
			out=1;
		end;
		return(out);
	end;
	def rep(n,charact=nil);
		out="";
		if(charact==nil);then
			charact=_SPACE;
		end;
		begin;
			out=charact * n;
		rescue;
			pass;
		end;
		return(out);
	end;
	def spc(n=1);
		return(rep(n));
	end;
	def clrscr();
		print(ESC+"[2J");
	end;

	def locate(y,x);
		print(ESC+"["+str(y+1)+";"+str(x+1)+"H");
	end;

	def gotoxy(x,y);
		locate(y,x);
	end;
	def _definecolours();
		colours={};
		palette=[ 
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
		colnames=[	
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
		for f in xrange(0,len(palette));
			colours[colnames[f]]=palette[f];
		end;
		
		$colours=colours;
		$colnames=colnames;
		$palette=palette;
		return(colours);
	end;

	def type(x);
		return(x.class);
	end;
	
	def ink(i=nil);
		begin;
			if($iNK); then
				iNK=$iNK;
			else;
				iNK=7;
			end;
		rescue;
			$iNK=7;
			iNK=$iNK;
		end;
		if(i==nil); then
			return(iNK);
		end;
		begin;
			iNK;
		rescue;
			iNK=0;
		end;
		if(type(i)==type(0));then
			iNK=i;
		else;
			if(type(i)==type("home"));then
				if(nil!=$colnames.index(i.downcase));then
					iNK=$colnames.index(i.downcase);
				end;
			end;
		end;
		if(iNK>7);then
			i=iNK-8;
			uF=";1";
		else;
			i=iNK;
			uF=";22";
		end;
		print(ESC+"[3"+str(i)+uF+"m");
		$iNK=iNK;
		return(iNK);
	end;
	
	def paper(p=nil);
		begin;
			if($pAPER); then
				pAPER=$pAPER;
			else;
				pAPER=0;
			end;
		rescue;
			$pAPER=0;
			pAPER=$pAPER;
		end;
		if(p==nil);then
			return(pAPER);
		end;
		
		if(type(p)==type(0));then
			pAPER=p;
		else;
			if(type(p)==type("home"));then
				if(nil!=$colnames.index(p.downcase));then
					pAPER=$colnames.index(p.downcase);
				end;
			end;
		end;
		if(pAPER>7); then
			i=pAPER-8;
			uF="";
		else;
			i=pAPER;
			uF=";1";
		end;
		print(ESC+"[4"+str(i)+"m");
		$pAPER=pAPER;
		return(pAPER);
	end;

	def color(i=0,p=7);
		ink(i);
		paper(p);
	end;


	def getkey();
		prev=STDIN.echo?;
		STDIN.echo=false;
		out=$stdin.getch;
		STDIN.echo=prev;
		return(out);
	end;
	
	def inkey();
		status = Timeout::timeout(5) do
			return(getkey());
		end;
		return("");
	end;
	
	
	def rnd();
		return(Random.rand());
	end;
	def int(obj);
		out=0;
		begin;
			out=obj.to_s.to_i;
		rescue;
		end;
		return(out);
	end;
	
	def chr(a);
		a=int(a);
		return(a.chr);
	end;
	def range(a=1,b=nil,c=nil);
		if(c!=nil); then
			return ( (int(a)..(int(b)-1)).step(int(c)).to_a);
		elsif(b!=nil); then
			return ( (int(a)..(int(b)-1)).to_a);
		else;
			return( (0..(int(a)-1)).to_a );
		end;
	end;
	def str(a);
		begin;
			return(a.to_s);
		rescue;
			return("");
		end;
	end;
	def len(a);
		begin;
			return(a.length);
		rescue;
			if (nil!=a); then
				return(1);
			else;
				return(0);
			end;
		end;
	end;
end;

include Colio_H;

_definecolours();


False=false;
True=true;
=begin

def ch(txt=" ");
	return(" " if txt==_SPACE else "X");
end;def main(args);
	grilla=[64,16];#x,y
	grid={};
	row=rep(grilla[0]);
	
	for f in range(grilla[1]);
		grid[f]=row;
	end;
	x,y=0,0;
	goOut=False;
	key="";
	sx,sy=2,2;
	while(not goOut);
		color(7,0);
		clrscr();

		for f in range(len(grid));
			for n in range(len(grid[f]));
				c=ch(grid[f][n]);
				if(c=="X"); then
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
			


=end

if caller.length==0; then	#main file
	clrscr();
	echo (rep(32,"*"));
	name=input("What's your name?");
	print("Hello, %s\n"%(name.capitalize));
	print("Press enter to continue...");
	a=getkey();
	print("\n");
	if([10.chr,13.chr,""].include? a); then
		print("Have a good day!\n");
	else;
		print("I said Enter! Not "+a+"!!!\n");
	end;
	print("Q or Escape to finish!\n");
	key="";
	while (key!="q" and key!=chr(27));
		key=inkey();
		print(key);
	end;
	exit(0);
end;


