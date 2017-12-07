api_key = "5OY240GGemjfZrjV66o7OgePYReqJPcG"
api_url = "https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey="

import ticketpy

tm_client = ticketpy.ApiClient("5OY240GGemjfZrjV66o7OgePYReqJPcG")
venues = tm_client.venues.find(keyword="Tabernacle").all()
for v in venues:
    print("Name: {} / City: {}".format(v.name, v.city))

