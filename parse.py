import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('stream.xml')
root = tree.getroot()

namespace = "http://www.dummy-temp-address"
xpath = './/{{{0}}}collection-periods/{{{0}}}collection-period/{{{0}}}detector-reports/{{{0}}}detector-report'.format(namespace)
reports = tree.findall(xpath)

csvfile = open('streamdata.csv', 'wb')
csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

csvwriter.writerow(['Detector-ID', 'Status'])

for i in range(1,100,1):
    csvwriter.writerow([reports[i].getchildren()[0].text, reports[i].getchildren()[1].text])

csvfile.close()
