#! usr/bin/python
# -*- coding: utf-8 -*-

############################# Application Imports #########################
from flask import Flask, request, render_template, json, Response, session, redirect, url_for, Markup
from werkzeug import secure_filename
import os
import json
import urllib2
from urllib import urlopen
import re

###############app settings######################
app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(25)

###############App routes##################
@app.route('/')
def index():
    url = 'http://www.history.com/this-day-in-history'
    f = urlopen(url).read()
    title = re.search( "<meta name=\"search_title\".*?content=\"([^\"]*)\"", f ).group( 1 )
    title = title.split('&mdash;')
    ip = request.remote_addr
    tmp = title[0].replace(" ","+")
    url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&imgsz=large&q='+tmp+'&userip='+ip)
    requests = urllib2.Request(url, None)
    response = urllib2.urlopen(requests)
    results = json.load(response)
    return render_template('history.html', title=title[0], url = results["responseData"]["results"][0]["url"], time = title[2])

################flask server################
if __name__ == "__main__":
    app.run(debug=True)
