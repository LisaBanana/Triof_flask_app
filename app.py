from flask import Flask, render_template, request
from src.utils import *
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():

    open_waste_slot()
    take_trash_picture()
    return render_template('insert.html')


@app.route('/waste/pick-type')
def pick_type():
    json = make_classification()
    label = json['predictions'][0]['tagName']
    close_waste_slot()
    return render_template('confirm_type.html', data = label)

@app.route('/waste/confirm_type')
def confirm_type():
    # close_waste_slot()
    process_waste(label)
    move_container(label)
    return render_template('confirmation.html', data = label)


@app.route('/confirmation', methods=['POST'])
def confirmation():
    return render_template('confirmation.html')




if __name__ == "__main__":
    app.run(debug=True)
