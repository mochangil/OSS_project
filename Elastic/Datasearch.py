#!/usr/bin/python3
#-*- coding: utf-8 -*-

import es

if __name__=='__main__':
	D={}
	moviename = input()
	D = es.moviesearch(moviename)
	print(D[1].pop('title'))          #제목
	print(D[1].pop('texts'))          #인덱스로 접근가능한 명대사 리스트
	print(D[1].pop('names'))          #인덱스로 접근가능한 작중인물명, 배우명

