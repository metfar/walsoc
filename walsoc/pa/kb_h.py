#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kb_h.py
#  
#  Copyright 2020 wmartinez <metfar@gmail.com>
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

from asc_h import *;

try:
    import msvcrt;
    OS="nt";
except:
    OS="x";
    import sys,termios,atexit;
    from select import select;

import threading; #generate thread
import time, traceback;#manage time events;


if (OS=='x'):
    LEFT_ARR,RIGHT_ARR,UP_ARR,DOWN_ARR=68,67,65,66;
else:
    LEFT_ARR,RIGHT_ARR,UP_ARR,DOWN_ARR=75,77,72,80;

def asc(cha=""):
    if(len(cha)>1):
        cha=cha[0];
    return(ASC.index(cha) if(cha in ASC) else 0);

def substi(inString=""):
    substi="ÀÈÌÒÙẀỲǸÂÊÎÔÛŴŶÁÉÍÓÚẂÝŃÄËÏÖÜẄŸÑÇàèìòùẁỳǹâêîôûŵŷáéíóúẃýńäëïöüẅÿñç";
    substo="AEIOUWYNAEIOUWYAEIOUWYNAEIOUWYNCaeiouwynaeiouwyaeiouwynaeiouwync";
    out="";
    for f in inString:
        cha=f;
        if f in susti:
            try:
                cha=substo[substi.index(cha)];
            except:
                pass;
        try:
            out+=str(cha);
        except:
            pass;
    return(out);

def chr(number):
    try:
        return(ASC[int(number)% len(ASC)]);
    except:
        return(ASC[0]);
#for f in range(255,24000):
#    if(str(chr(f)) not in ASC):
#        #print(f,"=",str(chr(f)));
#        ASC.append(str(chr(f)));

#print(len(ASC));
#from pprint import pprint;
#pprint(ASC);
#print(asc("Á"));

#exit(1);
FinishIT=False;
def recursive(task,seconds):
    ntime = time.time() + seconds;
    while not FinishIT:
        time.sleep(max(0, ntime - time.time()));
        try:
            task();
        except Exception:
            traceback.print_exc();#error time
        
        ntime += (time.time() - ntime);



class KBHit:
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''
        if (OS=="x"):
            # Save the terminal settings
            self.fd = sys.stdin.fileno();
            self.new_term = termios.tcgetattr(self.fd);
            self.old_term = termios.tcgetattr(self.fd);

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO);
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term);

            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term);


    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''
        global FinishIT;
        if (OS == 'x'):
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term);
        FinishIT=True;
        #sys.exit(0);


    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''
        s = '';
        if (OS != 'x'):
            a=msvcrt.getch();
            try:
                a=a.decode('utf-8');
                a=a+"\t"+str(ord(a));
            except:
                if(len(a)>1):
                    flg=1;
                    a=a[-1];
                else:
                    flg=0;
                n=ord(a);
                if(n==177):
                    n=164;
                a=ASC[n];
                if(flg==1):
                    a=ASC[0]+a;
                a=a+"\t"+str(n);
            return (a);
        else:
            return (sys.stdin.read(1));




    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if (OS != 'x'):
            return (msvcrt.kbhit());
        else:
            dr,dw,de = select([sys.stdin], [], [], 0);
            return (dr != []);


kb = KBHit();
getch=kb.getch;
kbhit=kb.kbhit;
    
KEYBUFFER=[];

class KT:
    """
    Key_Time class
    
    """
    def __init__(self,Key="",Time=-1):
        self.Time=Time;
        self.Key=Key;
    def setTime(self,Time=-1):
        self.Time=Time;
    def setKey(self,Key=""):
        self.Key=Key;
    
    
    def get(self,Key="",Time=-1):
        return([self.Key,self.Time]);
    
    def set(self,Key="",Time=-1):
        self.Time=Time;
        self.Key=Key;
    
    def __str__(self):
        return(self.Key);
    
LASTTIME=-1;
def inkey():
    global KEYBUFFER,LASTTIME;
    out="";
    if (len(KEYBUFFER)>0):
        tmp=KEYBUFFER.pop(0);
        out=tmp.Key;
        if(out==SOFT_ESCAPE):
            out="";
        LASTTIME=tmp.Time;
    else:
        LASTTIME=time.time();
    
    return(out);

def newKey(laKey,leTime):
    global KEYBUFFER,LASTTIME,LSTKY;
    LSTKY=KT(laKey,leTime);
    KEYBUFFER.append(LSTKY);

def lastKey():
    if(len(KEYBUFFER)<1):
        return(KT());
    else:
        return(KEYBUFFER[len(KEYBUFFER)-1]);


from pprint import pprint;
def clearBuffer(Time):
    flg=False;
    while(not flg):
        if(len(KEYBUFFER)<1):
            flg=True;
        else:
            try:
                if (KEYBUFFER[0].Time<Time):
                    KEYBUFFER.pop(0);
            except:
                
                pass;


def clearLastKey():
    global KEYBUFFER;
    try:
        KEYBUFFER.pop(len(KEYBUFFER)-1);
    except:
        pass;

def readKey():
    Time=time.time();
    #clearBuffer(Time-10);#clear keys if a second passed and it was not processed
    
    out="";
    if (kbhit()):
        c = kb.getch();
        act=ord(c[0]);
        f=0;
        if (act==9):
            newKey(RIGHT_TAB,Time);
            f=1;
        elif(act==27):
            newKey(SOFT_ESCAPE,Time);
            last=act;
            c = kb.getch();
            act=ord(c[0]);
            f=1;
        if(act==91):
            c = kb.getch();
            act=ord(c[0]);
            f=1;
            if(act==LEFT_ARR):
                newKey(LEFT_ARROW,Time);
            elif(act==RIGHT_ARR):
                newKey(RIGHT_ARROW,Time);
            elif(act==UP_ARR):
                newKey(UP_ARROW,Time);
            elif(act==DOWN_ARR):
                newKey(DOWN_ARROW,Time);
            else:
                if(ord(c)==50):
                    newKey(INSERT,Time);
                elif(ord(c)==51):
                    newKey(DELETE,Time);
                elif(ord(c)==72):
                    newKey(HOME,Time);
                elif(ord(c)==70):
                    newKey(END,Time);
                elif(ord(c)==53):
                    newKey(PAGE_UP,Time);
                elif(ord(c)==54):
                    newKey(PAGE_DOWN,Time);
                elif(ord(c)==90):
                    newKey(LEFT_TAB,Time);
                else:
                    newKey(c,Time);
            
        tmp=lastKey();
        
        if (act==27 or tmp.Key==SOFT_ESCAPE):
            newKey(ESCAPE,Time);
            
        if(f!=1 and ord(c)!=126):#sacrifico el 126
            newKey(c,Time);
        

READKEY=threading.Thread(target=lambda: recursive(readKey,.25));

def AtExit():
    global kb;
    kb.set_normal_term();
    sys.exit(1);

def Exit(n=0):
    global kb;
    global FinishIT;
        
    kb.set_normal_term();
    FinishIT=True;
    sys.exit(n);

def AtStart():
    global kb;
    
    atexit.register(kb.set_normal_term);
    READKEY.start();


# Test
if __name__ == "__main__":
    AtStart();
    print('Press double ESC to exit or any key to be shown');
    while True:
        ap=inkey();
        if(ap==ESCAPE):
            Exit();
        elif(ap!=""):
            print(ap);
    
    
