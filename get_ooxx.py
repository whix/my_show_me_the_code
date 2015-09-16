#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import re
import os


class FetchMMPictureUrl():
    def __init__(self):
        # 抓取的页数范围
        self.urls = ['http://jandan.net/ooxx/page-%d#comments'% x for x in xrange(1500, 1551)]
        self.directory = 'jiandanmeizitu'
        self.reg = re.compile(r'src=".*?(http://.*?\.jpg)')
        self.path = os.getcwd() + '\\' + self.directory
        is_exist = os.path.exists(self.path)
        if not is_exist:
            os.system('mkdir ' + self.path)

    def working(self):
        for url in self.urls:
            try:
                headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
                html = requests.get(url, headers=headers).content
            except IOError:
                pass
            items = re.findall(self.reg, html)
            for item in items:
                name = len(os.listdir(self.path))
                try:
                    data = requests.get(item).content
                except IOError:
                    pass
                name = self.path + '\\' + str(name) + '.jpg'
                with open(name, 'wb') as f:
                    f.write(data)
                    f.close

if __name__ == '__main__':
    fetch_mm = FetchMMPictureUrl()
    fetch_mm.working()