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
	
	null=Null=NULL=NONE=None=nil;
	True=TRUE=true;
	False=false;
	ENTER=enter=LF="\n";
	EXCLAMATION="!";
	LOADED=" loaded"+EXCLAMATION;
	RUBYOPT="-W0";
	ALIAS_H=TRUE;
	APP=$0;
	PROCID=$$;
	FS=File::SEPARATOR;
	CORRECT_TYPES={
				"array"=>		"list",
				"hash"=>		"dict",
				"trueclass"=>	"boolean",
				"falseclass"=>	"boolean"
				};
	
	
	def version;
		return(RUBY_VERSION);
	end;
	
	def echo(*content);
		print(*content);
		print(ENTER);
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
	
end;

	
def main(*argv);
	include Alias_H;

	echo (APP+LOADED);
	echo is(defined? APP);
	
	
end;

if caller.length==0 then	#main file
	main(ARGV);
end;
