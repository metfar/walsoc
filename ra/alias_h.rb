#!/usr/bin/ruby 
#
#  alias_h.rb
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

module Alias_H
	#ARGV native
	null=Null=NULL=NONE=None=nil;
	ON=True=TRUE=true;
	OFF=False=false;
	ALIAS_H=TRUE;
	$ECHO=ON;
	$GLUE=" ";
	#version native
	APP=$0;
	PROCID=$$;
	FS=File::SEPARATOR;
	NAME=APP;
	ENTER=enter=LF="\n";
	EXCLAMATION="!";
	LOADED=" loaded"+EXCLAMATION;
	#RUBYOPT="-W0";
	CORRECT_TYPES={
				"array"=>		"list",
				"hash"=>		"dict",
				"trueclass"=>	"boolean",
				"falseclass"=>	"boolean"
				};
	
	def List(*vargs);
		"""
				Define a list
		
		List()
				returns []
		
		List(1,['la','casa'],'roja')
				
				returns [1, ['la', 'casa'], 'roja']
		
		"""
		args=(vargs);
		out=[];
		for f in args;
			out.append(f);
		end;
		return(out);
	end;
	
	def Dict(*vargs);
		"""
		Dict()
				returns {}
				
		Dict('a'=>1,'b'=>2)
				returns {'a'=>1, 'b'=>2}
		
		Dict(a:1,b:2)
				returns {:a=>1, :b=>2}
		
		"""
		if(vargs.length<1) then;
			return({});
		end;
		begin
			return ((vargs)[0]);
		rescue
			return ((vargs));
		end;
	end;
	
	def version;
		return(RUBY_VERSION);
	end;
	
	def procStr(x);
		out=x.to_s;
		begin
			if		(out[0]=='[' and out[-1]==']') then;
					out=out[1..-2];#remove first and last  []
			end;
			if		(out[0]=='"' and out[-1]=='"') then;
					out=out[1..-2];#remove first and last quotation
			end;
			if 		(out[0]=="'" and out[-1]=="'") then;
					out=out[1..-2];#remove first and last simple quotation
			end;
		end;
		return(out);
	end;
	
	def echo(*args);
		"""
			GENERAL Function
			================
			
			if global ECHO is ON
				prints the argument and an ENTER
			else
				returns argument as a string
			
			
			It returns the string conversion of argument.
		"""
		begin
			$ECHO
		rescue
			$ECHO=TRUE;
		end;
		
		
		begin
			out=procStr(sprintf("%s",args.to_s));#args.join($GLUE);
		rescue
			out="";
		end;
		
		if 	($ECHO==ON)	then;
			print(out,ENTER);
		end;
		return(out);
	end;
	
	#sprintf native
	def str(input)
		if(input.class==nil.class); then
			out="null";
		else
			out=sprintf("%s",input);
		end;
		return(out);
	end;
	
	def is(x);
		"""
			is(defined? varname)
			
			INP:	:varname	variable name
			
			ANS:	Boolean:	exists in local or global scope
			
			
			is(defined? a)	corresponds to	is_defined('a')
		
		"""
		tmp=sprintf("%s",x);
		return(tmp!="");
	end;
	
	def toFloat(inp);
		"
		GENERAL Function
		================
		
		toFloat	converts the first numeric element of the input
				into a Float number and returns it or 0.0.
		"
		
		out=0.0;
		x=sprintf("%s",inp).strip();
		for f in x.split();
			
			begin
				tmp=((Float(f)).class==out.class);
			rescue
				tmp=false;
			end;
			if (tmp) then;
				out=Float(f);
				break;
			end;
		end;
		return(out);
	end;
	
	def toInt(inp);
		"
		GENERAL Function
		================
		toInt 	returns the first numeric element of the input
				converted into an Integer, or 0.
		"
		return(Integer(toFloat(inp)));
	end;
	
	
	def count(input);
		"
		GENERAL Function
		================
		
		Number of elements from an object
		
		
		count(['la','123'])
						returns(2)
						
						
		count('casa')
						returns(4)
		
		"
		return(input.length);
	end;
	
	alias :len	:count;


	
	class XRaise <StandardError
		attr_accessor :message;
		
		def initialize(msg="");
			@message = msg;
		end;
    end;
    
	def xraise(message="Error!");
		raise XRaise.new(message);
	end;
	
	def xrange(*vargs);
		"""
		GENERAL Function
		================
		
		xrange	requires 1 to 3 arguments(
				
		
		xrange(5)
				returns [0, 1, 2, 3, 4]
		
		xrange(2,10)
				returns [2, 3, 4, 5, 6, 7, 8, 9]
				
		xrange(2,10,3)
				returns [2,5,8]
				
		"""
		args=(vargs);
		_step=0;
		_start=0;
		_stopBefore=nil;
		c=count(args);
		case (c)
		
		when 0;
				xraise("TypeError: xrange expected 1 argument, got 0");
				
		when 1;
				_stopBefore=toInt(args[0]);
		when 2;
				_start=toInt(args[0]);
				_stopBefore=toInt(args[1]);
		when 3;
				_start=toInt(args[0]);
				_stopBefore=toInt(args[1]);
				_step=toInt(args[2]);
		else;
				xraise("TypeError: xrange expected at most 3 arguments, got "+c.to_s);
		end;
		
		if((_step>0 and _stopBefore<_start) or (_step<0 and _stopBefore>_start)) then;
			_stopBefore=_start;
		end;
		if(toInt(_step)==0) then;
			_step=1;
		end;
		out=[0];
		
		begin
			out=(_start.._stopBefore).step(_step).to_a;
		rescue
		end;
		if (out[-1]==_stopBefore) then;
			out.pop();
		end;
		return(out);
	end;
	
	def popLast(*input);
		out=*input[0].pop(1);
		return(out[0]);
	end;
	
	def pushLast(where,what);
		where.append(what);
		return(where.length);
	end;
	
	def popFirst(*input);
		out=*input[0].shift(1);
		return(out);
	end;
	
	def pushFirst(where,what);
		where.unshift(what);
		return(where.length);
	end;

	def isString(obj);
		 return(typeOf(obj)=="string");
	end;

	def isInteger(obj);
		 return(typeOf(obj)=="integer");
	end;

	def isFloat(obj);
		 return(typeOf(obj)=="float");
	end;

	def isNumeric(obj);
		 return(isFloat(obj) or isInteger(obj));
	end;

	def isList(obj);
		return(typeOf(obj)=="list");
	end;

	def isDict(obj);
		return(typeOf(obj)=="dict");
	end;

	def isIn(what,where);
		return(where.include?(what));
	end;


	def typeOf(input);
		out=str(input.class).downcase;
		if(isIn(out,CORRECT_TYPES)) then
			out=CORRECT_TYPES[out];
		end;
		return(sprintf("%s",out));
	end;
end;

	
def main(*argv);
	include Alias_H;

	echo (APP+LOADED);
	echo is(defined? APP);
	echo (xrange(5));
	echo (xrange(2,10));
	echo (xrange(2,10,3));
	echo ("La casa roja");
	a=List(1,2,3);
	echo(popLast(a));
	echo(popLast(a));
	echo(a);
	echo(typeOf(a));
end;

if caller.length==0 then	#main file
	main(ARGV);
end;
