__author__ = 'Administrator'

f = open('filtered_words.txt', 'r')
str = f.read()
print str
word = raw_input("Enter a word:")
if word in str:
    print 'Freedom'
else:
    print 'Human Rights'