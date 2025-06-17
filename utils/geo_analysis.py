from shapely.geometry import mapping

def apply_buffer(gdf, distance):
    try:
        gdf = gdf.to_crs(epsg=3857)  # Web Mercator for buffering in meters
        gdf["geometry"] = gdf.buffer(distance)
        gdf = gdf.to_crs(epsg=4326)
        return gdf
    except Exception as e:
        print(f"Error applying buffer: {e}")
        return gdf