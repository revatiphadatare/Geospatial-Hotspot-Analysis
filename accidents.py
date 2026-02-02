# This program creates accidents.csv with 500 records


import csv
import random
from datetime import datetime, timedelta

# Maharashtra city locations (latitude, longitude)
locations = [
    (19.075983, 72.877655),  # Mumbai
    (18.520430, 73.856743),  # Pune
    (21.145800, 79.088158),  # Nagpur
    (19.997454, 73.789803),  # Nashik
    (16.705000, 74.243300),  # Kolhapur
    (19.876165, 75.343314),  # Aurangabad
    (20.937423, 77.779551),  # Amravati
]

# Generate a random date in 2025
def random_date_2025():
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    days_between = (end - start).days
    random_days = random.randint(0, days_between)
    return start + timedelta(days=random_days)

# Create accidents.csv file
with open("accidents.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header (must match hotspot code)
    writer.writerow([
        "accident_id",
        "latitude",
        "longitude",
        "severity",
        "timestamp"
    ])

    # Generate 500 accident records
    for accident_id in range(1, 501):

        # Choose random Maharashtra location
        base_lat, base_lon = random.choice(locations)

        # Add small random variation
        latitude = base_lat + random.uniform(-0.02, 0.02)
        longitude = base_lon + random.uniform(-0.02, 0.02)

        # Severity between 1 and 5
        severity = random.randint(1, 5)

        # Date in 2025
        date = random_date_2025().strftime("%Y-%m-%d")

        # Write one row to CSV
        writer.writerow([
            accident_id,
            round(latitude, 6),
            round(longitude, 6),
            severity,
            date
        ])

print("accidents.csv generated successfully with 500 records")
