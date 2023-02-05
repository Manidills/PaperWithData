
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





def get_datasets(search_word):

    with open('datasets/data_sets.json') as json_file:
        data = json.load(json_file)
        select_data = [ key  for key, values in data.items() if  key.startswith(search_word)]
        contract = get_contract()
        call_papers = [contract.functions.retrieveDataset(i).call() for i in select_data ]

        for idx,i in enumerate(call_papers):

            col1, col2 = st.columns((3,1))
            with col1:
                st.markdown('#')
                
                
                #     st.markdown(f"""
                # <embed src="https://{i[1]}.ipfs.nftstorage.link/" width="1200" height="600">
                # """, unsafe_allow_html=True)
                url = f"https://{i[1]}.ipfs.nftstorage.link/"
                response = requests.get(url)
            

                data = pd.read_csv(io.StringIO(response.text))

                st.write(data.head())
            with col2:
                st.download_button(label=f"Download dataset_{idx}",data =  requests.get(f"https://{i[1]}.ipfs.nftstorage.link/").content, file_name=f'{i[0]}.csv')

            