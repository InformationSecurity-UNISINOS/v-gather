#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *
from base import *
from cqueue import*

def Similarity(string_a,string_b):
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    return fuzz.ratio(string_a,string_b)


def MatchData():

	# quantos casos tem na base?
	total_cases=SqlCountCases()
	if total_cases == False:
		return False

	# ok, criar loop pra recuberar cada caso da base
	for (case_id=1;case_id <= total_cases;case_id++):
		print "**"*50
		GetCase(case_id)
		print "**"*50
		print GetQueue()
		print "**"*50

	# pega primeiro caso da base

	# agora receber a queue dos dados enviados pelo agente

	# pega primeiro processo da queue

	# comparar atributos





