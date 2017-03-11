#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试gensim使用，处理中文语料
时间：2016年5月21日 20:49:07
"""

from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u'testVec.txt' )  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

# 计算某个词的相关词列表
y2 = model.most_similar(u"螺旋线", topn=20)  # 20个最相关的
# print(u"和【螺纹】最相关的词有：\n")
count = 0
for item in y2:
    # if(count < 3):
    #     count += 1
        print(item[0], item[1])


# 计算两个词的相似度/相关程度
# y1 = model.similarity(u"不错", u"好")
# print(u"【不错】和【好】的相似度为：", y1)