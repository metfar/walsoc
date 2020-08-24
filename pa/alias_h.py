#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
#  alias_h.py
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

import sys;

	
def is_defined(x):
	"""
		is_defined (String)
		
		INP:	String:		variable name
		
		ANS:	Boolean:	exists in local or global scope
		
		
		is_defined("a")		corresponds to		is(defined? a)
	
	"""
	return ((x in locals()) or (x in globals()));

ARGV=sys.argv;

TRUE=true=True;
FALSE=false=False;
NULL=null=none=None;

ALIAS_H=TRUE;

version=sys.version;

APP=ARGV[0];
NAME=APP;
ENTER=enter=LF="\n";
EXCLAMATION="!";
LOADED=" loaded"+EXCLAMATION;

echo=print;
CORRECT_TYPES={
				"str":	"string",
				"int":	"integer",
				"bool":	"boolean"
				};

def main(*argv):
	echo(APP+LOADED);
	echo(is_defined("APP"));
	


if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
