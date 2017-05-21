from flask import Flask, request, make_response, redirect


APP = Flask(__name__)


@APP.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response('<h1>This document sets a cookie.</h1>')
    response.set_cookie('answer', '42')
    return response # '<h1>Hello World!</h1><p>Your browser is {}.</p>'.format(user_agent)


@APP.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@APP.route('/google')
def google():
    return redirect('http://www.google.com')


if __name__ == '__main__':
    APP.run(debug=True)