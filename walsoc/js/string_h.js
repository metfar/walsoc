#!/usr/bin/js
/*
#  string_h.py
#  
#  Copyright 2020- William Martinez Bas <metfar@gmail.com>
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
#  This is part of WalSoc Project < https://github.com/metfar/walsoc/tree/master/walsoc/js >
*/

STRING_H=true;

True=true;
False=false;

function len(x){
	try{
		return(x.length);
		}
	catch(e){
		try{
			return(x.length());
		}
		catch(e){
			return(0);
		}
	}
}

function array(){
	const out=[];
	for (var f=0; f<arguments.length; f++){
		out[f]=arguments[f];
	}
	return(out);
}


function print(){
	if(len(arguments)<1)
		out="\n";
	else
	{
		out=arguments[0];
		for (var f=1; f<arguments.length; f++){
			out+=" "+String(arguments[f]);
		}
	}
	console.log(out);
}


function join(glue=" ",arrayIn=[]){
	out="";
	for (var f=0; f<len(arrayIn); f++){
		out+=glue+String(arrayIn[f]);
	}
	return(out);
}

function is_null(x){
	try{
		return(null==x);
	} catch(e){
		return(false);
	}
}

function str(x){
	try{
		return((String)(x));
	} catch(e){
		return("");
	}
}

function split(delimiter=" ",string="",limit=null){
	out=[];
	_tmp=str(string).split(delimiter);
	if(is_null(limit))
		 return(_tmp);
	else{
		 if(limit==-1)
			return(_tmp);
		 else
			return(_tmp.slice(0,limit+1));
		}
	return(out);
}

function toUpper(string){
	a="";
	try{
		a=a+string.toUpperCase();
	}catch(e){
		tmp=1;
	}
	return(a);
}

function toLower(string){
	a="";
	try{
		a=a+string.toLowerCase();
	}catch(e){
		tmp=1;
	}
	return(a);
}

function toCaps(string){
	a="";
	arr=str(string).split(' ');
	arr=arr.map(word => word[0].toUpperCase() + word.substring(1));
	a=arr.join(" ");
	return(a);
}
function isIn(what,where){
	return(where.indexOf(what)>-1);
}
function filterAlpha(which, withWhat){
	out="";
	for(f=0;f<len(which);f++){
		if(isIn(which[f],withWhat))
			out+=str(which[f]);
	}
	return(out);
}
function bin2dec(num){
	/*
	Math Function
	-------------
	Binary to decimal:
	
	bin2dec('10101010')
			returns 170
	*/
	
	return(parseFloat(filterAlpha(num,"01"), 2));
}

function dec2bin(num){
	/*
	Math Function
	-------------
	Decimal to binary:
	
	dec2bin(42)
			returns "52"
	*/
	tmp=filterAlpha(str(num),"-0123456789.");
	if(len(tmp)<1)
		tmp="0";
	return(parseFloat(tmp).toString(2));
}


function oct2dec(num){
	/*
	Math Function
	-------------
	Octal to decimal:
	
	oct2dec('63')
			returns 51
	*/
	return(parseFloat(filterAlpha(num,"01234567"), 8));
}


function dec2oct(num){
	/*
	Math Function
	-------------
	Decimal to octal:
	
	dec2oct(42)
			returns "52"
	*/
	tmp=filterAlpha(str(num),"-0123456789.");
	if(len(tmp)<1)
		tmp="0";
	return(parseFloat(tmp).toString(8));
}

function hex2dec(num){
	/*
	Math Function
	-------------
	Hexadecimal to decimal:
	
	hex2dec('6a')
			returns 106
	*/
	return(parseFloat(filterAlpha(toLower(num),"0123456789abcdef"), 16));
}

function dec2hex(num){
	/*
	Math Function
	-------------
	Decimal to hexadecimal:
	
	dec2hex(42)
			returns "2a"
	*/
	tmp=filterAlpha(str(num),"-0123456789.");
	if(len(tmp)<1)
		tmp="0";
	return(parseFloat(tmp).toString(16));
}


function dec2exp(num){
	/*
	Math Function
	-------------
	Decimal to exponential:
	
	dec2exp(42)
			returns "4.2e+1"
	*/
	tmp=filterAlpha(str(num),"-0123456789.");
	if(len(tmp)<1)
		tmp="0";
	return(parseFloat(tmp).toExponential());
}


function exp2dec(num){
	/*
	Math Function
	-------------
	Exponential to decimal:
	
	exp2dec("4.2e+1")
			returns 42
	*/
	tmp=filterAlpha(str(num),"-+0123456789.e");
	if(len(tmp)<1)
		tmp="0";
	return(parseFloat(tmp));
}

function dec2exp10(num){
	/*
	Math Function
	-------------
	Decimal to exponential10:
	
	dec2exp10(42)
			returns "4.2 x 10^+1"
	*/
	return(str(dec2exp(num)).replace(/e\+?/, ' x 10^'));
}

function exp10toDec(num){
	/*
	Math Function
	-------------
	Exponential10 to Decimal:
	
	exp10toDec(42)
			returns "4.2 x 10^+1"
	*/
	num=filterAlpha(str(num),"+-.x^0123456789").replace(/x10^/,"e");
	
	return(exp2dec(num));
}


function sprintf(){
	/* 
	File Functions
	--------------
	
	stringOut= sprintf (FORMAT [,arg1,arg2,...]) 
	
	c-like sprintf
	
	FORMAT
	%d      integer with sign
	%i      integer with sign
	%u      unsigned int
	%o      octal
	%x      hexadecimal lowercase
	%X      hexadecimal uppercase
	%f      floating point
	%e      scientific notation lowercase
	%E      scientific notation upppercase
	%c      character
	%s      string
	
	
	*/
	formats="diuoxXfleEcs";
	out="";
	args=[];
	for (f=0;f<len(arguments);f++)
		args[f]=arguments[f];
	
	if(len(args)>0)
		{
		Format=str(args.shift());
		if(len(args)>0)
			{
				chain=Format.split("%");
				if(len(chain)<2){
					out=Format;
				}
				else
				{
					for (f=0;f<len(chain);f++){
						which=chain[f];
						
						
					}
					
				}
			
			}
		else
			{
				out=Format;
			}
		}
	
	return(out);
}

printf=console.log;
/*
function printf(){//not really but it is enough approximated to it
	if(len(arguments)>1)
		{
		form=str(arguments[0]);
		for (f=1;f<len(arguments);f++)
			form=form.format(arguments[f]);
		}
	else
		if(len(arguments)<1)
			form=arguments[0];
		else
			form="\n";
	console.log(form);
}*/
printf("%s %i %f",toLower(toUpper(toCaps("la casa roja"))),5,3.3);
printf("%s %s|%s","La","casa","roja");
print(array("La","casa","roja"));
print("Casa");
printf("%s","-----------");

