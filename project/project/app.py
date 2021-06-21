#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request

app= Flask(__name__)

@app.route('/')
def index():
        return render_template('practice.html')
        
@app.route('/1',methods=['POST'])
def t1():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page1.html',result=result) 
		        
@app.route('/2',methods=['POST'])
def t2():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page2.html',result=result) 
		        
@app.route('/3',methods=['POST'])
def t3():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page3.html',result=result) 
		        
@app.route('/4',methods=['POST'])
def t4():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page4.html',result=result) 
		        
@app.route('/5',methods=['POST'])
def t5():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page5.html',result=result) 
		        
@app.route('/6',methods=['POST'])
def t6():
	if request.method=='POST':
		result = request.form['search']
		return render_template('page6.html',result=result) 
		

if __name__ == '__main__':
	app.run(debug=True)	
