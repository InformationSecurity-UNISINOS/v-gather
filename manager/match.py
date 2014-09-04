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

	print "[>] MatchData->total_cases: %i" %total_cases
	# ok, criar loop pra recuberar cada caso da base
	case_id=1
	qlen=CountQueue()
	while case_id <= total_cases:
		db_case={}
		db_case=GetCase(case_id)
		print db_case
		

	# pega primeiro caso da base

	# agora receber a queue dos dados enviados pelo agente

	# pega primeiro processo da queue

	# comparar atributos





