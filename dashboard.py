import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
day = pd.read_csv('data\day.csv')

# Streamlit app
st.set_page_config(page_title="Bikecycle Rental")

st.title("Bicycle Rental Dashboard")
tab1, tab2 = st.tabs(["Seasonal Analysis", "Monthly Patterns and Weather Impact"])

# First Tab: Seasonal Analysis
with tab1:
    
    st.header("Bike Rental Analysis")

    # Data visualization - Relationship between season and bike rentals
    seasonal_data = day.groupby('season')['cnt'].mean()
    season_names = ['springer', 'summer', 'fall', 'winter']
    colors = ["pink", "pink", "darkcyan", "pink"]

    # Plotting using seaborn
    fig, ax = plt.subplots()
    sns.barplot(season_names, seasonal_data, palette=colors, ax=ax)
    ax.set(xlabel='Musim', ylabel='Rata-rata Jumlah Sewa Sepeda Harian')
    ax.set_title('Pengaruh Musim terhadap Jumlah Sewa Sepeda Harian')

    # Display the plot using Streamlit
    st.pyplot(fig)
# Explanation
    st.write("""
    Berdasarkan grafik diatas dapat dilihat bahwa rata-rata sewa sepeda lebih banyak pada musim gugur(Fall)
    yaitu sekitar 5600-an sepeda 
    """)
    
    st.write("""
    Musim gugur sering kali ditandai dengan suhu yang nyaman, kelembaban yang moderat, 
    dan kurangnya kondisi ekstrem seperti panasnya musim panas atau dinginnya musim dingin. 
    Cuaca yang baik dan nyaman cenderung mendorong orang untuk beraktivitas di luar ruangan, termasuk bersepeda.
    """)

# Second Tab: Monthly Patterns and Weather Impact
with tab2:
    
    st.header("Bike Rental Analysis")

    # Option to select attribute
    selected_attribute = st.selectbox("Select Attribute", ["Monthly Patterns", "Weather Impact"])

    if selected_attribute == "Monthly Patterns":
        # Visualisation and explanatory data
        # Difference in patterns based on the month in the number of daily bike rentals
        sns.set_style("darkgrid")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x="mnth", y="cnt", data=day, ci=None, color="purple")
        plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
        plt.xlabel("Bulan")
        plt.ylabel("Jumlah Sewa Sepeda Harian")
        st.pyplot()
        # Explanation
        st.write("""
        berdasarkan line chart di atas dapat disimpulkan bahwa dilihat 
        dari pola bulan jumlah sewa sepeda meningkat pada bulan 6 dan 9. 
        Pada bulan 6 dan 9 penyewaan sepeda ada sekitar lebih dari 5500an unit sepeda.
        """)

    elif selected_attribute == "Weather Impact":
        # Visualisation and explanatory data
        # Influence of weather situation (weathersit) on the number of daily bike rentals
        plt.figure(figsize=(10, 6))
        sns.boxplot(x="weathersit", y="cnt", data=day)
        plt.title("Pengaruh Weathersit Terhadap Jumlah Sewa Sepeda Harian")
        plt.xlabel("Weathersit")
        plt.ylabel("Jumlah Sewa Sepeda Harian")
    
        # Display the selected plot using Streamlit
        st.pyplot()

        # Explanation
        st.write("""
        Berdasarkan boxplot di atas dapat disimpulkan bahwa jumlah sewa sepeda mengingkat 
        ketika cuaca Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian. 
        """)
    
        st.write("""
        Cuaca yang cerah atau berawan sebagian dapat memberikan kondisi lalu lintas yang lebih baik dan visibilitas yang lebih tinggi,
        yang dapat meningkatkan rasa aman bagi para penyewa sepeda. Selain itu, suhu yang nyaman pada kondisi cuaca tersebut membuat bersepeda lebih menyenangkan.
        """)