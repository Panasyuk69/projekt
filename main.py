from flask import Flask, request
import settings

app = Flask(__name__)

app.config.from_object(settings)

@app.route('/')
def index():
    some_value = request.args
    name = some_value.get('name')
    age = some_value.get('age')
    return "Hello, " + name + " " + age
    #return ' Hello world!'

@app.route('/feed/history')
def history():
    return "My name is Vova"

@app.route('/test')
def test():
    return "Test"

# app.add_url_rule('/', "index", index)
app.run()