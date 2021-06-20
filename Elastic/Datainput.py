#!/usr/bin/python3
#-*- coding: utf-8 -*-

import es
import search_moviename

if __name__ == '__main__':
    count = 1

#주소의 시작 인덱스, 끝 인덱스
    for i in range(10002,10005):
        total = search_moviename.integrate(str(i))
        es.inputmovie(total,count)
        count = count+1
        	
	
