from nltk.parse.stanford import StanfordDependencyParser

chi_parser = StanfordDependencyParser(r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser-3.6.0-models.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/chinesePCFG.ser.gz"
                                      )
res = list(chi_parser.parse(u'螺纹 按 其 截面 形状 （ 牙型 ） 分为 三角形螺纹 、 矩形螺纹 、 梯形螺纹'.split()))

for row in res[0].triples():
    print(row)