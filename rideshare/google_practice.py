

start = input("Where from?").replace(" ", "")
end = input("Where to?").replace(" ", "")

from gmaps import Directions
api = Directions(api_key="AIzaSyDfh7J9G9P_GsThqT6LLtVSowywxuxRRY0")

result = api.directions(start, end)
print(result)


