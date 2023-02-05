from ctypes import sizeof
import json
from re import search
from data import get_all
from dataset import get_datasets
from models import get_models
from papers import get_papers
import streamlit as st
from upload import upload_ipfs
#from metamask_component import metamask_component
from wallet_connect import wallet_connect
import web3
from abi.abi import get_contract
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time


st.set_page_config(
    page_title="PaperswithFVM",
    layout="wide"
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_download = "https://assets8.lottiefiles.com/packages/lf20_xhlbndhm.json"
lottie_download = load_lottieurl(lottie_url_download)

col1, col2, col3 = st.columns([1,1.5,1])

with col1:
    st.write(' ')
with col2:
    st_lottie(lottie_download, key="hello",width =300)
with col3:
    st.write(' ')




_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])

with col:
    connect_button = wallet_connect(label="wallet", key="wallet")

if connect_button != 'not':
    print(connect_button)


    # Metamask
    #value = metamask_component(account_results="hello there")

    #connect_button = wallet_connect(label="wallet", key="wallet")


    with st.sidebar:
        option = st.radio(
            'Select Category',
            ('All','Papers','Datasets', 'Models', "Upload"))


    if option == "Papers":
        with st.form("form1", clear_on_submit=False): 
            search_word = st.text_input(f'Search here')
            submit = st.form_submit_button("Submit")
        if submit:
            get_papers(search_word)
            st.balloons()
    elif option == "Datasets":
        with st.form("form1", clear_on_submit=False): 
            search_word = st.text_input(f'Search {option} here')
            submit = st.form_submit_button("Submit")
        if submit:
            get_datasets(search_word)
            st.balloons()
    elif option == "Models":
        with st.form("form1", clear_on_submit=False): 
            search_word = st.text_input(f'Search {option} here')
            submit = st.form_submit_button("Submit")
        if submit:
            get_models(search_word)
            st.balloons()
    elif option == "Upload":
        upload_ipfs()

    else:
        with st.form("form1", clear_on_submit=False): 
            search_word = st.text_input(f'Search {option} here')
            submit = st.form_submit_button("Submit")
        if submit:
            get_all(search_word)
            st.balloons()
        





