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


module Math_H
	
	def pi;
		#(2**0.5)*2.221441469079;#3.1415926535895347
		return(3.141592653589793);
	end;
	def e;
		#((pi**4)+(pi**5))**(1/6);#2.7182818086117377
		return(2.718281828459045);
	end;
	
	def infinite;
		return(-Math.log(0));
	end;
	def toRad(ang);
		"""
		Math Function
		-------------
		
		Converts degrees into radians.
		
		toRad(180) 
				returns 3.1415927 (PI)
		"""
		pi=3.141592653589793;
		return(ang*pi/180.0);
	end;

	def toDeg(ang);
		"""
		Math Function
		-------------
		
		Converts radians into degrees.
		
		toDeg(pi) 
				returns 180 (degrees)
		"""
		return(ang*180.0/pi);
	end;
	
	
	def round(num,digits=0);
		begin
			out=0.0+toFloat(num);
		rescue
			out=0.0;
		end;
		return(out.round(digits));
	end;
	
	def sin(ang);
		"""
		Math Function
		-------------
		
		Returns the Sine value of n-degrees angle.
		
		sin(90)
				returns 1
		"""
		return(Math.sin(toRad(ang)));
	end;

	def sinh(ang);
		"""
		Math Function
		-------------
		
		Returns the hyperbolic sine value of n-degrees angle.
		
		sinh(90)
				returns 2.30129896
		"""
		return(Math.sinh(toRad(ang)));
	end;

	def asin(val);
		"""
		Math Function
		-------------
		
		Returns the arc Sine value of n (-1<=n<=1).
		
		asin(1)
				returns 90
		"""
		return(toDeg(Math.asin(val)));
	end;

	def asinh(val);
		"""
		Math Function
		-------------
		
		Returns the hyperbolic arc sine value of n.
		
		asinh(2.301298960533041)
				returns 90
		"""
		return(toDeg(Math.asinh(val)));
	end;
	
	def cos(ang);
		"""
		Math Function
		-------------
		
		Returns the Cosine value of n-degrees angle.
		
		cos(0)
				returns 1
		"""
		return(Math.cos(toRad(ang)));
	end;
	
	def cosh(ang);
		"""
		Math Function
		-------------
		
		Returns the hyperbolic Cosine value of n-degrees angle.
		
		cosh(90)
				returns 2.50917853
		"""
		return(Math.cosh(toRad(ang)));
	end;
	
	def acos(val);
		"""
		Math Function
		-------------
		
		Returns the arc Cosine value of n.
		
		acos(0)
				returns 0
		"""
		return(toDeg(Math.acos(val)));
	end;
	
	def acosh(val);
		"""
		Math Function
		-------------
		
		Returns the hyperbolic Cosine value of n-degrees angle.
		
		acosh(2.50917853)
				returns 90
		"""
		return(toDeg(math.acosh(val)));
	end;

	def tan(ang);
		"""
		Math Function
		-------------
		
		Returns the tangent value of n-degrees angle.
		
		tan(45)
				returns 1
		"""
		return(Math.tan(toRad(ang)));
	end;

	def atan(val);
		"""
		Math Function
		-------------
		
		Returns the arc tangent in degrees.
		
		atan(1)
				returns 45
		"""
		
		return(toDeg(math.atan(val)));
	end;

	def tanh(ang);
		"""
		Math Function
		-------------
		
		Returns the hyperbolic tangent value of n-degrees angle.
		
		tan(45)
				returns 0.65579421
		"""
		return(Math.tanh(toRad(ang)));
	end;
		
	def atanh(val);
		"""
		Math Function
		-------------
		
		Returns the angle of an hyperbolic tangent arc value.
		
		atanh(0.65579421)
				returns 45.0
		"""
		return(toDeg(Math.atanh(val)));
	end;

	def atan2(y,x);
		"""
		Math Function
		-------------
		
		Returns the arc tangent of y/x in degrees.
		
		atan2(1,1)
				returns 45
		"""
		
		return(toDeg(Math.atan2(y,x)));
	end;
	
	def sqrt(num,y=2);
		"""
		Math Function
		-------------
		
		Returns the square root of a number (precision 8).
		
		sqrt(2)		returns 1.41421354
		
		"""
		num=toFloat(num);
		
		if(toFloat(y)==0.0) then;
			out=nil;
			xraise("SQRT 0 of "+str(num)+" is undefined!");
			
		else
			begin
				invers=1/toFloat(y);
				out= num ** (invers) ;
			rescue
				begin
					out=Math.sqrt(num);
				rescue
					out=0.0;
				end;
			end;
		end;
		return(out);
	end;

	alias :sqr	:sqrt;


	def decToBin(num);
		"""
		Math Function
		-------------
		
		Decimal to Binary:
		
		decToBin(138)
		
			returns '10001010'
		"""
		num=toInt(num);
		return(num.to_s(2));
	end;
	
	def decToHex(inp);
		"""
		Math Function
		-------------
		
		Decimal to Hexadecimal:
		
		decToHex(16383000)
		
			returns 'f9fc18'
		"""
		num=toInt(inp);
		return(num.to_s(16));
	end;
	
	def hexToDec(num);
		"""
		Math Function
		-------------
		
		Hexadecimal to decimal:
		
		hexToDec('0F')
			returns 15
		
		"""
		return(num.to_i(16));
	end;
	
	def hexToBList(num);
		"""
		Math Function
		-------------
		
		Hexadecimal to Bytes List:
		
		hexToBList('fffff')
			returns (15,255,255);
		"""
		out=[];
		num=str(num);
		if (len(num)%2==1) then;
			num="0"+num;
		end;
		for f in xrange(0,len(num),2);
			val=substr(num,f,2);
			out.append(val.to_i(16));
		end;
		return(out);
	end;

	def decToBList(inp);
		"""
		Math Function
		-------------
		
		Decimal to bytes:
		
		decToBList(1638400)
			returns (25,0,0);
		"""
		out=[];
		while (inp>255);
			ent=inp-(toInt(inp/256))*256;
			out.insert(0,ent);
			inp=(inp/256);
		end;
		out.insert(0,inp);
		return(out);
	end;
	
	
	def col(hexa);
		"""
		Math Function
		-------------
		
		col('ffffff') to tuple(r,g,b)
		
		"""
		val=hexToDec(hexa);
		print(decToHex(val),"\n");
		out=decToBList(val);
		while (len(out)<3);
			out.insert(0,0);
		end;
		return( out );
	end;
	
	
	
	def pow(x,y=2);
		"""
		Math Function
		-------------
		
		pow(x,y)	returns x^y
		pow(x)	returns x^2
		
		"""
		if (y==infinite) then;
			return(infinite);
		end;
		y=toFloat(y);
		if(y==0) then;
			out=1.0;
		else;
			begin
				nom=toFloat(num);
				out=num ** y;
			rescue
				out=0.0;
				xraise ("Error at power!");
			end;
		end;
		return(out);
	end;
	
	def exp(x=1);
		"""
		Math Function
		-------------
		
		exp(1)	returns e^1=2.718281828459045
		exp(0)	returns 1
		
		"""
		begin
			return(pow(e,x));
		rescue
			begin
				return(e ** toFloat(x));
			rescue
				xraise("Error at e-exponential!");
			end;
		end;
		return(1.0);
	end;

	def log(x=1);
		"""
		Math Function
		-------------
		
		log(2)	returns 0.30103 (log_10(x))
		
		"""
		begin
			return(Math.log(toFloat(x))/Math.log(10));
		rescue
			xraise("Error at 10-based logarythm!");
		end;
		return(0.0);
	end;

	def ln(x=1);
		"""
		Math Function
		-------------
		
		ln(2)	returns 0.69314718 (log_e(x))
		
		"""
		begin
			return(Math.log(x));
		rescue
			xraise("Error at natural logarythm!");
		end;
		return(0.0);
	end;
	
	def div(x,y=1);
		"""
		Math Function
		-------------
		
		div(3,2)	returns 1.5
		div(3,0)	returns infinite
		
		"""
		y=toFloat(y);
		x=toFloat(x);
		if(y==0.0) then;
			return(infinite);
		else;
			begin
				return(x/y);
			rescue
				xraise("Error at division!");
			end;
		end;
		return(0.0);
	end;

	def fabs(x);
		"""
		Math Function
		-------------
		
		fabs(-3.33333)		returns 3.33333
		
		"""
		x=toFloat(x);
		begin
			if(x<0) then;
				x=-x;
			end;
			return(x);
		rescue
			xraise("Error at fabs!");
		end;
		return(0.0);
	end;

	def floor(num);
		"""
		Math Function
		-------------
		
		floor(-3.33333)	returns -4
		floor( 3.33333)	returns  3
		
		"""
		x=toFloat(num);
		begin
			return(x.floor);
		rescue
			xraise("Error at floor!");
		end;
		return(0.0);
	end;


	def ceil(num);
		"""
		Math Function
		-------------
		
		ceil(-3.33333)	returns -3
		
		ceil( 3.33333)	returns  4
		
		"""
		x=toFloat(num);
		begin
			return(x.ceil);
		rescue
			xraise("Error at ceil!");
		end;
		return(0.0);
	end;

	def fmod(x,y);
		"""
		Math Function
		-------------
		
		fmod(5,3.3)	returns -1.7
		
		fmod(10,3)	returns  1.0
		
		"""
		x=toFloat(x);
		y=toFloat(y);
		begin
			return(x%y);
		rescue
			xraise("Error at fmod!");
		end;
		return(0.0);
	end;

	def min(*vargs);
		args=(vargs);
		begin
			if(len(args)>1) then;
				_min=toFloat(args[0]);
			else;
				_min=toFloat(args);
			end;
			for f in args;
				if( _min > f ) then;
					_min=f;
				end;
			end;
		rescue
			_min=nil;
		end;
		return(_min);
	end;
		
	def max(*vargs);
		args=(vargs);
		begin
			if(len(args)>1) then;
				_max=args[0];
			else;
				_max=args;
			end;
			for f in args;
				if( f > _max ) then;
					_max=f;
				end;
			end;
		rescue
			_max=nil;
		end;
		return(_max);
	end;
	
	
	def pal(n);
		"""
		Math Function
		-------------
		
		pal		#Set default colours as global
		
		pal(1)	#Dark palette;
		
		pal()	#ZX_Spectrum-like palette;
		
		
		"""
		
		colnames=["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "brightblack", "brightred", "brightgreen", "brightyellow", "brightblue", "brightmagenta", "brightcyan", "brightwhite"];
		
		n=toInt(n);
		if(n==1) then;
			colvalues=[	[0, 0, 0], [159, 0, 0], [0, 159, 0], [159, 159, 0], [0, 0, 159], [159, 0, 159], [0, 159, 159], [159, 159, 159], [36, 36, 36], [189, 0, 0], [0, 189, 0], [189, 189, 0], [0, 0, 189], [189, 0, 189], [0, 189, 189], [189, 189, 189]];
			
		else;
			colvalues=[[0, 0, 0], [215, 0, 0], [0, 215, 0], [215, 215, 0], [0, 0, 215], [215, 0, 215], [0, 215, 215], [215, 215, 215], [51, 51, 51], [255, 0, 2], [0, 255, 3], [253, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]];
		end;
		out=Dict();
		for f in xrange(0,min(len(colvalues),len(colnames)));
			out[colnames[f]]=colvalues[f];
		end;
		return(out);
	end;



end;



if caller.length==0 then;	#main file
	include Math_H;
	echo (toRad(90));
	echo (sqr(2));
	echo (hexToBList("5384ff"));
	echo (decToBList(1638400));
	echo (col("538457"));
	echo (pal(1));
	exit(0);
end;


