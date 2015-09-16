#!/usr/bin/env python2
# -*- coding: utf-8 -*-

f = open('filtered_words.txt', 'r')
words = [i.replace('\n', '') for i in f]

print words
f.close()
def replace_sentence(sentence, filtered_words):
    for word in filtered_words:
        if word in sentence:
            print word
            sentence = sentence.replace(word, len(word)*'*')
    return sentence
while True:
    str = raw_input("Enter a Sentence or enter 'q' to quit:")
    if str == 'q':
        break
    print replace_sentence(str, words)

