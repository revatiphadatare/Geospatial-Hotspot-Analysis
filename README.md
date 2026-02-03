<<<<<<< HEAD
# Geospatial Hotspot Analysis – Phase I

# Objective
The goal of this project is to implement a **Geospatial Hotspot Analysis** system to identify accident-prone areas in Maharashtra and calculate zone-level risk scores. This is part of Phase-I of the AI Emergency Pressure & Ambulance Load Prediction System.

## Project Description
This project analyzes accident data from the year 2025 (synthetic dataset) to:
1. Detect accident hotspots using **DBSCAN clustering**.
2. Perform clustering on geospatial location data.
3. Generate **zone-level risk scores** based on accident count and severity.
4. Output **heatmap-ready JSON data** for visualization.

## Folder Structure
Geospatial Hotspot Analysis/
│
├── geospatial_hotspot.py # Main implementation of hotspot detection
├── accidents.py # Script to generate synthetic accident data
├── accidents.csv # Input accident dataset (2025, Maharashtra)
├── heatmap_data.json # Output JSON file (heatmap-ready)
└── README.md # Project explanation


## Tools and Libraries
- Python 3.x
- Pandas
- NumPy
- scikit-learn (DBSCAN)
- JSON (for output)

## How to Run
1. Make sure all files are in the same folder.
2. Open Command Prompt or terminal and navigate to the folder:

```bash
cd "path_to/Geospatial Hotspot Analysis"
Run the hotspot analysis script:

python geospatial_hotspot.py
Output file heatmap_data.json will be generated in the same folder.

Notes
accidents.csv is a synthetic dataset generated for demonstration.

Risk score is calculated using:

Risk Score = (Accident Count × 0.6) + (Average Severity × 0.4)
Only hotspots (clusters) are considered; noise points are ignored.

Author
Revati Phadatare

Project submitted for Phase-I: AI Emergency Pressure & Ambulance Load Prediction System
=======
# Geospatial-Hotspot-Analysis
Phase-1 Geospatial Hotspot Analysis Project
>>>>>>> origin/main
