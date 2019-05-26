from flask import Flask, request, render_template

apps = Flask(__name__)

@apps.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@apps.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@apps.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='rainys' and password=='123':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    apps.run()