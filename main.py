#!/usr/bin/env python

import urllib2
import urllib
import re
import sys
    

def read_file(url):
    passage = '\n'
    try:
        res = urllib2.urlopen(url)
    except urllib2.URLError, e:
        print e.code
        print "Some error in ",url
        pass
    else:    
        f = res.read()
        pat = re.compile("<p>(.+)</p>?")
        paras = pat.findall(f)

        non = re.compile("&#\d{3,4};")
        for para in paras:
            para = non.sub("", para)
        
            passage = para + passage + '\n'
        return passage



def fetch(url):
    arch = {}
    res = urllib2.urlopen(url)
    root_url = res.geturl()
    root_url = '/'.join(root_url.split("/")[:-1])+'/'
    data = res.read() 
    pat = re.compile("<p>.+</p>?")
    paras = pat.findall(data)
    en = re.compile(r"<p><a href=\"(\w+)\">(.+)?</a>(.+)?</p>") # findall(?<![/<])(\w+)(?![>])
    
    for para in paras:
        ent = en.match(para)
        if ent:
            arch[ent.group(2)] = root_url + ent.group(1)

    for key in arch.keys():
        filename = arch[key].split('/')[-1]
        filename = "aaron_blog/" + filename
        f = open(filename,"w")
        f.write(ent.group(2) + ent.group(3) + '\n')
        try:
            f.write(read_file(arch[key]))
        except TypeError:
            print "Bad URL and not content found!"
            pass
        finally:
            f.close()
        

if "__main__"==__name__:

    url = sys.argv[1]
    fetch(url)
