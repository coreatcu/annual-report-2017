from flask import Flask, redirect, render_template, request, url_for, abort
import simplejson

app = Flask(__name__)
data = {}

# import data from relevant JSON
def load_data():
    global data
    with open("data/events.json", 'r') as file:
        data = simplejson.load(file)
    print data.keys()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/event/<event_name>')
def events(event_name):
    if not event_name in data.keys():
        abort(404)
    return render_template('event.html', event_data=data[event_name])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

load_data()

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)

application = app