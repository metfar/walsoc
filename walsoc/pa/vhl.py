#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vhl.py
#  
#  Copyright 2020 William Martinez Bas <wmartinez@metfar>
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

#from all_h import *;
import sys;

VARS={};
true=TRUE=True;
false=FALSE=False;
null=NULL=nil=NIL=None;

def TF(a):
	out=True;
	for f in ["false","0","f","none"]:
		if(f in str(a).lower()):
			out=false;
	return(out==true);
	
def Not(a):
	return((not TF(a))==true);
def Nor(a,b):
	return(Not(a) & Not(b));
def Xor(a,b):
	return(TF(a) != TF(b));
def Imp(a,b):
	return(Not(TF(a) & Not(b)));

def Nand(*args):
	out=0;
	for f in args:
		out=out | Not(f);
	return(out==true);


def Or(*args):
	out=0;
	for f in args:
		out=out | TF(f);
	return(out ==true);
	

def And(*args):
	out=1;
	for f in list(args):
		out=out & TF(f);
	return(out ==true);

	
def Iff(*args):
	out=1;
	vargs=list(args);
	while(len(vargs)>0):
		first=vargs.pop(0);
		out=(first==out);
	return(out ==true);


	
	
NOT=Not;
NAND=Nand;
AND=And;
OR=Or;
NOR=Nor;
XOR=Xor;
IFF=IFANDONLYIF=IfAndOnlyIf=Iff;
IMP=Implies=Imp;
def clrscr():
	print(chr(27)+"[2J\n");

def printv(*args):
	vargs=list(args);
	out="";
	for f in vargs:
		x=str(f).strip().lower();
		if(x in ["true","false"]):			
			print("T" if ("true" in x) else "F",end="");
		else:
			print(f,end="");
	print();
	
def example(args):
	clrscr();
	print(	"a\tb\t"+
			"¬a\t¬b\t"+
			"a∧b\t"+
			"a∨b\t"+
			"a⊼b\t"+
			"a⊽b\t"+
			"a⊻b\t"+
			"a⇒b\t"+
			"a⟺b".replace("\t","\t\r\r")); 
	for a in [1,0]:
		for b in [1,0]:
			printv(	a==true,"\t",
					b==true,"\t",
					Not(a),"\t",
					Not(b),"\t",
					And(a,b),"\t",
					Or(a,b),"\t",
					Nand(a,b),"\t",
					Nor(a,b),"\t",
					Xor(a,b),"\t",
					Imp(a,b),"\t",
					Iff(a,b));
					
	return(0);


def main(args):
	var=[1,0];
	VARS={
			"Armed"	:	var,
			"Door"	:	var,
			"Glass"	:	var,
			"Motion":	var
			};
	RES=[	{
			"name"	:	"Alarm",
			"title"	:	"Armed ∧ ( Door ∨ Glass ∨ Motion )",
			"value"	:	"AND(Armed, OR( Door, Glass, Motion ))"
			}
		];
	
	rows=1;
	cols={};
	#vals={};
	lVars=len(VARS);
	mods=[0]*lVars;
	n=1;
	for f in VARS:
		length=len(VARS[f]);
		
		rows=rows*length;
		cols[f]=length;
		mods[lVars-n]=rows;
		n+=1;
		#vals[f]=VARS[f][0];
	
	row=0;
	names,values=list(VARS.keys()),list(VARS.values());
	for f in names:
		print(f,end="\t");
	
	for f in RES:
		print(f["name"],end="\t");
	
	print();
	#for f in mods:	print(f,end="\t");
	#print();
	while(row<rows):
		t=row;
		leRow=[0]*lVars;
		
		for f in range(len(values)-1,-1,-1):
			leRow[f] = t %  len(values[f]) ;
			t=(t-leRow[f]) // len(values[f]);
		n=0;
		val=[0]*lVars;
		for f in leRow:
			val[n]=str(values[n][f]);
			print(val[n].center(len(names[n])),end="\t");
			cad="_"+names[n]+"="+val[n];
			n+=1;
			exec(cad);
		#for f in RES:
			
		print();
		row+=1;
		
	return(0);

if __name__ == '__main__':
    exit(main(sys.argv));
