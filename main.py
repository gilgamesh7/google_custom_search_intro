# Readme
# https://youtu.be/D4tWHX2nCzQ?si=N5WM3D54rkEeX7WL
# https://programmablesearchengine.google.com/controlpanel/create
# <script async src="https://cse.google.com/cse.js?cx=3260b8cb168c449a1">
# </script>
# <div class="gcse-search"></div>
# https://developers.google.com/custom-search/v1

import httpx
import pandas

from dotenv import load_dotenv
import os
import sys

pandas.set_option('display.max_colwidth', None)

load_dotenv()
API_KEY = os.environ.get('API_KEY')
SEARCH_ENGINE_ID = os.environ.get('SEARCH_ENGINE_ID')
print(f"{API_KEY=} , {SEARCH_ENGINE_ID=}")
sys.exit()

# query = "Donnie Brasco"
# query = "Benedict Cumberbatch"

query = "Benedict Cumberbatch movies list"

# query = "hwqgbdiuwyfgdbsuw"
# query = "MongoDB"

information_sources=['imdb', 'rotten tomatoes', 'wikipedia']
for index in range(0,3):
    # query = f"List of Movies Benedict Cumberbatch has acted in from {information_sources[index]}"
    query = f"Movie Donnie Brasco from {information_sources[index]}"
    payload = {
        'key' : API_KEY,
        'q' : query,
        'cx' : SEARCH_ENGINE_ID,
        'start' : 1,
        'num' : 1
    }

    response = httpx.get('https://www.googleapis.com/customsearch/v1', params=payload)
    print(response.json()['items'][0]['link'])
    

# dataframe_main = pandas.json_normalize(response.json()['items'][0])

# dataframe_metatags = pandas.json_normalize(response.json()['items'][0]['pagemap']['metatags'])
# print(dataframe_main.to_string())
# print(dataframe_metatags.to_string())

# print(dataframe_main.title.to_string(index=False))
# print(dataframe_main.link.to_string(index=False))
# print(dataframe_main.snippet.to_string(index=False))

# print(dataframe_metatags['twitter:image:alt'].to_string(index=False))
# for col in dataframe_metatags.columns:
#     print(col)

# print(response.json())
# print(response.json()['items'][0]['title'])
# print(response.json()['items'][0]['snippet'])
# print(response.json()['items'][0]['link'])
# print(response.json()['items'][0]['pagemap']['metatags'][0]['twitter:image:alt'])
# page = httpx.get("https://en.wikipedia.org/wiki/List_of_Benedict_Cumberbatch_performances")
# print(page.content)
# for item in response.json()['items']:
#     print(item['link'])
    
