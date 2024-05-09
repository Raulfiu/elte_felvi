import pandas as pd
import streamlit as st


# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="./data/orsz_jelentk_adatok_2010_tol.xlsx",
        engine="openpyxl",
        sheet_name="data",
        # skiprows=3,
        # usecols="B:R",
        # nrows=1000,
    )
    df['ev'] = df['ev'].astype(str)
    # Add 'hour' column to dataframe
    # df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df