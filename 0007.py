__author__ = 'Administrator'
import os

file_path = 'F:\\wayne\\test\\'
files = os.listdir(file_path)
dic = {}
for f in files:
    try:
        line_num = len(open(file_path + f, 'r').readlines())
        dic[f] = line_num
    except IOError, e:
        print e
print dic