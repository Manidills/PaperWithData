
import json
from re import search
import streamlit as st
#from metamask_component import metamask_component
from wallet_connect import wallet_connect
import web3
from abi.abi import get_contract
import requests
import pandas as pd
import io





def get_models(search_word):

    with open('datasets/models.json') as json_file:
        data = json.load(json_file)
        select_data = [ key  for key, values in data.items() if  key.startswith(search_word)]
        contract = get_contract()
        call_papers = [contract.functions.retrieveModel(i).call() for i in select_data ]

        for idx,i in enumerate(call_papers):

            col1, col2 = st.columns((3,1))
            with col1:
                st.markdown('#')
            
                st.write(f"{i[0]}_volume_202{idx}".upper())
            with col2:
                st.download_button(label=f"Download Models_{idx}",data =  requests.get(f"https://{i[1]}.ipfs.nftstorage.link/").content, file_name=f'{i[0]}.h5')

            