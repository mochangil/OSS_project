#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from elasticsearch import Elasticsearch

es_host = "127.0.0.1" #elasticsearch data host & port
es_port = "9200"

if __name__ == '__main__':
    es = Elasticsearch([{'host':es_host,'port':es_port}],timeout=30)

    #choose subject, searchword
    subject = "title"
    searchword = "Ironman"
    query = {"query":{"bool":{"must":[{"match":{"title":searchword}}]}}}

    while True:
        try:
            docs = es.search(index="movie",body=query,size=10)
            break
        except Exeception as e:
            print(1)
            continue


    if docs['hits']['total']['value']>0:
        for doc in docs['hits']['hits']:
            #using data

            print(doc['_source'])
