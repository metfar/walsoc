#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys;
import os;
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'pa')));
for f in "asc,alias,string,enum,math,stdio,set".split(","):
        exec("from .pa."+f+"_h import *;");

