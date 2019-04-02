# coding: utf-8
# Developer: Deiner Zapata Silva.
# Date: 01/14/2019
# Description: Server to show everything to received.
# https://blog.nearsoftjobs.com/crear-un-api-y-una-aplicación-web-con-flask-6a76b8bf5383
#########################################################################################
import sys, requests, json, ast
from utils import print_json
from datetime import datetime, timedelta
from flask import Flask, request, abort
#######################################################################################
URL = "http://209fe4c7.ngrok.io"
app = Flask(__name__)
#######################################################################################
def req_get(URL_API, data=None, timeout=None):
    try:
        headers =  {'Content-Type': 'application/json'}
        rpt = requests.get( url=URL_API, data=data, headers=headers, timeout=timeout)
        print("{0} [INFO ] req_get |{1}|{2}|{3}|".format( datetime.utcnow().isoformat(), rpt.status_code, rpt.reason, URL_API))
        print(rpt.text)
        return rpt.text
    except:
        print("{0} [ERROR] req_get |{1}|{2}|".format( datetime.utcnow().isoformat(), URL_API))
        return ""
#######################################################################################
def req_post(URL_API, data=None, timeout=None):
    try:
        headers =  {'Content-Type': 'application/json'}
        rpt = requests.post( url=URL_API, data=None, headers=headers , timeout=timeout)
        print("{0} [INFO ] req_post|{1}|{2}|{3}|".format( datetime.utcnow().isoformat(), rpt.status_code, rpt.reason, URL_API))
        print(rpt.text)
        return rpt.text
    except:
        print("{0} [ERROR] req_post|{1}|{2}|".format( datetime.utcnow().isoformat(), URL_API))
        return ""
#######################################################################################
def bytesELK2json(data,codification='utf-8'):
    d_dict = {}
    try:
       d_str = data.decode(codification)
       d_str = d_str.replace("false","False")
       d_dict = eval(d_str)
    except:
       print("[ERROR] type={0} ".format( type(data) ))
    finally:
       return d_dict
#######################################################################################
@app.route('/', methods=['POST'])
def webhook_post():
    #URL = "http://1855b969.ngrok.io"
    print("webhook_post()-> "+ str(sys.stdout.flush()) )
    print_json( bytesELK2json( request.data ))
    rpt = req_post(URL, data = request.data, timeout=None)
    return '', 200
#######################################################################################
@app.route('/', methods=['GET'])
def webhook_get():
    #URL = "http://1855b969.ngrok.io"
    print("webhook_get()-> "+ str(sys.stdout.flush()) )
    print_json( bytesELK2json( request.data ))
    rpt = req_get(URL, data = request.data, timeout=None)
    return '', 200
#######################################################################################
@app.route('/hearbeat_ping_down', methods=['GET','POST'])
def solve_ping():
    print("DEF ping-----------------------")
    print( request.data )
    return '', 200
#######################################################################################
if __name__ == '__main__':
    app.run(host='172.30.0.114',port=3009)
