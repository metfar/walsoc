#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
	from .context import *;
except:
	from context import *;

from walsoc import *;
import unittest;

class Tests(unittest.TestCase):

	def test_string(self):
		assert  ("boolean" == typeOf(STRING_H));
		assert  ("asac" == reverse("casa"));
		assert  (4 == count("casa"));
		assert  ("None" == str(null));
		assert  ("Martinez Bas" == toTitle("martinez bas"));
		assert  (" r" == substr("la casa roja",-5,2));
		assert  ("la" == substr("la casa roja",0,2));

	def test_alias(self):
		self.assertEqual(str(xrange(5)),"[0, 1, 2, 3, 4]");
		self.assertEqual(str(xrange(2,10,3)),"[2, 5, 8]");
		a=List(1,2,3);
		self.assertEqual(3,popLast(a));
		self.assertEqual(2,popLast(a));
		self.assertEqual([1],a);
		self.assertEqual("list",typeOf(a));
		self.assertEqual (ascToIntl("¡El murciélago veloz del año comió pingüinos con Garçía!"),"!El murcielago veloz del ano comio pinguinos con Garcia!");

	
	def test_set(self):
		assertEqual=self.assertEqual;
		assertTrue=self.assertTrue;
		assertFalse=self.assertFalse;
		a=set(1,2,13,5,2,7,"casa");
		assertEqual("set",typeOf(a));
		assertEqual(6,len(a));
		assertEqual(str(a),"{1,13,2,5,7,casa}");
		a.remove(2);
		assertEqual(str(a),"{1,13,5,7,casa}");
		a.add("la");
		a.add("Casa","roja");
		assertEqual(a.getContent(),"{1,13,5,7,Casa,casa,la,roja}");
		b=set();
		assertEqual(str(b),"{}");
		assertTrue(set().isEmpty());
		b=set("la","casa");
		assertTrue(a.equals(a));
		assertTrue (b.isStrictSubset(a) );
		assertFalse(a.isSubset(b));
		assertTrue(a.isSuperset(b));
		assertFalse(b.isSuperset(a));
		assertEqual("{1,13,5,7,Casa,casa,la,roja}",str(a.union(b)));
		assertEqual(str(a.intersection(b)),"{casa,la}");
		assertEqual("{1,13,5,7,Casa,roja}",str(a.difference(b)));
		c=set(1,2);
		d=set(2,3,4);
		c.update(d);
		assertEqual(str(c),"{1,2,3,4}");
		c.intersection_update(d);
		assertEqual(str(c),"{2,3,4}");
		c.difference_update(set(2,4));
		assertEqual(str(c),"{3}");
		assertEqual(3,c.pop());
	
	
	def test_stdio(self):	
		a='Something12lacasaroja[1,2]{a:1,b:2}Upsi000001002003004005006007008009file-get-contents(pepe)None-------file-get-contents(tmp.tmp)000/n001/n002/n003/n004/n005/n006/n007/n008/n009/n-------';#rough string
		
		ob_start();
		print_r('Something',[1,2]);
		print_r(["la casa roja",[1,2],{"a":1,"b":2}],"Upsi");
		arch=fopen("tmp.tmp","wt");
		for f in xrange(10):
			fprintf(arch,"%03d\n",f);

		fclose(arch);
		
		arch=fopen("tmp.tmp","rt");
		printf("%s",fread(arch));
		fclose(arch);
		printR("file_get_contents('pepe')",file_get_contents("pepe"),"-------");
		printR("file_get_contents('tmp.tmp')",file_get_contents("tmp.tmp"),"-------");
		rm("tmp.tmp");
		out=str(ob_get_clean());
		self.assertEqual(aGrossoModo(out),aGrossoModo(a));
	
	def test_asc(self):
		self.assertEqual("ñ",chr(164));
		self.assertEqual(164,asc("ñ"));
		self.assertEqual("['L', 'a', ' ', 'c', 'a', 's', 'a', ' ', 'r', 'o', 'j', 'a']",sprintf("%s",toList("La casa roja")));
		self.assertEqual(str(toList({"la":2,"casa":1})),"['la', 'casa']");
		self.assertEqual("?Comio mani?",ascToIntl("¿Comió maní?"));
		
	
	def test_enum(self):
		a='STARTINGRUNNINGRUNNINGSTARTINGRUNNINGPROCESSINGCHECKINGFINISHINGTERMINATED----------Manually----------STARTINGFINISHING----------STARTINGRUNNINGPROCESSINGCHECKINGFINISHINGTERMINATED0';
		STATUS=Enum("STARTING","RUNNING","FINISHED");
		assert( Enum()[1]==Enum().RUNNING);
		ob_start();
		printR(STATUS.name(0));
		
		next(STATUS);
		printR(STATUS);
		printR(STATUS);
		for f in Enum():
			printR(f);

		f=Enum();
		printR("----------");
		printR("Manually");
		printR("----------");
		printR(f);
		f+=4;
		printR(f);
		printR("----------");
		f=Enum();
		while(True):
			printR(f);
			try:
				f.next();
			except StopIteration:
				break;
		printR(f.STARTING);
		out=ob_get_clean();
		self.assertEqual(aGrossoModo(out),aGrossoModo(a));
		
	def test_math(self):
		a="1.57079632679489661.4142135623730951[83,132,255][25,0,0]({black:[0,0,0],red:[159,0,0],green:[0,159,0],yellow:[159,159,0],blue:[0,0,159],magenta:[159,0,159],cyan:[0,159,159],white:[159,159,159],brightblack:[36,36,36],brightred:[189,0,0],brightgreen:[0,189,0],brightyellow:[189,189,0],brightblue:[0,0,189],brightmagenta:[189,0,189],brightcyan:[0,189,189],brightwhite:[189,189,189]})";
		ob_start();
		printR(toRad(90));
		printR(sqr(2));
		printR(str(hexToBList("5384ff")));
		printR(str(decToBList(1638400)));
		printR(str(pal(1)));
		out=ob_get_clean();
		self.assertEqual(aGrossoModo(a),aGrossoModo(out));
		
if __name__ == '__main__':
	unittest.main();

