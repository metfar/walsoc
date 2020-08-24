#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
	ALIAS_H;
except NameError:
	from alias_h import * ;
MATH_H=TRUE;

import math;
from sys import version;
#from math import sin, cos,sqrt;

PI=pi=3.1415927;
e=E=  2.7182818;
infinite=math.inf;


def arad(ang):
	"""
	Math Function
	-------------
	
	Converts degrees into radians.
	
	arad(180) 
			returns 3.1415927 (PI)
	"""
	return(ang*pi/180.0);
def adeg(ang):
	"""
	Math Function
	-------------
	
	Converts radians into degrees.
	
	adeg(pi) 
			returns 180 (degrees)
	"""
	return(ang*180.0/pi);

def sin(ang):
	"""
	Math Function
	-------------
	
	Returns the Sine value of n-degrees angle.
	
	sin(90)
			returns 1
	"""
	return(round(math.sin(arad(ang)),8));

def sinh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic sine value of n-degrees angle.
	
	sinh(90)
			returns 2.30129896
	"""
	return(round(math.sinh(arad(ang)),8));
def asin(val):
	"""
	Math Function
	-------------
	
	Returns the arc Sine value of n (-1<=n<=1).
	
	asin(1)
			returns 90
	"""
	return(adeg(math.asin(val)));

def asinh(val):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic arc sine value of n.
	
	asinh(2.301298960533041)
			returns 90
	"""
	return(round(adeg(math.asinh(val)),7));

def cos(ang):
	"""
	Math Function
	-------------
	
	Returns the Cosine value of n-degrees angle.
	
	cos(0)
			returns 1
	"""
	return(round(math.cos(arad(ang)),8));

def cosh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic Cosine value of n-degrees angle.
	
	cosh(90)
			returns 2.50917853
	"""
	return(round(math.cosh(arad(ang)),8));
def acos(val):
	"""
	Math Function
	-------------
	
	Returns the arc Cosine value of n.
	
	acos(0)
			returns 0
	"""
	dm=val/2*.0000000075;
	return(round(adeg(math.acos(val+dm)),7));

def acosh(val):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic Cosine value of n-degrees angle.
	
	acosh(2.50917853)
			returns 90
	"""
	return(round(adeg(math.acosh(val)+.0000000005),7));


def tan(ang):
	"""
	Math Function
	-------------
	
	Returns the tangent value of n-degrees angle.
	
	tan(45)
			returns 1
	"""
	return(round(math.tan(arad(ang)),7));

def atan(val):
	"""
	Math Function
	-------------
	
	Returns the arc tangent in degrees.
	
	atan(1)
			returns 45
	"""
	
	return(round(adeg(math.atan(val)),8));

def tanh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic tangent value of n-degrees angle.
	
	tan(45)
			returns 0.65579421
	"""
	return(round(math.tanh(arad(ang)),8));
	
def atanh(val):
	return(round(adeg(math.atanh(val)),6));


def atan2(y,x):
	"""
	Math Function
	-------------
	
	Returns the arc tangent of y/x in degrees.
	
	atan2(1,1)
			returns 45
	"""
	
	return(round(adeg(math.atan2(y,x)),5));

def sqrt(num,y=2,digits=8):
	"""
	Math Function
	-------------
	
	Returns the square root of a number (precision 8).
	
	sqrt(2)		returns 1.41421354
	sqrt(2,3)		returns 1.25992105
	sqrt(2,3,2)	returns 1.26
	
	"""
	if(y==0):
		return(infinite);
	else:
		try:
			invers=1/y;
			return(round(math.pow(num,invers),digits));
		except:
			try:
				return(round(math.sqrt(num),digits));
			except:
				return(0.0);


sqr=sqrt;


def bin2dec(num):
	"""
	Math Function
	-------------
	
	Binary to decimal:
	
	bin2dec('10101010')
		
			returns 170
	
	"""
	return(int(num,2));

def oct2dec(num):
	"""
	Math Function
	-------------
	
	Octal to decimal:
	
	oct2dec('063')
		returns 51
	
	"""
	return(int(num,8));

def hex2dec(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to decimal:
	
	hex2dec('0F')
		returns 15
	
	"""
	return(int(num,16));

def hex2bytes(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to bytes:
	
	hex2bytes("ffff")
		returns (255,255);
	"""
	out=[];
	for f in range(0,len(num),2):
		out.append(int(num[f:f+2],16));
	return(out);


def dec2bytes(inp):
	"""
	Math Function
	-------------
	
	Decimal to bytes:
	
	dec2bytes(65535)
		returns (255,255);
	"""
	out=[];
	while inp>255:
		ent=inp-(inp//256)*256;
		out.insert(0,ent);
		inp=inp//256;
	out.insert(0,inp);
	return(out);


def col(hexa):
	"""
	Math Function
	-------------
	
	col("ffffff") to tuple(r,g,b)
	
	"""
	out=dec2bytes(hex2dec(hexa));
	while len(out)<3:
		out.insert(0,0);
	return( out );
	

def pal(n):
	"""
	Math Function
	-------------
	
	pal		#Set default colours as global
	
	pal(1)	#Dark palette;
	
	pal()	#ZX_Spectrum-like palette;
	
	
	"""
	global BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHTBLACK, BRIGHTRED, BRIGHTGREEN, BRIGHTYELLOW, BRIGHTBLUE, BRIGHTMAGENTA, BRIGHTCYAN, BRIGHTWHITE;
	global black, red, green, yellow, blue, magenta, cyan, white, brightblack, brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan, brightwhite;
	
	try:
		n==1;
		BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHTBLACK, BRIGHTRED, BRIGHTGREEN, BRIGHTYELLOW, BRIGHTBLUE, BRIGHTMAGENTA, BRIGHTCYAN, BRIGHTWHITE=black, red, green, yellow, blue, magenta, cyan, white, brightblack, brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan, brightwhite=[0, 0, 0], [159, 0, 0], [0, 159, 0], [159, 159, 0], [0, 0, 159], [159, 0, 159], [0, 159, 159], [159, 159, 159], [36, 36, 36], [189, 0, 0], [0, 189, 0], [189, 189, 0], [0, 0, 189], [189, 0, 189], [0, 189, 189], [189, 189, 189];
	except:
		BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHTBLACK, BRIGHTRED, BRIGHTGREEN, BRIGHTYELLOW, BRIGHTBLUE, BRIGHTMAGENTA, BRIGHTCYAN, BRIGHTWHITE=black, red, green, yellow, blue, magenta, cyan, white, brightblack, brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan, brightwhite=[0, 0, 0], [215, 0, 0], [0, 215, 0], [215, 215, 0], [0, 0, 215], [215, 0, 215], [0, 215, 215], [215, 215, 215], [51, 51, 51], [255, 0, 2], [0, 255, 3], [253, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255];


def pow(x,y=2):
	"""
	Math Function
	-------------
	
	pow(x,y)	returns x^y
	pow(x)	returns x^2
	
	"""
	if(y==0):
		return(1.0);
	elif (y==infinite):
		return(infinite);
	else:
		try:
			return(round(math.pow(num,y),digits));
		except:
			try:
				return(math.pow(num,y));
			except:
				printf("Error at power!");
				return(0.0);
	
def exp(x=1,digits=8):
	"""
	Math Function
	-------------
	
	exp(x)	returns e^x
	
	"""
	try:
		return(round(math.exp(x),digits));
	except:
		try:
			return(math.pow(e,x));
		except:
			try:
				return(e**x);
			except:
				printf("Error at e-exponential!");
				return(1);

def log(x=1,digits=8):
	"""
	Math Function
	-------------
	
	log(2)	returns 0.30103 (log_10(x))
	
	"""
	try:
		return(round(math.log10(x),digits));
	except:
		try:
			return(math.log10(x));
		except:
			printf("Error at 10-based logarythm!");
			return(0);

def ln(x=1,digits=8):
	"""
	Math Function
	-------------
	
	ln(2)	returns 0.69314718 (log_e(x))
	
	"""
	try:
		return(round(math.log(x),digits));
	except:
		try:
			return(math.log(x));
		except:
			printf("Error at natural logarythm!");
			return(0);

def div(x,y=1,digits=8):
	"""
	Math Function
	-------------
	
	div(3,2)	returns 1.5
	div(3,0)	returns infinite
	
	"""
	if(y==0):
		return(infinite);
	else:
		try:
			return(round(y/x,digits));
		except:
			printf("Error at division!");
			return(0);

def fabs(x,digits=8):
	"""
	Math Function
	-------------
	
	fabs(-3.33333)		returns 3.33333
	fabs( 3.33333, 2)	returns 3.33
	
	"""
	try:
		return(round(math.fabs(x),digits));
	except:
		printf("Error at fabs!");
		return(0);

def floor(num):
	"""
	Math Function
	-------------
	
	floor(-3.33333)	returns -4
	floor( 3.33333)	returns  3
	
	"""
	try:
		return(math.floor(num));
	except:
		printf("Error at floor!");
		return(0);
def ceil(num):
	"""
	Math Function
	-------------
	
	ceil(-3.33333)	returns -3
	
	ceil( 3.33333)	returns  4
	
	"""
	try:
		return(math.ceil(num));
	except:
		printf("Error at ceil!");
		return(0);

def fmod(x,y,digits=8):
	"""
	Math Function
	-------------
	
	fmod(5,3.3)	returns -1.7
	
	fmod(10,3,2)	returns  1.0
	
	"""
	try:
		return(round(math.fmod(x,y),digits));
	except:
		try:
			return(math.fmod(x,y));
		except:
			printf("Error at fmod!");
			return(0);



DEFS_MATH=[
		'__builtins__', 
		'__add__',
		'__class__',
		'__contains__',
		'__delattr__',
		'__dir__',
		'__eq__',
		'__format__',
		'__ge__',
		'__getattribute__',
		'__getitem__',
		'__getnewargs__',
		'__gt__',
		'__hash__',
		'__init__',
		'__init_subclass__',
		'__iter__',
		'__le__',
		'__len__',
		'__lt__',
		'__mod__',
		'__mul__',
		'__ne__',
		'__new__',
		'__reduce__',
		'__reduce_ex__',
		'__repr__',
		'__rmod__',
		'__rmul__',
		'__setattr__',
		'__sizeof__',
		'__str__',
		'__subclasshook__',
		'__doc__', 
		'__loader__', 
		'__name__', 
		'__package__', 
		'__spec__',
		'help',
		'version',
		'DEFS_MATH',
		'__annotations__',
		'__builtins__',
		'__cached__',
		'__doc__',
		'__file__',
		'__loader__',
		'__name__',
		'__package__',
		'__spec__'
		];
CMDS_MATH=dir(); 

def main(args):
	print("""MATH_H\n
	
	Set of common mathematical operations.
	
	Directory
	---------
	\n""");
	a=CMDS_MATH;
	a.sort();
	for f in a:
		if(f not in DEFS_MATH):
			h_doc=str(eval(f+".__doc__")).strip();
			if(h_doc!="None"):
				print("\t"+f);
	"""
	for f in CMDS_:
		if(f not in DEFS_):
			h_doc=str(eval(f+".__doc__")).strip();
			if(h_doc!="None"):
				printf("%s\n",h_doc);"""
	return(0);

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
else:
	pal(1);

