import json

temperature_data = 'temperature_anomaly.json'

#https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/7/1880-2021/data.json

with open(temperature_data, 'r', encoding='utf-8') as temp_data_file:
    anomalies_data = json.load(temp_data_file)
# In the temperature_anomaly.json file, choose Code -> Reformat Code to view
# the JSON file in a more readable format

print(anomalies_data['description'])
print(anomalies_data['data'])
print(anomalies_data['citation'])

print("=" * 80)

for year in anomalies_data['data'].keys():
    print(year)

print("=" * 80)

for key, value in anomalies_data['description'].items():
    print(f"{key} : {value}")

print("=" * 80)

for year, temp in anomalies_data['data'].items():
    year, temp = int(year), float(temp)
    print(f"{year} ...{temp:6.2f}")
