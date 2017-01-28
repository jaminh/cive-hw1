import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

url = 'http://205.221.97.102/Iowa.Sims.AllSites.C2C/IADOT_SIMS_AllSites_C2C.asmx/OP_ShareTrafficDetectorData?MSG_TrafficDetectorDataRequest=string%20HTTP/1.1'
request = urllib2.Request(url, headers={"Accept": "text/xml"})
contents = urllib2.urlopen(request).read()

f = open("stream.xml", 'w')
f.write(contents)
f.close()


