#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def hfilter(s):
	hangle = re.compile('[^ a-zA-Zㄱ-ㅣ0-9가-힣]+')
	return hangle.sub('', s)
	
def movietext(s):
	req = requests.get(u'https://movie.naver.com/movie/bi/mi/script.nhn?code='+s+'&order=best&nid=')
	soup = BeautifulSoup(req.content, 'html.parser')
	daesa = soup.find_all('p',class_="one_line")
	p=[]
	
	for list1 in daesa:
		text = hfilter(list1.get_text())
		p.append(text)
		
#	print(p)
	return p
