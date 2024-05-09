import streamlit as st

def pageConf():
    st.set_page_config(page_title="SZE Felveteli adatok 2010-2022", page_icon=":bar_chart:", layout="wide")
    # A felso nagy ures hely csokkentese
    st.markdown("""
            <style>
                .block-container {
                        padding-top: 1rem;
                        padding-bottom: 0rem;
                        padding-left: 10rem;
                        padding-right: 10rem;

                    }
            </style>
            """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .stTextInput > label {
                font-size:10%; 
                font-weight:bold; 
                color:yellow;
            }
            .stMultiSelect > label {
                font-size:10%; 
                font-weight:bold; 
                color:red;
            } 
        </style>
        """, unsafe_allow_html=True)
    # st.markdown(
    #     """
    #     <style>
    #         section[data-testid="stSidebar"] {
    #             padding-top: -5rem;
    #             margin-left:0   rem;                    
    #             padding-left: -20rem;
    #             padding-right: -5rem;
    #         }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    return st



