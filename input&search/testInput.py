#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from elasticsearch import Elasticsearch
import re
import requests

es_host="127.0.0.1"
es_port="9200"


D={
        "title":"Ironman",
        "character_name":"Ironman",
        "string":"I am Ironman",
        "actor_name":"Robert"
}

if __name__=='__main__':
    es = Elasticsearch([{'host':es_host, 'port':es_port}],
            timeout=30)
    res = es.index(index='movie', doc_type='movie',id=1,body=D)
    print(res)
