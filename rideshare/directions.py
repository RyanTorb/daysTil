import googlemaps
from datetime import datetime

# gmaps = googlemaps.Client(key='AIzaSyDfh7J9G9P_GsThqT6LLtVSowywxuxRRY0')

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)

# print(directions_result)


import urllib.request
import json
import webbrowser
endpoint = 'https://maps.googleapis.com/maps/api/staticmap?'
api_key = 'AIzaSyDfh7J9G9P_GsThqT6LLtVSowywxuxRRY0'
center = input("What region are you starting from?").replace(' ', '+')
zoom = 6
size = '400x400'
origin = input("Where are you?").replace(" ", '+')
start_marker = 'color:white%7C' + origin
end = input("Where are you going?").replace(' ', '+')
end_marker = 'color:red%7C' + end
nav_request = 'center={}&zoom={}&size={}&markers={}&markers={}&key={}'.format(center, zoom, size, start_marker, end_marker, api_key)
request = endpoint + nav_request
print(request)
webbrowser.open(request)
# response = urllib.request.urlopen(request).read()
# directions = json.load(response)
# print(directions)