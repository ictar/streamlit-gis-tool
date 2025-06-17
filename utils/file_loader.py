import geopandas as gpd
import zipfile
import tempfile
import os

def load_vector_data(uploaded_file):
    try:
        if uploaded_file.name.endswith(".geojson"):
            return gpd.read_file(uploaded_file)
        elif uploaded_file.name.endswith(".zip"):
            with tempfile.TemporaryDirectory() as tmp:
                with zipfile.ZipFile(uploaded_file, "r") as z:
                    z.extractall(tmp)
                files = [os.path.join(tmp, f) for f in os.listdir(tmp)]
                shp_files = [f for f in files if f.endswith(".shp")]
                if shp_files:
                    return gpd.read_file(shp_files[0])
    except Exception as e:
        print(f"Error loading vector data: {e}")
        return None