#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def hfilter(s):
	hangle = re.compile('[^ㄱ-ㅣ0-9가-힣]+')
	return hangle.sub('', s)
	
def movename(s):
	req = requests.get('https://movie.naver.com/movie/bi/mi/scriptAndRelate.nhn?code='+s)
	soup = BeautifulSoup(req.content, 'html.parser')
	name = soup.find('h3',class_="h_movie")
	p=[]
	text = hfilter(name.get_text())
	p.append(text)
	
	p1=p[0][:-4]
	
	if (p1[len(p1)-1]==p1[len(p1)-2]):
		p1=p1[:-1]
	p[0]=p1
	
	return p
	
if __name__ == '__main__':

	print(movename('10003'))
	
	
	
