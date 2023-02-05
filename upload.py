import streamlit as st
import nft_storage
from nft_storage.api import nft_storage_api
from io import BytesIO


def nft_storage_store(file_name):
        # Defining the host is optional and defaults to https://api.nft.storage
        # See configuration.py for a list of all supported configuration parameters.
        configuration = nft_storage.Configuration(
            host="https://api.nft.storage"
        )

        configuration = nft_storage.Configuration(
            access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDE0RkY4NTU4MzVGMDYwZDBCRTk0ZWQyOTBjNTdiODE1YTE5MjQxNUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1NzU2OTU4ODQxOSwibmFtZSI6Ik1BTklESUxMUyJ9.idaK-qJVyOb8WKP1cD0yddE8UJX4zRpBKtX-QqN49fU'
        )
        with nft_storage.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = nft_storage_api.NFTStorageAPI(api_client)
          
            body = file_name.read()
            body = BytesIO(body)
            #body = open(file_name, 'rb')  # file_type |


            # example passing only required values which don't have defaults set
            try:
                # Store a file
                api_response = api_instance.store(body, _check_return_type=False)
                return (api_response)
            except nft_storage.ApiException as e:
                st.info("Exception when calling NFTStorageAPI->store: %s\n" % e)

def upload_ipfs():

    st.title("Upload Papers/Datasets/Models with proper filename")
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        ipfs_store = nft_storage_store(uploaded_file)
        st.write(ipfs_store['value'])
        st.info("Thanks for uploading the data, Our community validators will validate and approve the data")
        st.markdown("#")
        st.success("Do check #PaperWithData in twitter to join our community to grab tokens, swag and more prizes")
        st.balloons()