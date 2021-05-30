#!/usr/bin/python3
#-*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup as soups
from flask import Flask, jsonify
from flask import render_template
from flask import redirect, url_for
from flask import request
from selenium import webdriver
from bs4 import BeautifulSoup as soups
import mypkg

def search_selenium(search_name, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    browser = webdriver.Chrome('/home/mochangil/chrome/chromedriver') #chromedriver directory 
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    
    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    for i in range( search_limit ) :
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("/home/mochangil/project/templates/" + str(i) + ".png") #img save path

    browser.close()

app= Flask(__name__)

@app.route('/1',methods=['POST'])
def t1():
    mywords = str(request.form['words'])
    search_selenium(mywords,5)
    return render_template('page1.html',title=mywords)
@app.route('/2',methods=['POST'])
def t2():
    mywords = str(request.form['words'])
    return render_template('page2.html',title=mywords)
@app.route('/',methods=['GET'])
def index():
    return render_template('homepage.html')


#@app.route('/3')
#def t3():
#	return render_template('page3.html')
#@app.route('/4')
#def t4():
#	return render_template('page4.html')
#@app.route('/5')
#def t5():
#	return render_template('page5.html')
#@app.route('/6')
#def t6():
#	return render_template('page6.html')
#@app.route('/7')
#def t7():
#	return render_template('page7.html')

if __name__ == '__main__':
    app.run(debug=True)	
