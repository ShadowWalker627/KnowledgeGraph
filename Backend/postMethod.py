# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, request
import requests, os

UPLOAD_FOLDER = '/Users/baymax'

# 接收上传文件
def uploadFile(file):
    # file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))