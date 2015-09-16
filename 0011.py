# -*- coding: utf-8 -*-
import io
f = open('filtered_words.txt', 'r')
words = [word.replace('\n', '') for word in f]

print words
f.close()
def check_sentence(sentence, words):
    for word in words:
        if word in sentence:
            return 'Freedom'
    return 'Human Rights'
while True:
    sentence = raw_input("Enter a Sentence or enter 'q' to quit:")
    if sentence == 'q':
        break
    print check_sentence(sentence, words)

