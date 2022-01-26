import json
import urllib.request

# Downloading from the internet directly:
temperature_data = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/7/1880-2021/data.json'
# What we are doing here is a stream - we are accessing the data directly
# from the source without downloading the actual data to our devices. Similar
# to films/series and audio streaming services, such as Netflix, Amazon Prime
# and Spotify

# with open(temperature_data, 'r', encoding='utf-8') as temp_data_file:
# Reading our data from a URL:
with urllib.request.urlopen(temperature_data) as temp_json_stream:
    json_url_data = temp_json_stream.read().decode('utf-8')
    anomalies_data = json.loads(json_url_data)  # We need to use the .loads()
    # method for us to be able to read the string in temperature_data

print(anomalies_data['data'])

for year, temp in anomalies_data['data'].items():
    year, temp = int(year), float(temp)
    print(f"{year} ...{temp:6.2f}")