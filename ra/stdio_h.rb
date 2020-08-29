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
		if(File.exist? (name) and File.lstat(name).symlink?)	then;
			tmp=File.readlink(name);
			return(tmp);
		else;
			return(null);
		end;
	end;
	def linkExists(name);
		"""
		File Functions
		--------------
		
		linkExists('/tmp')
				returns true if it exists and target too
		"""
		if(File.exist? (name)) then;
			tmp=readlink(name);
			return(exists(tmp));
		else;
			return(false);
		end;
	end;
	
	def exists(name);
		"""
		File Functions
		--------------
		
		exists('/tmp')
				returns true if it exists as file/dir/link
		"""
		if 		(name==nil)	then;
				return(false);
			
		elsif 	(fileExists(name))	then;
				return(true);
				
		elsif 	(dirExists(name))	then;
				return(true);
				
		elsif 	(File.exist?(name) and File.lstat(name).symlink?)	then;
				return(true);
		else;
				return(false);
		end;
	end;


	def file_get_contents(url);
		"""
		File Functions
		--------------
		
		file_get_contents('https://www.google.com/index.html')
		or
		file_get_contents('/tmp/myFile.txt')
		
		
		"""
		out=nil;
		if	(url.start_with?("http:")) then;
			begin
				out=Net::HTTP.get_response(URI.parse(name)).body;
			rescue
			end;
		elsif(url.start_with?("https:")) then;
			begin
				out=Net::HTTP.get_response(URI.parse(name)).body;
			rescue
			end;
		elsif(exists(url)) then;
			begin
				tmp=fopen(url,"r");
				out=tmp.read();
				fclose(tmp);
			rescue
			end;
		end;
		return(out);
	
	end;

	def	rm (name);
		"""
		File Functions
		--------------
		
		rm('/tmp/myFile.txt')
				if it deletes the file, it will return true
		
		"""
		if(fileExists(name)) then;
			begin
				if(File.unlink(name)) then;
					return(true);
				else;
					return(false);
				end;
			rescue
			end;
		end;
		return(false);
	end;

	def rmdir(name,force=false);
		"""
		File Functions
		--------------
		
		rmdir('/tmp/dir01')
				if it is an empty directory,
				and it is being removed, it will return true
				
		rmdir('/tmp/dir01',true)
				if it is being removed, empty or not,
				it will return true
		
		"""
		if(dirExists(name)) then;
			begin
				if(Dir.rmdir(name)==0) then;
					return(true);
				else;
					return(false);
				end;
			rescue Errno::ENOTEMPTY, Errno::ENOENT
				if(!force) then;
					return(false);
				else;
					begin;
						FileUtils.remove_dir(name,true);
					rescue;
					end;
				end;
			end;
		end;
		return(false);
	end;

	def mkdir(name);
		"""
		File Functions
		--------------
		
		mkdir('tmp')
						makes directory tmp
		"""
		begin
			return(0==Dir.mkdir(name));
		rescue
			return(false);
		end;
	end;
	
	def chdir(name);
		"""
		File Functions
		--------------
		
		chdir('tmp')
						change directory to tmp
		"""
		begin
			if(0==Dir.chdir(name)) then;
				return(true);
			end;
		rescue;
		end;
		return(false);
	end;

	def ls(dirname=".",contains="",startsWith="",endsWith="");
		"""
		File Functions
		--------------
		
		ls(dirname='tmp')
						returns the ls of directory tmp
		ls(dirname='tmp',contains='a')
						list files/directories in tmp containing a
		ls(dirname='tmp',contains='a',startsWith='n',endsWith='py')
						list files/directories in tmp with all conditions
						
		
		
		"""
		begin
			o=Dir.entries(dirname);
		rescue
			o=[];
		end;
		out=[];
		for f in o;
			add=true;
			if(len(contains)>0 and not(f.include? contains)) then;
				add=false;
			end;
			if(len(startsWith)>0 and not(f.start_with?(startsWith))) then;
				add=false;
			end;
			if(len(contains)>0 and not(f.end_with(endsWith))) then;
				add=false;
			end;
			if(add) then;
				if(f!=".." and f!=".")	then;
					out.append(f);
				end;
			end;
		end;
		return(out);
	end;
	
	def touch(name);
		"""
		File Functions
		--------------
		
		touch('file.txt')
		
		"""
		begin
			FileUtils.touch(name);
			return(true);
		rescue
			return(false);
		end;
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
	
	printR("file_get_contents('pepe')",file_get_contents("pepe"),'------');
	printR("file_get_contents('tmp.tmp')",file_get_contents("tmp.tmp").split("\n").join(" "),'------');
	rm("tmp.tmp");
	printR(ls());
	exit(0);
end;
