import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
from st_pages import hide_pages

# hide_pages(["Home"]) # nameが"Home"のページを隠す(複数ページ追加可能)

st.set_page_config(layout="wide")

nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()