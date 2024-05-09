import streamlit as st
import plotly.express as px  # pip install plotly-express
import plotly.graph_objects as go
# import uuid
import styles as sty #oldal konfigurálása, style elemek benne
# import getData as gd
from streamlit_gsheets import GSheetsConnection

# oldal konfigurálása
sty.pageConf()

# google sheets connection
# https://docs.streamlit.io/knowledge-base/tutorials/databases/private-gsheet
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="data")

# A pandas adatset beolvasása
# df = gd.get_data_from_excel()

st.header("Országos és SZE-szintű jelentkezési és felvételi adatok 2010-től")
# st.markdown("##")
st.subheader("Felvételi adatok 2010-től")


# container = st.container()
# all = st.button("Select all")
     
# if all:
#     selected_options_3 = container.multiselect("Select one or more options:",
#             ['A', 'B', 'C'],['A', 'B', 'C'], key='option_3')
# else:
#     selected_options_3 =  container.multiselect("Select one or more options:",
#             ['A', 'B', 'C'], key='option_3')


# szűrők main content
column11, column12, column13, column14 = st.columns(4)


with column11:
    with st.expander("Év"):
        selected_ev = st.multiselect(
            label="",
            options=df['ev'].unique(),
            default=df['ev'].unique()
        )

with column12:
    with st.expander("Eljárás"):
        selected_eljaras = st.multiselect(
            label="",
            options=df['eljaras'].unique(),
            default=df['eljaras'].unique()
            )

with column13:
    with st.expander("Intézmény"):
        selected_intezmeny = st.multiselect(
            label="",
            options=df['intezmeny'].unique(),
            # default=['SZE']
            default=df['intezmeny'].unique()
        )

with column14:
    with st.expander("Képzési terület"):
        selected_kepz_terulet= st.multiselect(
            label="",
            options=df['kepz_terulet'].unique(),
            default=df['kepz_terulet'].unique()
        )


# A szűrőn beállított adatok leszűrése a pd adatszeten
df_selection = df.query(
    # "City == @city & Customer_type ==@customer_type & Gender == @gender"
    "ev== @selected_ev & eljaras== @selected_eljaras & intezmeny== @selected_intezmeny & kepz_terulet== @selected_kepz_terulet"
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

# Bar chart 
sum_by_year = df_selection.groupby('ev')[['osszes_jelentkezo', 'elsohelyes', 'felvettek']].sum().sort_values(by="osszes_jelentkezo").reset_index()

fig = px.bar(sum_by_year, 
             x='ev', 
             y=['osszes_jelentkezo', 'felvettek', 'elsohelyes'],
            barmode="group",
            text_auto=".2d",
            height=400,
            # title="Felvettek száma 2010-től"
            )

fig.update_xaxes(type='category')
fig.update_layout(xaxis={'categoryorder':'category ascending'})

st.plotly_chart(fig, use_container_width=True)

# Részletes adatok megtekintője

with st.expander("Adatok előnézete_1"):
    st.dataframe(
        df,
        column_config={"ev": st.column_config.NumberColumn(format="%d")},
    )

# with st.expander("Adatok előnézete_google sheets"):
#     st.dataframe(
#         df1,
#         column_config={"Év": st.column_config.NumberColumn(format="%d")},
#     )

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





