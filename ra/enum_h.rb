#!/usr/bin/ruby 
#
#  enum_h.rb
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



module Enum_H
	class EEnum
		
		def initialize (*argv)
			@names={};
			@actual=nil;
			if(typeOf(argv)=="list") then
				n=0;
				for f in argv
					@names[f]=n;
					n+=1;
				end;
			else
				if (typeOf(argv)=="dict") then
					for f in argv
						@names[f]=argv[f];
					end;
				end;
			end;
			if(@names.length!=0) then
				@actual=@names.first[0];
			end;
		end;
		
		def names;
			out=[];
			for x in @names;
				out.append(x[0]);
			end;
			return(out);
		end;
		def values;
			out=[];
			for x in @names;
				out.append(x[1]);
			end;
			return(out);
		end;
		
		
		def info;
			out=str("names:",@names)+"\t actual:"+str(@actual);
			return(out);
		end;
		
		def to_s;
			if	(@names.length==0) then
				out="";
			else
				if ( ! isIn(@actual,@names)) then
					@actual=@names.first[0];
				end;
				out=@actual;
			end;
			return(out);
		end;
		
		def value;
			return(@names[@actual]);
		end;
		def name;
			return(@actual);
		end;

	end;

	def enum(*argv);
		return(EEnum.new(*argv));
	end;
end;


if caller.length==0 then;	#main file
	include Enum_H
	echo (APP+LOADED);
	STATUS=enum("STARTING","RUNNING","FINISHED");
	echo(STATUS.names());
	echo(STATUS.values());
	echo(STATUS.name());
	echo(STATUS.value());
	echo(Module.included_modules);
end;
