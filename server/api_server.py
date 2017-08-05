from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Menu, Chef

app = Flask(__name__)
cors = CORS(app)

engine = create_engine('sqlite:///foodapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# API
# TODO: need to convert a datetime string to a datetime.time object
# https://chrisalbon.com/python/strings_to_datetime.html
@app.route('/')
def show_api():
    methods = ['/api/get/menu/date/<string:date>/',
              '/api/get/menu/id/<int:menu_id>/',
              '/api/get/menu/all',
              '/api/post/menu/id/']
    return render_template('welcome.html', methods=methods)

@app.route('/api/get/menu/date/<string:date>/', methods=['GET'])
def get_menu_daily(date):
    menu_daily = session.query(Menu).filter_by(date=date).all()
    return jsonify(dailyMenu=[menu.serialize for menu in menu_daily])

@app.route('/api/get/menu/id/<int:menu_id>/', methods=['GET'])
def get_menu_byId(menu_id):
    menu = session.query(Menu).filter_by(id=menu_id).one()
    return jsonify(dailyMenu=menu.serialize)

@app.route('/api/get/menu/all', methods=['GET'])
def get_menu_all():
    menu_all = session.query(Menu).all()
    return jsonify(allMenus=[menu.serialize for menu in menu_all])

# TODO: research in what format client form data is sent to server
# and if flask request method works for this
@app.route('/api/post/menu/id/', methods=['POST'])
def create_menu():
    newMenu = Menu(date=request.form['date'],
                   name=request.form['name'],
                   description=request.form['description'],
                   price=request.form['price'],
                   image_url=request.form['image_url'],
                   chef_id=request.form['chef_id'],)
    session.add(newMenu)
    session.commit()
    return "success"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
