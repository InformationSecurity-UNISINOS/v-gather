#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import pickletools
import common
    




def Similarity(string_a,string_b):
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    return fuzz.ratio(string_a,string_b)