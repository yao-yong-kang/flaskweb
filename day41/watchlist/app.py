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

    user=User.query.first() #查询出来用户记录
    movie=Movie.query.all()
    return render_template('index.html',user=user,movies=movie)


#自定义命令
#建立空数据库
@app.cli.command() #注册为命令
@click.option('--drop',is_flag=True,help='先删除后创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')


#向空数据库中插入数据

@app.cli.command() #注册为命令
def forge():
    name='yyk'
    movies=[
        {'title':'奥特曼','year':"2079"},
        {'title':'战狼','year':"2104"},
        {'title':'外星人','year':"9999"},
        {'title':'无字天书','year':"2079"},
        {'title':'舒克和贝塔','year':"2001"},
        {'title':'葫芦娃','year':"2009"},
        {'title':'铁甲小宝','year':"1999"},
    ]
    user=User(name=name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    