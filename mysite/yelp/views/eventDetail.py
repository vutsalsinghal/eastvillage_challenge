from django.shortcuts import render
import requests

def page(request, event_id, miles_away):
    API_KEY = 'API_KEY'
    API_ENDPOINT = 'https://api.yelp.com/v3/events/' + event_id

    headers = {'Authorization': 'Bearer %s' %(API_KEY)}
    url_params = {}

    response = requests.request('GET', API_ENDPOINT, headers=headers, params=url_params)
    responseObj = response.json()

    d = {}
    d['name'] = responseObj['name']
    d['description'] = responseObj['description']
    d['time_start'] = responseObj['time_start']
    d['event_site_url'] = responseObj['event_site_url']
    d['latitude'] = responseObj['latitude']
    d['longitude'] = responseObj['longitude']

    if responseObj['cost'] is None:
        d['cost'] = 'Free!!!'
    else:
        d['cost'] = '$' + str(responseObj['cost'])

    return render(request, 'eventDetail.html',{'detail':d, 'miles_away':miles_away})