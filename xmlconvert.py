
import xmltodict
import urllib


import os, sys

MAIN_URL = 'http://www.tfl.gov.uk/tfl/livetravelnews/trafficcams/cctv/'

def downloadImage(url,postcode):

    filename = '/users/shared/documents/media3/' + postcode + '.jpg'

    url = MAIN_URL +url
    print 'Downloading picture for url:' + url

    f = open(filename, 'wb')
    f.write(urllib.urlopen(url).read())
    f.close()

xmlurl = 'http://www.tfl.gov.uk/tfl/livetravelnews/trafficcams/cctv/jamcams-camera-list.xml'

camerasInEast = []

xml = urllib.urlopen(xmlurl).read()
parsed = xmltodict.parse(xml, process_namespaces=False) 
for d in parsed['syndicatedFeed']['cameraList']['camera']:
    postcode = d['postCode']
    if postcode and postcode[0] =='E':
        if not 'unavailabilityCause' in d:
            file = d['file']
            loc = d['location']
            dic = {'loc': loc, 'postcode': postcode, 'file':file}
            camerasInEast.append(dic)

print camerasInEast

def main():
    for camera in camerasInEast:
        postcode = camera['postcode']
        file = camera['file']
        downloadImage(file,postcode)

if __name__ == '__main__':
    main()


