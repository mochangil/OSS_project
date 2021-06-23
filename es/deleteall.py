#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"

if __name__== '__main__':
    es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)

    es.indices.delete(index='movies')
