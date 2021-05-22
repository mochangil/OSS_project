from flask import Flask
from flask import render_template
from flask import redirect, url_for

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('page1.html') 
@app.route('/2')
def t2():
	return render_template('page2.html')
@app.route('/3')
def t3():
	return render_template('page3.html')
@app.route('/4')
def t4():
	return render_template('page4.html')
@app.route('/5')
def t5():
	return render_template('page5.html')
@app.route('/6')
def t6():
	return render_template('page6.html')
@app.route('/7')
def t7():
	return render_template('page7.html')
if __name__ == '__main__':
	app.run(debug=True)	
