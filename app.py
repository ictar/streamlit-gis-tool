import streamlit as st
from utils.file_loader import load_vector_data
from utils.geo_analysis import apply_buffer
from components.map_view import render_map_and_table
from components.map_3d import render_3d_map

st.set_page_config(page_title="Streamlit GIS Analyst", layout="wide")
st.title("🗺️ Streamlit GIS Analyst")

uploaded_file = st.file_uploader("Upload a GeoJSON or Shapefile (.zip)", type=["geojson", "zip"])

if uploaded_file:
    gdf = load_vector_data(uploaded_file)
    if gdf is not None:
        st.subheader("📍 Attribute Table")
        st.dataframe(gdf.drop(columns='geometry'))

        st.subheader("🗺️ 2D Map View")
        render_map_and_table(gdf)

        st.subheader("📏 Buffer Analysis")
        distance = st.slider("Buffer distance (meters)", 100, 10000, 1000)
        buffered_gdf = apply_buffer(gdf, distance)
        st.write("Buffered geometry preview:")
        render_map_and_table(buffered_gdf)

        st.subheader("🌍 3D Map View")
        render_3d_map(gdf)
    else:
        st.error("Failed to load vector data. Please check your file format.")