import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("https://raw.githubusercontent.com/Bovendiska/Tugas-Akhir/main/all_data.csv")

def create_bystate_df(df):
    bystate_df = all_df.groupby(by="customer_state").Arrived.nunique().reset_index()
    bystate_df.rename(columns={
            "customer_id": "customer_count"
    }, inplace=True)
    
    return bystate_df

def create_bycity_df(df):
    bycity_df = all_df.groupby(by="customer_city").Arrived.nunique().reset_index()
    bycity_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    
    return bycity_df

bystate_df = create_bystate_df(all_df)
bycity_df = create_bycity_df(all_df)

st.header('Dicoding Collection Dashboard :sparkles:')

# Assuming you have defined 'bycity_df' and 'bystate_df' DataFrames before this code block
# Assuming 'st' is the Streamlit module

st.subheader("Customer By City")

# Plotting for Customer by City
fig, ax = plt.subplots(figsize=(20, 10))
bycity_df_sorted = bycity_df.sort_values(by="Arrived", ascending=False)

# Take the top 10 cities
top_10_cities = bycity_df_sorted.head(10)

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="Arrived", 
    x="customer_city",
    data=top_10_cities,  # Use the top 10 cities DataFrame
    palette=colors,
    ax=ax,
    dodge=2.0
)
ax.set_title("Number of Customer by City", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("Customer By State")
# Plotting for Customer by States
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="Arrived", 
    y="customer_state",
    data=bystate_df.sort_values(by="customer_state", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customer by States", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("Kesimpulan :")
st.subheader("1. Kota mana yang memiliki customer paling banyak? Sao Paulo")
st.subheader("2. State mana yang memiliki customer paling banyak? SP")