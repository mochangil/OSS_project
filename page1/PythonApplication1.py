from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/search')
def quote_search() ->'html':
    return render_template('page1.html')
@app.route('/resultpage')
def search_result()->'html':
    title=request.form['title']
    quote=request.form['quote']
    director=request.form['director']
    actor=request.form['actor']
    character=request.form['character']

app.run()