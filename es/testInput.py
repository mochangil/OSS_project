#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from elasticsearch import Elasticsearch
import re
import requests

es_host="127.0.0.1"
es_port="9200"
        
list1 =["백투더퓨처1519",['미래는 너희들이 만드는 것이란다', '에멧 브라운 박사 크리스토퍼 로이드'],['Nobody calls me Chicken','에멧 브라운 박사 크리스토퍼 로이드'],['여보세요 우여보세요 아무도 없어요','비프 태넌 토마스 윌슨']]
def inputmovie(movieinform,i):
    D={}
    title = movieinform[0]
    movie_text = []
    movie_name = []
    for j in range(1,len(movieinform)):
        movie_text.append(movieinform[j][0])
        movie_name.append(movieinform[j][1])

    D["title"] = title
    D["texts"] = movie_text
    D["names"] = movie_name

    es = Elasticsearch([{'host':es_host, 'port':es_port}],
        timeout=30)
    res = es.index(index='movies', doc_type='movie',id=i,body=D)
#    print(res) #입력값 출력 테스트



if __name__=='__main__':
     inputmovie(list1,4)


