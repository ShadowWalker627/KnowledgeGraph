# -*- coding: utf-8 -*-
import requests

# 获取所有节点和关系，用于查询一个label时返回
def getAllNodeAndRelation():
    query = {
        "query": "MATCH (n)-[r]->() RETURN n, r",
        "params": {}
    }
    res = requests.post("http://localhost:7474/db/data/cypher", data=query, auth=('neo4j', 'database'))
    print(res.json())
    # for i in res.json()['data']:
    #     print(i)
    return res.json()

# 查询 label 时的返回
def getOneLabelInfo(label):
    query = {
        "query": "MATCH (n:%s)-[r]->() RETURN n, r" % (label),
        "params": {}
    }
    res = requests.post("http://localhost:7474/db/data/cypher", data=query, auth=('neo4j', 'database'))
    print(res.json())


# 直接上传文本字符串
def uploadString():
    print('updateString')

if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")