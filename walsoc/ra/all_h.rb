#!/usr/bin/ruby 
#
#  all_h.rb
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

def main(*argv);
	echo(APP+LOADED);
	echo is(defined? APP);
	return(0);
end;

if caller.length==0 then	#main file
	main(ARGV);
end;
