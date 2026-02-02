#Geospatial Hotspot Analysis
#Phase-I - Foundation

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import json
try:
    accidents=pd.read_csv("accidents.csv")
except FileNotFoundError:
    print("accidents.csv file not found")
    exit()
locations = accidents[['latitude', 'longitude']].values
location_rad = np.radians(locations)

dbscan = DBSCAN(eps = 0.01,min_samples = 3,metric = 'haversine')
accidents['cluster'] = dbscan.fit_predict(location_rad)

hotspots=accidents[accidents['cluster'] != -1]

hotspots['zone_lat'] = hotspots['latitude'].round(3)
hotspots['zone_lon'] = hotspots['longitude'].round(3)

zone_data = hotspots.groupby(['zone_lat', 'zone_lon']).agg(accident_count=('accident_id', 'count'),average_severity=('severity', 'mean')).reset_index()
zone_data['risk_score'] = ( zone_data['accident_count'] * 0.6 + zone_data['average_severity'] * 0.4)

heatmap_data = []
for _, row in zone_data.iterrows():
    heatmap_data.append({"lat": row['zone_lat'],"lng": row['zone_lon'],"weight": round(row['risk_score'], 2)})
with open("heatmap_data.json", "w") as output_file:
    json.dump(heatmap_data, output_file, indent = 2)

print("Geospatial hotspot analysis completed successfully")









