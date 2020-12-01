import requests
import pprint
import pandas as pd
api_key = "<api_key>"
# movie_id = 603
api_version = 3
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"


base_url = f"https://api.themoviedb.org/{api_version}"
path = f"/search/movie"
searc_query = "The Matrix"
url = f"{base_url}{path}?api_key={api_key}&query={searc_query}"
x = requests.get(url)

movies_ids = set()
if x.status_code in range(200, 299):
    data = x.json()
    results = data["results"]
    if len(results) > 0:
        for result in results:
            _id = result["id"]
            movies_ids.add(_id)


movie_data = []

for movie_id in movies_ids:
    api = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
df.to_csv("movies.csv", index=False)
