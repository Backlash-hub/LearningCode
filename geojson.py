import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break
    
    url = serviceurl + urllib.parse.urlencode({'address': address})
    
    print('Retreiving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retreived', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] !='OK':
        print('======FAILURE TO GET========')
        print(data)
        continue