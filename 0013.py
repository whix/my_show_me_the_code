#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import re
import os


class FetchMMPictureUrl():
    def __init__(self):
        self.url = 'http://tieba.baidu.com/p/2166231880'
        self.html = ''
        self.items = []
        self.directory = 'mm'

    def get_html(self):
        self.html = requests.get(self.url).content

    def get_picture_items(self):
        reg = re.compile(r'src=".*?(http://img.*?sign=.*?jpg)')
        self.items = re.findall(reg, self.html)
        for i in self.items:
            print i

    def get_start(self):
        self.get_html()
        self.get_picture_items()
        self.save_picture()

    def save_picture(self):
        path = os.getcwd() + '\\' + self.directory
        is_exist = os.path.exists(path)
        if not is_exist:
            os.system('mkdir '+ path)
        for i in self.items:
            name = i.split('/')[-1]
            name = path + '\\' + name
            has_pic = os.path.isfile(name)
            if not has_pic:
                f = open(name, 'wb')
                data = requests.get(i).content
                f.write(data)
                f.close()

if __name__ == '__main__':
    fetch_mm = FetchMMPictureUrl()
    fetch_mm.get_start()

