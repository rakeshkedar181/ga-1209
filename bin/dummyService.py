import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def checkStatus():
    return "Yay It's working!!"

#added coment
app.run(host='localhost',port='8080')