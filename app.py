#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request
import es
import search_moviename

count=1
counter = 0

for i in range(10002,10005):
        total = search_moviename.integrate(str(i))
        es.inputmovie(total,count)
        count = count+1

#추가된 함수
def divwords(wordlist,start):
	words = []
	i = 0
	for i in range(5):
		words.append(wordlist[start+i])
	return words

def Movsearch(movname):
	D={}
	moviename = movname
	D = es.moviesearch(moviename)
	if D==0:
	        return 0
	else:
	        return D

app= Flask(__name__)

@app.route('/')
def index():
        return render_template('practice.html')
        
@app.route('/1',methods=['POST'])
def t1():
	if request.method=='POST':
		words_text = []
		words_name = []
		result = request.form['search']
		D=Movsearch(result)
		lists_text = D[1].pop('texts')
		lists_name = D[1].pop('names')
		global resultnum
		resultnum=len(lists_text)
		
		wordt = divwords(lists_text,0)
		wordn = divwords(lists_name,0)
		if D==0:
			return render_template('errorpage.html')
		else:
			return render_template('page1.html',result=result,title=D[1].pop('title'),text=wordt,name=wordn) 		        
@app.route('/2',methods=['POST'])
def t2():
	words_text = []
	words_name = []
	result = request.form['search']
	D=Movsearch(result)
	lists_text = D[1].pop('texts')
	lists_name = D[1].pop('names')
		
	wordt = divwords(lists_text,5)
	wordn = divwords(lists_name,5)
	if D==0:
		return render_template('errorpage.html')
	elif resultnum<=5:
		return render_template('errorpage.html')
	else:
		return render_template('page2.html',result=result,title=D[1].pop('title'),text=wordt,name=wordn)
\
if __name__ == '__main__':
	app.run(debug=True)	
