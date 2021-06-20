#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from elasticsearch import Elasticsearch

es_host = "127.0.0.1" #elasticsearch data host & port
es_port = "9200"

def moviesearch(searchword):
	counter = 1
	D={}
	es = Elasticsearch([{'host':es_host,'port':es_port}],timeout=30)



    #choose subject, searchword
	subject = "title"
	query = {"query":{"bool":{"must":[{"match":{'title':searchword}}]}}}

	while True:
	        try:
	            docs = es.search(index="movies",body=query,size=100)
	            break
	        except Exeception as e:
	            print(1)
	            continue
	if docs['hits']['total']['value']>0:
		for doc in docs['hits']['hits']:
	            #using data
			#print(doc['_source'])
			D[1]=doc['_source']
			#counter = counter + 1
                        
                        
	else:
		print('no document!')

	return D

if __name__=='__main__':
	moviesearch("빽 투 더 퓨쳐 3      1990")
