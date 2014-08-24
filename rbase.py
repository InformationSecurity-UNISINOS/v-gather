#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import pickletools
import common

def DumpBase(data):
    output = open('data.p', 'wb')
    pickle.dump(data, output)
    output.close()

def OpenBase():
    y=[]
    with open('data.p', 'rb') as f:
        y = pickle.load(f)
    return y

def Similarity(string_a,string_b):
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    return fuzz.ratio(string_a,string_b)