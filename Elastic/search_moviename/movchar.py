#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def hfilter(s):
	hangle = re.compile('[^ ㄱ-ㅣ0-9가-힣]+')
	return hangle.sub('', s)
	
def moviechar(s):
	req = requests.get(u'https://movie.naver.com/movie/bi/mi/script.nhn?code='+s+'&order=best&nid=')
	soup = BeautifulSoup(req.content, 'html.parser')
	charter = soup.find_all('p',class_="char_part")
	p=[]
	
	for list1 in charter:
		text = hfilter(list1.get_text())
		p.append(text)		
#	print(p)
	return p
	
	
