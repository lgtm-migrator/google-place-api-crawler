# -*- coding: utf8 -*-
from googleplaces import GooglePlaces, types, lang
import pandas as pd
import simplejson as json

API_KEY = 'AIzaSyBZ6dHIrv_aep5hXWLOnrNvdanTWEHy1EI'

google_places = GooglePlaces(API_KEY)
df = pd.read_csv("list_places.csv")
df['FullAddress'] = df.Ward + " " + df.District + " " + df.City

def get_full_information(address = ""):
    print ('Request for address:', address)
    try:
        query_result = google_places.text_search(query=address)
        with open("text_search_cache/" + address, "w") as f:
            json.dump(query_result.raw_response, f)
        print ('Done!')
        return query_result.raw_response
    except:
        print ("Error, skip!")
        return None

df['JSON'] = df.FullAddress.apply(get_full_information)
df.to_csv("list_places_update.csv", index=False)
