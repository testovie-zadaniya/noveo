__author__ = 'flare'

import requests
import urllib
import time

def get_escaped_lines(src):
    with open(src, 'r') as src_obj:
        return [urllib.quote_plus(e) for e in src_obj.readlines()]

def send(line):
    ans = requests.get("http://server:8082?expr=" + line)
    return ans.text

while True:
    try:
        for line in get_escaped_lines('./expressions.txt'):
            send(line)
    except:
        print "pechal'ka"
    time.sleep(1)
