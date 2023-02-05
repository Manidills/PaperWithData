
import json
from re import search
import streamlit as st
#from metamask_component import metamask_component
from wallet_connect import wallet_connect
import web3
from abi.abi import get_contract
import requests





def get_papers(search_word):

    with open('datasets/papers_ipfs.json') as json_file:
        data = json.load(json_file)
        select_data = [ key  for key, values in data.items() if  key.startswith(search_word)]
        contract = get_contract()
        call_papers = [contract.functions.retrievePaper(i).call() for i in select_data ]

        for i in call_papers:
            st.markdown('#')
            col1,col2 = st.columns((3,1))
            with col1:
                st.markdown(f"""
            <embed src="https://{i[1]}.ipfs.nftstorage.link/" width="1200" height="600">
            """, unsafe_allow_html=True)
           


