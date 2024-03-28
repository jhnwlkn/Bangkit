import streamlit as st

st.title("Air Quality Analysis Dashboard")

# Function to display image and information for a specific graph
def display_graph_info(judul_grafik, penjelasan_grafik, path_gambar):
    st.header(judul_grafik)
    with st.expander("Penjelasan"):
        st.text(penjelasan_grafik)

    st.image(path_gambar, caption=judul_grafik, use_column_width=True)

# Display information for each graph
display_graph_info("Bar Plot Perbandingan SO2 di Antara Stasiun", "Tingkat SO2 tertinggi tercatat di stasiun Wanshouxigong dengan rata-rata 17.15, \nsedangkan tingkat terendah terjadi di stasiun Huairou dengan rata-rata 12.12. \nVariasi ini mencerminkan perbedaan dalam paparan sulfur dioksida di kedua lokasi.", "SO2.png")
display_graph_info("Bar Plot Perbandingan NO2 di Antara Stasiun", "Stasiun Wanliu mencatat tingkat tertinggi NO2 dengan rata-rata 65.26, \nsementara stasiun Dingling menunjukkan tingkat terendah sebesar 27.59. \nPerbedaan ini dapat memberikan indikasi tentang sumber polusi udara di kawasan tersebut.", "NO2.png")
display_graph_info("Bar Plot Perbandingan CO di Antara Stasiun", "Stasiun Wanliu kembali mendominasi dengan tingkat CO tertinggi, \nmencapai rata-rata 1370.40, sementara stasiun Dingling memiliki tingkat terendah sebesar 904.90. \nInformasi ini penting untuk pemahaman tingkat paparan karbon monoksida di daerah tersebut.", "CO.png")
display_graph_info("Bar Plot Perbandingan O3 di Antara Stasiun", "Stasiun Dingling memiliki tingkat O3 tertinggi dengan rata-rata 68.55, \nsedangkan stasiun Wanliu menunjukkan tingkat terendah sebesar 48.87. \nVariabilitas ini dapat memberikan wawasan tentang ketersediaan ozon di lokasi tersebut.", "O3.png")
display_graph_info("Bar Plot Perbandingan Pollutant Level di Antara Stasiun", "Tingkat pencemaran udara secara keseluruhan tertinggi terjadi di stasiun \nWanshouxigong dengan rata-rata 374.83, sedangkan \nstasiun Dingling mencapai tingkat terendah sebesar 253.19. \nData ini menggambarkan gambaran menyeluruh tentang tingkat pencemaran \nudara di berbagai lokasi pengukuran.", "pollutant level.png")
display_graph_info("Bar Plot Perbandingan Max Min Tempratur di Antara Stasiun", "Informasi ini mengindikasikan variasi suhu yang signifikan antara stasiun \nGucheng dan Wanliu. Suhu tertinggi yang tercatat di stasiun Gucheng dapat menggambarkan \nkondisi lingkungan yang cenderung lebih panas di lokasi tersebut. \nDi sisi lain, suhu terendah yang terjadi di stasiun Wanliu menunjukkan adanya perbedaan \niklim atau karakteristik lingkungan yang membuat stasiun tersebut lebih \ncenderung mengalami suhu yang lebih rendah", "max min temprature.png")
st.caption("Made by: Jo")