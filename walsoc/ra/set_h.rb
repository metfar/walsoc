#!/usr/bin/ruby 
#
#  set_h.rb
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
for f in "asc,alias,string,enum,math,stdio,set".split(",");
	eval("require './"+f+"_h';");
end;

module Set_H
	$SETSEP=",";
	$SETINIT="{";
	$SETEND="}";

	class Set
		def initialize(*vargs);
			@content=[];
			args=(vargs);
			out=false;
			for f in args;
				if(not @content.include? f) then;
					@content.append(f);
					out=true;
				end;
			end;
			
			if(out) then;
				begin
					@content=@content.sort();
				rescue
					out=[];
					for f in @content;
						out.append(str(f));
					end;
					@content=out.sort();
				end;
			end;
		end;
		
		def add(*vargs);
			args=vargs[0];
			if(args.class.to_s!="Array") then;
				args=vargs;
			end;
			out=false;
			for f in args;
				if(not @content.include? f) then;
					@content.append(f);
					out=true;
				end;
			end;
			if(out) then;
				begin
					@content=@content.sort();
				rescue
					out=[];
					for f in @content;
						out.append(str(f));
					end;
					@content=out.sort();
				end;
			end;
		end;
		
		def includes(x);
			return(@content.include? x);
		end;
		def getContent();
			out=$SETINIT;
			flg=false;
			for f in @content;
				if(flg) then;
					out+=$SETSEP;
				else;
					flg=true;
				end;
				out+=str(f);
			end;
			out+=$SETEND;
			return(out);
		end;
		
		def to_a();
			out=@content;
			return(out);
		end;
		
		def to_s();
			return(getContent);
		end;
		def length;
			return(@content.length);
		end;
		
		def remove(x);
			out=@content;
			if(@content.include? x) then;
				out.delete_at(out.index(x));
			elsif(@content.include? str(x)) then;
				out.delete_at(out.index(str(x)));
			else;
				xraise("KeyError: "+str(x));
			end;
			@content=out.sort();
		end;
		def discard(x);
			if(@content.include?(x)) then;
				remove(x);
				return(true);
			else;
				return(false);
			end;
		end;
		
		def clear();
			begin
				@content=[];
				return(true);
			rescue
				return(false);
			end;
		end;
		
		def isSubset(t);
			out=true;
			for f in @content;
				if(not t.includes(f)) then;
					out=false;
					break;
				end;
			end;
			return(out);
		end;
		
		def isSuperset(t);
			out=true;
			for f in t.to_a();
				if(not includes(f)) then;
					out=false;
					break;
				end;
			end;
			return(out);
		end;
		
		def copy();
			out=Set.new();
			for f in @content;
				if(not out.includes(f)) then;
					out.add(f);
				end;
			end;
			return(out);
		end;
		
		def union(t);
			out=copy();
			for f in t.to_a();
				if(not (out.includes(f))) then;
					out.add(f);
				end;
			end;
			return(out);
		end;
		
		def difference(t);
			out=copy();
			toTake=t.to_a();
			for f in toTake;
				if(out.includes(f)) then;
					out.remove(f);
				end;
			end;
			return(out);
		end;
		
		def sub(t);
			return(difference(t));
		end;
		
		
		
		def intersection(t);
			out=Set.new();
			for f in t.to_a();
				if(includes(f)) then;
					out.add(f);
				end;
			end;
			return(out);
		end;
		
		def symmetric_difference(t);
			out=union(t);
			dif=intersection(t);
			for f in dif.to_a();
				out.remove(f);
			end;
			return(out);
		end;
		
		def isEmpty();
			return(len(@content)<1);
		end;
		
		def equals(t);
			a=intersection(t);
			return(a.length==t.length and a.length==length());
		end;
		
		def isStrictSubset(t);
			return(isSubset(t) && (not equals(t)));
		end;
		
		def update(t);
			out=copy();
			for f in t.to_a();
				if(not out.includes(f)) then;
					out.add(f);
				end;
			end;
			@content=out.to_a();
			return(out);
		end;
		
		def intersection_update(t);
			out=Set.new();
			for f in t.to_a();
				if(self.includes(f)) then;
					out.add(f);
				end;
			end;
			@content=out.to_a();
			return(out);
		end;
		
		def difference_update(t);
			o=difference(t);
			@content=o.to_a();
			return(@content);
		end;
		
		def symmetric_difference_update(t);
			o=symmetric_difference(t);
			@content=o.to_a();
			return(@content);
		end;
		
		def pop();
			if(length()<1) then;
				print("KeyError: ");
				return(nil);
			else;
				o=@content[-1];
				discard(o);
				return(o);
			end;
		end;
	end;

	def set(*vargs);
		out=Set.new();
		out.add(vargs);
		return(out);
	end;
end;
include Set_H;

def main(*argv);
	echo(APP+LOADED);
	echo is(defined? APP);
	a=set(1,2,13,5,2,7,"casa");
	echo(typeOf(a));
	echo(len(a));
	echo(a);
	a.remove(2);
	echo(a);
	a.add("la");
	a.add("Casa","roja");
	echo(a.getContent());
	b=set();
	echo(b);
	echo("A:");
	echo(a);
	b=set("la","casa");
	echo("B:");
	echo(b);
	
	echo("A = A?");
	echo(a.equals(a));
	echo("B ⊂ A?");
	echo (b.isStrictSubset(a) );
	echo("A ⊆ B?");
	echo(a.isSubset(b));
	echo("A is superset of B?");
	echo(a.isSuperset(b));
	echo("B is superset of A?");
	echo(b.isSuperset(a));
	echo("A U B?");
	echo(a.union(b));
	echo("A ∩ B?");
	echo(a.intersection(b));
	echo("A - B?");
	echo(a.difference(b));
	echo("{}=∅ ?");
	echo(set().isEmpty());
	c=set(1,2);
	d=set(2,3,4);
	c.update(d);
	echo(c);
	c.intersection_update(d);
	echo(c);
	c.difference_update(set(2,4));
	echo(c);
	echo(c.pop());
	echo(c.pop());
	echo(typeOf(set()));
	return(0);
end;

if caller.length==0 then	#main file
	main(ARGV);
end;
