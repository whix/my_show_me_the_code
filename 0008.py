__author__ = 'Administrator'
import re
import requests
from goose import Goose

html = requests.get('http://www.xuebuyuan.com/2127057.html').content.decode('utf-8')
print html
lst = re.findall(r'', html)

print lst