from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Menu, Chef

app = Flask(__name__)

engine = create_engine('sqlite:///foodapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# API
# TODO: need to convert a datetime string to a datetime.time object
# https://chrisalbon.com/python/strings_to_datetime.html
@app.route('/', methods=['GET'])
def get_daily_menu():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
