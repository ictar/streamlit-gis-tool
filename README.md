# 🗺️ Streamlit GIS Tool

A simple web-based GIS viewer built with Streamlit. Upload vector data (GeoJSON or Shapefile) and view it interactively on a map.

## Features

- Upload and preview vector files (GeoJSON, Shapefile)
- Interactive 2D map visualization with Folium
- Attribute table display
- 3D map rendering with pydeck
- Geospatial operations: buffering, reprojection, centroid, etc.
- Easy deployment with Streamlit

## Getting Started

```bash
conda create -n gis_app python=3.10
conda activate gis_app
conda install -c conda-forge geopandas folium shapely pyproj streamlit streamlit-folium
streamlit run app.py
```