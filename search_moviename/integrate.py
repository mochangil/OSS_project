#!/usr/bin/python3
#-*- coding: utf-8 -*-

import search_moviename

def integrate(s):

	p1=[]
	p2=[]
	p3=[]
	p1=search_moviename.movename(s)
	p2=search_moviename.movietext(s)
	p3=search_moviename.moviechar(s)
#	print(p1)
#	print(p2)
#	print(p3)
	tototal=[p1[0]]
#	print(tototal)
	
	if len(p2)==len(p3):	
		for i in range(0,len(p2)):
			total1=[]
			if p3:
				total1.append(p2[i])
				total1.append(p3[i])
			tototal.append(total1)
		
	print(tototal)
	return tototal
