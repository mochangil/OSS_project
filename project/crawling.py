#!/usr/bin/python3
#-*- coding: utf-8 -*-

import search_moviename

import re
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def get_key(val,dic):
	for key, value in dic.items():
		if val ==value:
			return key
			
def make_index(es, index_name):
	if es.indices.exists(index=index_name):
		es.indices.delete(index=index_name)
	print(es.indices.create(index=index_name))

def hfilter(s):
	hangle = re.compile('[^ ㄱ-ㅣ0-9가-힣]+')
	return hangle.sub('', s)

if __name__ == '__main__':
	req = requests.get(u'https://movie.naver.com/movie/bi/mi/script.nhn?code=187322&order=best&nid=')
	soup = BeautifulSoup(req.content, 'html.parser')
	daesa = soup.find_all('p',class_="one_line")
	sanghwang = soup.find_all('p',class_="line_desc")
	charter = soup.find_all('p',class_="char_part")
	
	search_moviename.movename('187322')
	p1=[]
	p2=[]
	p3=[]
	dic = {}
	for list1 in daesa:
		text = hfilter(list1.get_text())
		arr = text.split()
		p1.append(text)

#	for list2 in sanghwang:
#		text2 = hfilter(list2.get_text())
#		arr2 = text2.split()
#		p2.append(text2)
#		print(text2)
#	print(p2)

	for list3 in charter:
		text3 = hfilter(list3.get_text())
		arr3 = text3.split()
		p3.append(text3)
	
	
	tototal=[]
	for i in range(0,10):
		total1=[]
		total1.append(p1[i])
		total1.append(p3[i])
		tototal.append(total1)
	print(tototal)
	
