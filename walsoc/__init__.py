#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys;
import os;
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'pa')));
sys.path.append(os.path.abspath(os.path.dirname(__file__)));
#asc,alias,string,enum,math,stdio,set
for f in "alias,all,asc,bgi,colio,ds,enum,html,math,md,set,stdio,string".split(","):
        exec("from .pa."+f+"_h import *;");

