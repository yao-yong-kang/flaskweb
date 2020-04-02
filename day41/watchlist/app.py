import os,sys

from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import click

WIN=sys.platform.startswith('win')
if WIN:
    prefix='sqlite:///'  #windows平台
else:
    prefix='sqlite:////' #mac linux 平台
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



db=SQLAlchemy(app)
#models数据层
class User(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))

class Movie(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(60))
    year=db.Column(db.String(4))


#视图函数
@app.route('/')
def index():
    name='yyk'
    movies=[
        {'title':'奥特曼','year':"2079"},
        {'title':'战狼','year':"2104"},
        {'title':'外星人','year':"9999"},
        {'title':'泰罗奥特曼','year':"2079"},
        {'title':'舒克和贝塔','year':"2079"},
        {'title':'奥特曼','year':"2079"},
        {'title':'奥特曼','year':"2079"},
    ]
    return render_template('index.html',name=name,movies=movies)


#自定义命令
@app.cli.command() #注册为命令
@click.option('--drop',is_flag=True,help='先删除后创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')


    # @app.cli.command()   #注册为命令
    # @click.option('--drop',is_flag=True,help='先删除再创建')
    # def initdb(drop):
    #     if drop:
    #         db.drop_all()
    #     db.create_all()
    #     click.echo('初始化数据库完成')    