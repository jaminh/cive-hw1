import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

tree = ET.parse('stream.xml')
root = tree.getroot()

#for i in range(1,100,1):
#	z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
#	print z.getchildren()[0].text, "|", z.getchildren()[1].text

namespace = "http://www.dummy-temp-address"
xpath = './/{{{0}}}collection-periods/{{{0}}}collection-period/{{{0}}}detector-reports/{{{0}}}detector-report'.format(namespace)
print xpath
reports = tree.findall(xpath)

for i in range(1,100,1):
    print reports[i].getchildren()[0].text, "|", reports[i].getchildren()[1].text
