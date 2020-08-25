#!/usr/bin/ruby -W0
#
#  string_h.rb
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
include Alias_H

module String_H
	def array(*vargs);
		args=(vargs);
		res=[];
		for a in args;
			res.append(a);
		end;
		return(res);
	end;

	

	def toUpper(string)
		return(str(string).upcase);
	end;
	
	def toLower(string)
		return(str(string).downcase);
	end;
	
	def toCaps(string);
		return(str(string).capitalize);
	end;
	
	def split(*vargs);#delimiter=" ",string="",limit=null
		args=(vargs);
		out=[];
		if(len(args)==1) then
			out=args[0].split();
		elsif(len(args)==2) then
			out=args[1].split(args[0]);
		elsif(len(args)==3) then
			out=args[1].split(args[0],args[2]);
		end;
		return(out);
	end;
	
	def join(*vargs);#delimiter=" ",string=""
		out="";
		args=(vargs);
		if(len(args)==1) then
			out=args[0].join(" ");
		elsif(len(args)==2) then
			out=args[1].join(args[0]);
		end;
		return(out);
	end;
	
	def toTitle(string);
		a=[];
		for f in split(" ",string);
			a.append(toCaps(f));
		end;
		return(join(a));
	end;
	def endsWith(text,endWith="");
		return(text.end_with? endWith);
	end;
	def basename(path,endWith="");
		return(File.basename(path,endWith));
	end;
	def dirname(path);
		return(File.dirname(path));
	end;

	def allTrim(string);
		tmp=str(string);
		return(tmp.strip());
	end;

	def lTrim(string);
		tmp=str(string);
		return(tmp.lstrip());
	end;

	def rTrim(string);
		tmp=str(string);
		return(tmp.rstrip());
	end;

	def abs(x);
		cond=
			begin
				x<0
			rescue
				true;
			end;
		if(cond) then;
			out=-x;
		else
			out=x;
		end;
		return(out);
	end;
	
	def left(string,nChars);
		out=str(string);
		n=abs(nChars);
		if (n>0) then;
			out=out[..(n)];
		else
			out="";
		end;
		return(out);
	end;

	def right(string,nChars);
		out="";
		n=abs(nChars);
		if(n>=len(string)) then;  
			out=str(string);
		elsif (n>0) then;
			out=out[(-n)..];
		end;
		return(out);
	end;

	def substr(string, start, nChars = nil);
		out="";
		if (start < 0) then
			start = start + len(string);
		end;
		nChars=nChars-1;
		if (nChars==nil) then
			out=string[start..];
		elsif (nChars > 0) then
			out=string[start..(start + nChars)];
		else
			out=string[start..nChars];
		end;
		
		return(out);
	end;
	
	


	def tr(string,characters,replacements);
		tmp=		sprintf("%s",string);
		what=		sprintf("%s",characters);
		forwhich=	sprintf("%s",replacements);
		return(tmp.tr(what,forwhich));
	end;

	def tr_d(string,characters);
		what=sprintf("%s",characters);
		return(tr(string,what,''));
	end;


	def rev(string);
		i=string;
		if(typeOf(i)=="string" or typeOf(i)=="list") then;
			o=i.reverse;
		elsif(typeOf(i)=="dict") then;
			o={};
			for f in i.reverse_each;
				o[f[0]]=f[1];
			end;
		else
			o=i;
		end;
		return(o);
	end;

				

	
	def instr(*vargs);
		"""
		instr(n,haystack,needle)
		instr(haystack,needle)
		"""
		out=-1;
		ins="";
		needle="";
		fromChar=0;
		args=(vargs);
		if(len(args)==3) then
			fromChar=0+popFirst(args);
		end;
		if(len(args)==2) then
			haystack=popFirst(args);
			needle=popFirst(args);
			ins=""+haystack[fromChar..];
		end;
		if(isIn(needle,ins)) then
			out=fromChar+ins.index(needle);
		end;
		return(out);
	end;
	
		
	def strtok(string,delimiter=" ");
		return(split(delimiter,string));
	end;
	
		
	alias	:reverse 	:rev;
	alias	:upper		:toUpper;
	alias	:lower		:toLower;
	alias	:count		:len;
	alias	:strrev		:rev;
	alias	:strlen		:len;
	alias	:strpos		:instr;
	alias	:repr		:str;
	alias	:implode	:join;
	alias	:explode	:split;
	alias	:mid		:substr;
end;

if caller.length==0 then;	#main file
	include String_H;
	echo (APP+LOADED);
	echo (version);
	echo (typeOf(ALIAS_H));
	echo (reverse("casa"));
	echo (count("casa"));
	echo (str(nil));
	echo (toTitle("martinez bas"));
	echo (array(1,2,3));
	echo (substr("la casa roja",-5,2));
	echo (substr("la casa roja",0,2));
	echo (rev(CORRECT_TYPES));
end;

