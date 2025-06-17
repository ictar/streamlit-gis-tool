import pydeck as pdk
import streamlit as st

def render_3d_map(gdf):
    if gdf.geometry.iloc[0].geom_type != "Point":
        st.info("3D map currently only supports Point geometries.")
        return

    df = gdf.copy()
    df["lon"] = df.geometry.x
    df["lat"] = df.geometry.y
    df["elevation"] = 1000  # static elevation or calculate from attribute

    layer = pdk.Layer(
        "ColumnLayer",
        data=df,
        get_position='[lon, lat]',
        get_elevation='elevation',
        elevation_scale=1,
        radius=200,
        get_fill_color='[180, 0, 200, 140]',
        pickable=True,
        auto_highlight=True
    )

    view_state = pdk.ViewState(
        latitude=df["lat"].mean(),
        longitude=df["lon"].mean(),
        zoom=10,
        pitch=45
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    st.pydeck_chart(r)
