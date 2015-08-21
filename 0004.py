__author__ = 'Administrator'
import string
ignore = string.digits + string.punctuation
text = 'filename'
def count_words_num(filename=text, ignore=ignore):
    txt = open(filename).read()
    for x in ignore:
        txt = txt.replace(x, ' ')
    txt = txt.lower()
    txt = txt.split(' ')
    dic = {}
    for word in txt:
        if len(word) == 1:
            continue
        if word in dic:
            dic[word] += 1
        if word not in dic:
            dic[word] = 1
    return dic

