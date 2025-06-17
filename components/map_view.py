import folium
from streamlit_folium import st_folium

def render_map_and_table(gdf):
    center = gdf.geometry.centroid.iloc[0].coords[0][::-1]
    m = folium.Map(location=center, zoom_start=10)
    folium.GeoJson(gdf).add_to(m)
    st_folium(m, width=700, height=500)
