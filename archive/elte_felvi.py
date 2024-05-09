import streamlit as st
import pandas as pd
import plotly.express as px  # pip install plotly-express
import plotly.graph_objects as go
import uuid

# Az oldal konfiguralasa
st.set_page_config(page_title="SZE Felveteli adatok 2010-2022", page_icon=":bar_chart:", layout="wide")

# A felso nagy ures hely csokkentese
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="orsz_jelentk_adatok_2010_tol.xlsx",
        engine="openpyxl",
        sheet_name="data",
        # skiprows=3,
        # usecols="B:R",
        # nrows=1000,
    )
    # Add 'hour' column to dataframe
    # df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

# a szűrő mezők megrajzolása,  FELADAT -> adattal feltölteni
def drawFilters(p1,p2,p3,p4,p5,p6,p7,p8):
    column11, column12, column13, column14 = st.columns(4)
    column21, column22, column23, column24 = st.columns(4)  

    with column11:
        selected_ev = st.multiselect(
            "Év",
            key=uuid.uuid4().hex[:8],
            options=p1
        )

    with column12:
        selected_eljaras = st.multiselect(
            "Eljárás",
            key=uuid.uuid4().hex[:8],
            options=p2
        )

    with column13:
        selected_intezmeny = st.multiselect(
            "Intézmény",
            key=uuid.uuid4().hex[:8],
            options=p3
        )

    with column14:
        selected_szak= st.multiselect(
            "Szak",
            key=uuid.uuid4().hex[:8],
            options=p4
        )

    with column21:
        selected_kepzszint = st.multiselect(
            "Képzési szint",
            key=uuid.uuid4().hex[:8],
            options=p5
        )

    with column22:
        selected_munkarend= st.multiselect(
            "Munkarend",
            key=uuid.uuid4().hex[:8],
            options=p6
        )

    with column23:
        selected_finforma = st.multiselect(
            "Finanszírozási forma",
            key=uuid.uuid4().hex[:8],
            options=p7
        )

    with column24:
        selected_kepzhely = st.multiselect(
            "Képzési hely",
            key=uuid.uuid4().hex[:8],
            options=p8
        )
    return column11

# A szükséges adatsetek szűrése a kimutatásokhoz
df = get_data_from_excel()
df['ev'] = df['ev'].astype(str)

selected_ev_ = drawFilters(df["ev"].unique(),['1'],['1'],['1'],['1'],['1'],['1'],['1'])

selected_df_bar = df.query(
    "ev == @selected_ev_"
)
sum_by_year = selected_df_bar.groupby('ev')[['osszes_jelentkezo', 'elsohelyes', 'felvettek']].sum().sort_values(by="osszes_jelentkezo").reset_index()
sum_by_year['ev'] = sum_by_year['ev'].astype(str)

fig = px.bar(sum_by_year, 
             x='ev', 
             y=['osszes_jelentkezo', 'felvettek', 'elsohelyes'],
            barmode="group",
            text_auto=".2s",
            height=400,
            title="Felvettek száma 2010-től"
            )


# left_column, = st.columns(1)
# left_column.plotly_chart(fig_hourly_sales)


# Cim meghatározása, méretezése
strTitle = r'''$\textsf{\tiny Országos és SZE-szintű jelentkezési és felvételi adatok 2010-től }$'''
strTitle2 = "Országos és SZE-szintű jelentkezési és felvételi adatok 2010-től"
st.title(strTitle)

st.plotly_chart(fig, use_container_width=True)
# st.markdown("##")

# st.image('test_graph_pic.png')


# szűrők



#A szövegméret formázása latex-el

# title = r'''
# $\textsf{
#     \Huge Text \huge Text \LARGE Text \Large Text 
#     \large Text \normalsize Text \small Text 
#     \footnotesize Text \scriptsize Text \tiny Text 
# }$
# '''

# Részletes adatok megtekintője

# st.markdown("### Részletes adatok")
with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={"Év": st.column_config.NumberColumn(format="%d")},
    )

st.markdown("##")

# ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)





