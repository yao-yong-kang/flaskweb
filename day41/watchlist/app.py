from flask import Flask,url_for,render_template

app=Flask(__name__)

@app.route('/')
def index():
    name='yyk'
    movies=[
        {'title':'奥特曼','year':"2079"},
        {'title':'战狼','year':"2104"},
        {'title':'外星人','year':"9999"},
        {'title':'泰罗奥特曼','year':"2079"},
        {'title':'奥特曼','year':"2079"},
        {'title':'奥特曼','year':"2079"},
        {'title':'奥特曼','year':"2079"},
    ]
    return render_template('index.html',name=name,movies=movies)