from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'My First Flask!!!!!'

@app.route('/learning')
def learn():
  return 'I am learning!'

app.run()