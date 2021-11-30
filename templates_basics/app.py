from flask import Flask, render_template, url_for
# import data
from data import *

application = Flask(__name__)


@application.route('/')
@application.route('/home')
@application.route('/index')
def index():
    return render_template('index.html', title='Git CheatSheet', data=data)


if __name__ == '__main__':
    application.run(debug=True)
