
import json
from re import search
import streamlit as st
#from metamask_component import metamask_component
from wallet_connect import wallet_connect
import web3
from abi.abi import get_contract
import requests





def get_all(search_word):

    with open('datasets/papers_ipfs.json') as json_file:
        data = json.load(json_file)
        select_data = [ key  for key, values in data.items() if  key.startswith(search_word)]
        contract = get_contract()
        call_papers = [contract.functions.retrievePaper(i).call() for i in select_data ]
    
    # with open('datasets/data_sets.json') as json_file:
    #     datasets = json.load(json_file)
    #     datasest_list = [key  for key, values in datasets.items()]
    #     call_datasest =  [contract.functions.retrieveDataset(i).call() for i in datasest_list ]
    
    # with open('datasets/models.json') as json_file:
    #     models = json.load(json_file)
    #     models_list = [key  for key, values in models.items()]
    #     call_model =  [contract.functions.retrieveModel(i).call() for i in models_list ]


        for i in call_papers:
            st.markdown('#')
            col1,col2 = st.columns((5,1))
            with col1:
                st.markdown(f"""
            <embed src="https://{i[1]}.ipfs.nftstorage.link/" width="600" height="600">
            """, unsafe_allow_html=True)
            with col2:
                st.download_button(label=f"Download dataset_{i[0]}",data=  requests.get(f"https://bafybeiclvp2oq24nbmg24yu2dhowa5i6xydpkauhorikmtdxqiv6z65tsy.ipfs.nftstorage.link/").content, file_name=f'{i[0]}.csv')
                st.download_button(label=f"Download model_{i[0]}",data=  requests.get(f"https://bafybeiahbxszypzogd25vwshqi5hjyy2zu3rgakfoqllc3mm6bo3xd2ygq.ipfs.nftstorage.link/").content, file_name=f'{i[0]}.h5')


