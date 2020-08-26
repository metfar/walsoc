#!/usr/bin/ruby 
#
#  stdio_h.rb
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
require "./string_h";

import "pp";
import 'stringio';
require 'net/http';
require 'net/https';
require 'net/ftp';

$ORIG_STDOUT=$stdout;
$ORIG_STDERR=$stderr;
$ORIG_STDIN=$stdin;
$SEP=" ";
$TB=2;
$TAB=$SEP*$TB;
$LF="\n";
module Stdio_H
	def ob_start();
		$old_stdout = $stdout;
		$tmp_stdout=StringIO.new;
		$stdout=$tmp_stdout;
		
	end;
	def ob_clean();
		$stdout=$old_stdout;
		$tmp_stdout=StringIO.new;
		$stdout=$tmp_stdout;
	end;
	
	def ob_end();
		$stdout=$old_stdout;
	end;
	
	def ob_end_clean();
		$tmp_stdout=StringIO.new;
		$stdout=$old_stdout;
	end;
	
	def ob_get_contents();
		out=$tmp_stdout.string;
		return(out);
	end;
	
	def ob_get_clean();
		out=ob_get_contents();
		ob_end_clean();
		return(out);
	end;
	def printR(*vargs);
		'''
		printR 
				Prints out mixed type data, similar to php-print_r.
		
		printR("Something",[1,2])
				
				returns
						"Something"
						  1
						  2
		
		print_r(["la casa roja",[1,2],{"a":1,"b":2}],"Upsi")
		
				returns
						"la casa roja"
						  [1, 2]
						  {:a=>1, :b=>2}
						"Upsi"
				
		'''
		args=(vargs);
		ob_start();
		for a in args;
			if(typeOf(a)=="list" or typeOf(a)=="dict");
				for f in a;
					print($TAB);
					pp(f);
				end;
			else;
				pp(a);
			end;
		end;
		out=ob_get_clean();
		
		#$stdout = old_stdout;
		#out=out.string;
		if(len(out)>len($SEP) and out[-len($SEP)]==$SEP) then;
			out=out[..-len($SEP)];
		end;
		print(out+$LF);
		return(out);
	end;

	def fopen(filename,mode);
		""" 
		File Functions
		==== =========
		
		fopen (filename,mode)
						 returns pointer to file
		
		Filename 	Path and filename
		
		MODE
		-----
		r - Read 
		a - Append 
		w - Write 
		x - Create - returns error if the file exist
		t - Text
		b - Binary

			
		Example:
		========
		fp = fopen('date.txt', 'wt')

		"""
		return(File.open(filename, mode));
	end;
	
	def fclose(handle);
		""" 
		File Functions
		==== =========
		
		fclose (FilePointer) 
		
		Example:
		========
		
		fclose(fp);

		"""
		handle.close();
	end;

	def fprintf(*vargs);
		""" 
		File Functions
		--------------

		fprintf (FilePointer, FORMAT [,arg1,arg2,...])

		FilePointer

		FORMAT
		%d	integer with sign
		%i	integer with sign
		%u	unsigned int
		%o	octal
		%x	hexadecimal lowercase
		%X	hexadecimal uppercase
		%f	floating point
		%lf	double float
		%e 	scientific notation lowercase
		%E 	scientific notation upppercase
		%c 	character
		%s 	string


		Example:
		========

		fprintf C-Style function 



		"""
		args=(vargs);
		begin
			arch=popFirst(args);
			format=popFirst(args);
			out=format % args;
			arch.write(out);
		rescue
			xraise("Error on fprintf!");
		end;
	end;

	#printf native
	
	def fread(fp,length=nil);
		"""
		File Functions
		--------------
		
		buffer = fread(fp,c);
		
		Equivalent in C-language to: fread(buffer, 1, strlen(c), fp);
		
		
		"""
		if(length==nil) then;
			begin
				return(fp.read(length));
			rescue
				return(nil);
			end;
		else;
			begin
				return(fp.read(length));
			rescue
				return(null);
			end;
		end;
	end;

	def dirExists(name);
		"""
		File Functions
		--------------
		
		dirExists('/tmp')
				returns true if it exists and it is a directory
		"""
		return(File.directory?(name));
	end;
	
	def fileExists(name);
		"""
		File Functions
		--------------
		
		fileExists('/tmp')
				returns true if it exists and it is not a directory
		"""
		return((!dirExists(name)) and File.exist?(name));
	end;


	def readlink(name);
		"""
		File Functions
		--------------
		readlink('/home/user/tmp.tmp')
		
				returns target name if it has or null
		""" 
		if(os.path.islink(name)):
			tmp=os.readlink(name);
			return(tmp);
		else:
			return(null);
			
	def linkExists(name):
		"""
		File Functions
		--------------
		
		linkExists('/tmp')
				returns true if it exists and target too
		"""
		if(os.path.islink(name)):
			tmp=os.readlink(name);
			return(exists(tmp));
		else:
			return(false);
	
	def exists(name):
		"""
		File Functions
		--------------
		
		exists('/tmp')
				returns true if it exists as file/dir/link
		"""
		if 		(name==null):
				return(false);
				
		elif 	(fileExists(name)):
				return(true);
				
		elif 	(dirExists(name)):
				return(true);
				
		elif 	(os.path.islink(name)):
				return(true);
		else:
				return(false);

	def file_get_contents(url);
		if	(url.starts_with?("http:")) then;
			out=Net::HTTP.get_response(URI.parse(name)).body;
		elsif(url.starts_with?("https:")) then;
			out=Net::HTTP.get_response(URI.parse(name)).body;
		elsif(exists(name)) then;
			tmp=fopen(name,"r");
			out=tmp.read();
			fclose(tmp);
		else;
			out=null;
		return(out);
	
	end;

	alias 	:print_r	:printR;
end;
	
	


include Stdio_H;

if (caller.length==0) then;	#main file
	print_r('Something',[1,2]);
	print_r(["la casa roja",[1,2],{"a":1,"b":2}],"Upsi");
	arch=fopen("tmp.tmp","wt");
	for f in xrange(10);
		fprintf(arch,"%03d\n",f);
	end;
	fclose(arch);
	
	
	arch=fopen("tmp.tmp","rt");
	printf("%s",fread(arch));
	fclose(arch);
	
	printR("file_get_contents('pepe')",file_get_contents("pepe"));
	exit(0);
end;
