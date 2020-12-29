# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:18:09 2020

@author: RAKESH
"""

import flask
from flask import Flask, request
from summariser import SummarizerDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizerObj = SummarizerDoc()
    summary = summarizerObj.findSummary()
    return summary
#added comment
app.run(host='localhost',port=8080)