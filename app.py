import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Setup ---
st.set_page_config(page_title="Flight Pricing Dashboard", layout="wide")
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 11, 'axes.labelcolor': '#2C3E50', 'axes.titlesize': 14})

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("dataset/airlines_flights_data.csv")
    return df

df = load_data()

# --- Sidebar ---
st.sidebar.header("🔎 Filter Data")
selected_airline = st.sidebar.multiselect("✈️ Airline", df["airline"].unique(), default=df["airline"].unique())
selected_class = st.sidebar.multiselect("💺 Class", df["class"].unique(), default=df["class"].unique())
selected_source = st.sidebar.multiselect("🛫 Source City", df["source_city"].unique(), default=df["source_city"].unique())
selected_dest = st.sidebar.multiselect("🛬 Destination City", df["destination_city"].unique(), default=df["destination_city"].unique())

filtered_df = df[
    (df["airline"].isin(selected_airline)) &
    (df["class"].isin(selected_class)) &
    (df["source_city"].isin(selected_source)) &
    (df["destination_city"].isin(selected_dest))
]

# --- Title Section ---
st.title("📊 Flight Pricing Analysis Dashboard")
st.markdown("A data-driven dashboard to analyze airline pricing trends across various features.")

st.markdown("---")

# --- Preview Table ---
st.markdown("### 📋 Filtered Dataset Preview")
st.dataframe(filtered_df.head(), use_container_width=True)

st.markdown("---")

# --- Charts Section ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💸 Price Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df["price"], kde=True, color="#2980B9", ax=ax1)
    ax1.set_title("Distribution of Flight Prices")
    ax1.set_xlabel("Price (₹)")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

with col2:
    st.markdown("### 🏷️ Price by Airline")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x="airline", y="price", palette="Blues", ax=ax2)
    ax2.set_title("Price Comparison Across Airlines")
    ax2.set_xlabel("Airline")
    ax2.set_ylabel("Price (₹)")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### ⏱️ Duration vs Price")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=filtered_df, x="duration", y="price", hue="class", palette="cool", ax=ax3)
    ax3.set_title("Flight Duration vs Price")
    ax3.set_xlabel("Duration (hrs)")
    ax3.set_ylabel("Price (₹)")
    st.pyplot(fig3)

with col4:
    st.markdown("### 🕐 Avg Price by Departure Time")
    avg_dep = filtered_df.groupby("departure_time")["price"].mean().sort_values()
    fig4, ax4 = plt.subplots()
    avg_dep.plot(kind="bar", color="#5DADE2", ax=ax4)
    ax4.set_title("Average Price vs Departure Time")
    ax4.set_ylabel("Price (₹)")
    ax4.set_xlabel("Departure Time")
    st.pyplot(fig4)

st.markdown("---")

st.markdown("### 📈 Correlation Heatmap")
corr = filtered_df[["price", "days_left"]].corr()
fig5, ax5 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="PuBuGn", ax=ax5)
ax5.set_title("Correlation Matrix")
st.pyplot(fig5)

# --- Footer ---
st.markdown("---")
