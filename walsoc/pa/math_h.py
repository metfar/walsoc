#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
	ALIAS_H;
except NameError:
	from alias_h import * ;
try:
	STRING_H;
except NameError:
	from string_h import * ;

MATH_H=TRUE;

import math;
from sys import version;
#from math import sin, cos,sqrt;

PI=pi=PI=3.141592653589793;	#(2**0.5)*2.221441469079;#3.1415926535895347
e=2.718281828459045; 		#((pi**4)+(pi**5))**(1/6);#2.7182818086117377
phi=1.618033988749895;          #phi=0.5+(5**(0.5))*0.5; Golden ratio
infinite=None;#math.inf;


def toRad(ang):
	"""
	Math Function
	-------------
	
	Converts degrees into radians.
	
	toRad(180) 
			returns 3.1415927 (PI)
	"""
	return(ang*pi/180.0);
def toDeg(ang):
	"""
	Math Function
	-------------
	
	Converts radians into degrees.
	
	toDeg(pi) 
			returns 180 (degrees)
	"""
	return(ang*180.0/pi);
	
def toFloat(inp):
	"""
	Convert first ocurrency of numeric value 
	into a floating point number
	
	toFloat(" la casa roja 3.2 180 ")
			
			ANS: 3.2
	"""
	out=0.0;
	x=sprintf("%s",inp).strip();
	for f in x.split():
		try:
			tmp=(type(float(f))==type(1.1));
			
		except:
			tmp=false;
		
		if (tmp):
			out=float(f);
			break;
	return(out);

def toInt(inp):
	return(int(toFloat(inp)));
	
#round native


def sin(ang):
	"""
	Math Function
	-------------
	
	Returns the Sine value of n-degrees angle.
	
	sin(90)
			returns 1
	"""
	return(math.sin(toRad(ang)));#(round(math.sin(toRad(ang)),8));

def sinh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic sine value of n-degrees angle.
	
	sinh(90)
			returns 2.30129896
	"""
	return (math.sinh(toRad(ang))); #(round(math.sinh(toRad(ang)),8));
	
def asin(val):
	"""
	Math Function
	-------------
	
	Returns the arc Sine value of n (-1<=n<=1).
	
	asin(1)
			returns 90
	"""
	return(toDeg(math.asin(val)));

def asinh(val):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic arc sine value of n.
	
	asinh(2.301298960533041)
			returns 90
	"""
	return(toDeg(math.asinh(val)));

def cos(ang):
	"""
	Math Function
	-------------
	
	Returns the Cosine value of n-degrees angle.
	
	cos(0)
			returns 1
	"""
	return(math.cos(toRad(ang)));

def cosh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic Cosine value of n-degrees angle.
	
	cosh(90)
			returns 2.50917853
	"""
	return(math.cosh(toRad(ang)));
	
def acos(val):
	"""
	Math Function
	-------------
	
	Returns the arc Cosine value of n.
	
	acos(0)
			returns 0
	"""
	dm=0;#val/2*.0000000075; used in early versions with rounded values
	return(toDeg(math.acos(val+dm)));

def acosh(val):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic Cosine value of n-degrees angle.
	
	acosh(2.50917853)
			returns 90
	"""
	dm=0;#.0000000005
	return(toDeg(math.acosh(val)+dm));


def tan(ang):
	"""
	Math Function
	-------------
	
	Returns the tangent value of n-degrees angle.
	
	tan(45)
			returns 1
	"""
	return(math.tan(toRad(ang)));

def atan(val):
	"""
	Math Function
	-------------
	
	Returns the arc tangent in degrees.
	
	atan(1)
			returns 45
	"""
	
	return(toDeg(math.atan(val)));

def tanh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic tangent value of n-degrees angle.
	
	tan(45)
			returns 0.65579421
	"""
	return(math.tanh(toRad(ang)));
	
def atanh(val):
	"""
	Math Function
	-------------
	
	Returns the angle of an hyperbolic tangent arc value.
	
	atanh(0.65579421)
			returns 45.0
	"""
	return(toDeg(math.atanh(val)));


def atan2(y,x):
	"""
	Math Function
	-------------
	
	Returns the arc tangent of y/x in degrees.
	
	atan2(1,1)
			returns 45
	"""
	
	return(toDeg(math.atan2(y,x)));

def sqrt(num,y=2):
	"""
	Math Function
	-------------
	
	Returns the square root of a number (precision 8).
	
	sqrt(2)		returns 1.41421354
	sqrt(2,3)		returns 1.25992105
	sqrt(2,3,2)	returns 1.26
	
	"""
	num=toFloat(num);
	if(toFloat(y)==0.0):
		xraise("SQRT 0 of "+str(num)+" is undefined!");
		return(null);
	else:
		try:
			invers=1/y;
			return(math.pow(num,invers));
		except:
			try:
				return(math.sqrt(num));
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

def hexToDec(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to decimal:
	
	hexToDec('0F')
		returns 15
	
	"""
	return(int(num,16));

def hexToBList(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to Bytes List:
	
	hex2List("fffff")
		returns (15,255,255);
	"""
	out=[];
	if(len(num)%2==1):
		num="0"+str(num);
	
	for f in range(0,len(num),2):
		out.append(int(num[f:f+2],16));
	return(out);

def decToBin(inp):
	"""
	Math Function
	-------------
	
	Decimal to Binary:
	
	decToBin(138)
	
		returns '10001010'
	"""
	num=toInteger(inp);
	return(bin(num)[2:]);
	
def decToHex(inp):
	"""
	Math Function
	-------------
	
	Decimal to Hexadecimal:
	
	decToHex(16383000)
	
		returns 'f9fc18'
	"""
	num=toInteger(inp);
	return(hex(num)[2:]);

def hexToBList(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to Bytes List:
	
	hexToBList('fffff')
		returns (15,255,255);
	"""
	out=[];
	num=str(num);
	if (len(num)%2==1):
		num="0"+num;

	for f in xrange(0,len(num),2):
		val=substr(num,f,2);
		out.append(int(val,16));

	return(out);


def decToBList(inp):
	"""
	Math Function
	-------------
	
	Decimal to bytes:
	
	decToBList(1638400)
		returns [25,0,0];
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
	out=decToBList(hexToDec(hexa));
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
	colnames=["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "brightblack", "brightred", "brightgreen", "brightyellow", "brightblue", "brightmagenta", "brightcyan", "brightwhite"];
	
	n=toInt(n);
	if(n==1):
		COLVALUES=[	[0, 0, 0], [159, 0, 0], [0, 159, 0], [159, 159, 0], [0, 0, 159], [159, 0, 159], [0, 159, 159], [159, 159, 159], [36, 36, 36], [189, 0, 0], [0, 189, 0], [189, 189, 0], [0, 0, 189], [189, 0, 189], [0, 189, 189], [189, 189, 189]];

	else:
		COLVALUES=[[0, 0, 0], [215, 0, 0], [0, 215, 0], [215, 215, 0], [0, 0, 215], [215, 0, 215], [0, 215, 215], [215, 215, 215], [51, 51, 51], [255, 0, 2], [0, 255, 3], [253, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]];
	out=dict();
	for f in xrange(0,min(len(COLVALUES),len(colnames))):
		out[colnames[f]]=COLVALUES[f];
	#	return({"names":colnames,"values":COLVALUES});
	return(out);


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
	
def exp(x=1):
	"""
	Math Function
	-------------
	
	exp(x)	returns e^x
	
	"""
	try:
		return(math.pow(e,x));
	except:
		try:
			return(e**x);
		except:
			xraise("Error at e-exponential!");
	return(1.0);

def log(x=1):
	"""
	Math Function
	-------------
	
	log(2)	returns 0.30103 (log_10(x))
	
	"""
	if(toFloat(x)==0.0):
		return(-math.inf);
	try:
		return(math.log10(x));
	except:
		xraise("Error at 10-based logarythm!");
	return(0);

def ln(x=1,digits=8):
	"""
	Math Function
	-------------
	
	ln(2)	returns 0.69314718 (log_e(x))
	
	"""
	try:
		return(math.log(x));
	except:
		printf("Error at natural logarythm!");
		return(0);

def div(x,y=1):
	"""
	Math Function
	-------------
	
	div(3,2)	returns 1.5
	div(3,0)	returns infinite
	
	"""
	y=toFloat(y);
	x=toFloat(x);
	if(y==0.0):
		return(infinite);
	else:
		try:
			return(x/y);
		except:
			xraise("Error at division!");
	return(0.0);

def fabs(x,digits=8):
	"""
	Math Function
	-------------
	
	fabs(-3.33333)		returns 3.33333
	
	"""
	try:
		return(math.fabs(x));
	except:
		xraise("Error at fabs!");
	return(0.0);

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

def fmod(x,y):
	"""
	Math Function
	-------------
	
	fmod(5,3.3)	returns -1.7
	
	fmod(10,3)	returns  1.0
	
	"""
	try:
		return(math.fmod(x,y));
	except:
		printf("Error at fmod!");
		return(0);

#min native
#max native


def main(args):
	
	echo (toRad(90));
	echo (sqr(2));
	echo (hexToBList("5384ff"));
	echo (decToBList(1638400));
	echo (pal(1));
	return(0);

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
else:
	pal(1);

