from django.shortcuts import render
from math import sin, cos, sqrt, atan2, radians
import geoip2.database
import requests

def distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1, lon1, lat2, lon2 = map(radians,[lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 0.621371
    return str(round(distance,2))

def page(request):
    API_KEY = 'API_KEY'
    API_ENDPOINT = 'https://api.yelp.com/v3/events'

    headers = {'Authorization': 'Bearer %s' %(API_KEY)}
    url_params = {'latitude':40.726156, 'longitude':-73.981809} # Location of East Village

    response = requests.request('GET', API_ENDPOINT, headers=headers, params=url_params)
    responseObj = response.json()

    events = []
    reader = geoip2.database.Reader('./eastvillage/GeoLite2-City.mmdb')
    response = reader.city(request.META.get('HTTP_X_REAL_IP'))

    if responseObj['total'] > 10:
        display_limit = 10
    else:
        display_limit = responseObj['total']

    if request.POST:
        try:
            display_limit = int(request.POST.get("display", ""))
            if display_limit > responseObj['total']:
                display_limit = responseObj['total']
        except:
            pass

    for i in range(display_limit):
        d = {}
        d['name'] = responseObj['events'][i]['name']
        d['id'] = responseObj['events'][i]['id']
        d['time_start'] = responseObj['events'][i]['time_start']
        d['event_site_url'] = responseObj['events'][i]['event_site_url']
        d['miles_away'] = distance(responseObj['events'][i]['latitude'], responseObj['events'][i]['longitude'], response.location.latitude, response.location.longitude)
        if responseObj['events'][i]['cost'] is None:
            d['cost'] = 'Free!!!'
        else:
            d['cost'] = '$' + str(responseObj['events'][i]['cost'])
        events.append(d)

    events = sorted(events, key=lambda k:float(k['miles_away']))

    return render(request, 'eventList.html',{'events':events, 'total': responseObj['total'], 'display_limit':display_limit})
