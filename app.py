
import streamlit as st
import pandas as pd
import plotly.express as px

# Load KPI data
st.title("📊 NVIDIA Financial KPI Dashboard")

uploaded_file = st.file_uploader("Upload your NVIDIA_KPI_Margins.csv file", type="csv")
if uploaded_file is not None:
    kpi_df = pd.read_csv(uploaded_file)

    # Sidebar filters
    st.sidebar.header("Filters")
    metric = st.sidebar.selectbox("Select KPI", ["Total Revenue", "Gross Profit", "Operating Income", "Net Income"])
    margin = st.sidebar.selectbox("Select Margin", ["Gross Margin (%)", "Operating Margin (%)", "Net Margin (%)", "FCF Margin (%)"])

   # Extract numeric year from Fiscal Year (e.g., 'FY2014' → 2014)
    kpi_df["Year"] = kpi_df["Fiscal Year"].str.replace("FY", "").astype(int)
    min_year = int(kpi_df["Year"].min())
    max_year = int(kpi_df["Year"].max())
    year_range = st.sidebar.slider("Select Fiscal Year Range", min_year, max_year, (min_year, max_year))

    # Filter data
    df_filtered = kpi_df[(kpi_df["Year"] >= year_range[0]) & (kpi_df["Year"] <= year_range[1])]

    # KPI Chart
    st.subheader(f"{metric} Over Time")
    fig_metric = px.line(df_filtered, x="Fiscal Year", y=metric, markers=True)
    st.plotly_chart(fig_metric, use_container_width=True)

    # Margin Chart
    st.subheader(f"{margin} Over Time")
    fig_margin = px.line(df_filtered, x="Fiscal Year", y=margin, markers=True)
    st.plotly_chart(fig_margin, use_container_width=True)

    st.caption("FP&A Dashboard built with Streamlit and Plotly")
else:
    st.warning("📥 Please upload the KPI CSV file to begin.")
