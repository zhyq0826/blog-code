##!/usr/bin/env python
# coding: utf-8

style = """
</style>
"""

style = open('custome.css', 'r').read() + style

import sys
import codecs
import re


def replace_fontface(s):
    last_start = s.find('@font-face')
    begin = last_start
    while 1:
        start = s.find('@font-face', last_start+11)
        if start < 0:
            break
        last_start = start

    end = s.find('}', last_start)
    return s[0:begin]+s[end+1:]

def replace_link(s):
    start = s.find('<link')
    end = s.find('>', start)
    return s[0:start]+s[end+1:]

def main():
    # name = sys.argv[0]
    name = 'pub.html'
    f = codecs.open(name,'r', 'utf-8')
    o = codecs.open(name.replace('.html', '_out.html'), 'w', 'utf-8')
    data = f.read()
    data = data.replace('</style>', style)
    data = replace_fontface(data)
    data = replace_link(data)
    o.write(data)

if __name__ == '__main__':
    main()