import urllib.request
import json
import webbrowser
endpoint = 'https://www.google.com/maps/embed/v1/directions?key=AIzaSyDfh7J9G9P_GsThqT6LLtVSowywxuxRRY0'
# start = input("Where are you from?").replace(' ', '+')
# end = input("Where are you going?").replace(' ', '+')
start_static = "Charlottesville, VA".replace(' ', '+')
end_static = "Chester, NJ".replace(' ', '+')
directions_request = '&origin={}&destination={}'.format(start_static, end_static)
nav_request = endpoint + directions_request