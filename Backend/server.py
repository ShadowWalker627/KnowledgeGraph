# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

import os
import requests

from restServer import getMethod, postMethod

# getMethod.getAllNodeAndRelation()

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = '/Users/baymax/'

'''
query_node = {
        # "query": "MATCH (n:`螺纹联接`) RETURN n",
        # "query": "MATCH (n) RETURN n",
        "query": "MATCH (n:`螺纹联接`)-[r]->() RETURN n, r",
        "params": {}
    }
rn = requests.post("http://localhost:7474/db/data/cypher", data=query_node, auth=('neo4j', 'database'))
rns = rn.json()
for i in rns['data']:
# for i in rns:
    print(i)
    # print(i[0]['data']['name'], i[0]['metadata']['id'])

query_relation = {
        "query": "MATCH ()-[r]->() RETURN r",
        "params": {}
    }
rr = requests.post("http://localhost:7474/db/data/cypher", data=query_relation, auth=('neo4j', 'database'))
rrs = rr.json()
print(rrs)
for i in rrs:
    print(i)
    # print(i[0]['data']['name'], i[0]['metadata']['id'])

'''

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/getAllInfo', methods=['GET'])
def get_allInfo():
    res = getMethod.getAllNodeAndRelation()
    # for info in res['data']:
    #     print(info)
    return jsonify({'res': res['data']})

@app.route('/getjson', methods=['GET'])
def get_tasks():
    query_node = {
        # "query": "MATCH (n:`螺纹联接`) RETURN n",
        # "query": "MATCH (n) RETURN n",
        "query": "MATCH (n:`螺纹联接`)-[r]->() RETURN n, r",
        "params": {}
    }
    rn = requests.post("http://localhost:7474/db/data/cypher", data=query_node, auth=('neo4j', 'database'))
    rns = rn.json()
    for i in rns['data']:
        # for i in rns:
        print(i)
        # print(i[0]['data']['name'], i[0]['metadata']['id'])

    query_relation = {
        "query": "MATCH ()-[r]->() RETURN r",
        "params": {}
    }
    rr = requests.post("http://localhost:7474/db/data/cypher", data=query_relation, auth=('neo4j', 'database'))
    rrs = rr.json()
    print(rrs)
    for i in rrs:
        print(i)
        # print(i[0]['data']['name'], i[0]['metadata']['id'])
    resp = jsonify({'res': rrs})
    # print(resp)
    return resp

# 上传文本字符串的 API
@app.route('/updateString', methods=['GET'])
def UpdateString():
    if 'textString' in request.args:
        print(request.args['textString'])


@app.route('/postjson', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    # print(task)
    resp = jsonify({'tasks': tasks})
    return resp, 201


@app.route('/uploadFile', methods=['POST'])
def uploadOWL():
    # print(request.files['file'])
    file = request.files['file']
    postMethod.uploadFile(file)

    # filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    resp = 'ok'
    return resp, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)