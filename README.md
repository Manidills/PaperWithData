# PaperWithData

<!-- PROJECT LOGO -->

<br />
<div align="center">
    <a href="https://ibb.co/c2J0Fwy"><img src="https://i.ibb.co/c2J0Fwy/Add-a-heading.png" alt="Add-a-heading" border="0"></a>
  <h3 align="center">PaperWithData</h3>
  * Deployed URL (Try mozila/opera for best view) : https://huggingface.co/spaces/dills1/PaperwithData
</div>

## Problems

* Not much AI + Blockchain projects are getting to live,due to lack of research.

* Finding quality data on blockchain space is very hard, so that many AI researchers not much into it.

* Currently no central place to learn or get the data/papers/AI model for web3 space. 

* Many people stuggling to find the correct resource that bridge AI + Blockchain space together.

## Solution
```sh
PaperWithData

1. PaperWithData is a DATA DAO, that provide AI integrated Web3 papers/datasets/AI models based on different categories.

2. PaperWithData comes as a web application and API as a service.

3. It tried to solve the gap between AI researcher/dev and blockchain space.

4. Central place that helps to data analysts, data scientiest, data reseachers, ML/DL devs.

5. IPFS + FVM += Fire
```

## Design
<div align="center">

  <a href="https://i.postimg.cc/44hq56Hr/D-2-1.jpg"><img src="https://i.postimg.cc/44hq56Hr/D-2-1.jpg" alt="Add-a-heading" border="0" width="700" height="500"></a>
</div>

  * Users -
  
    1. Initially user need to connect there wallet on **filecoin chain** to login ( current deployment under hyperspace testnet )
    
    2. They can view or download any papers/datasets/AI models based on there search.
    
    3. They dont have permission to upload or validate new papers/datasets/models to PaperWithCode.
    
  * Community -
  
    1. They have permission to upload papers/datasets/models to PaperwithData.
    
    2. They are the validators, who can check the uploads and **vote** if its seems fine to get into PaperWithData.
    
    3. Each data need to pass at least **2 votes currently** to get inside to FVM chain, **our contracts take care of the votings and approval**.
    
    4. Once it got approved by our community peoples, it pushed to **FVM**.
    
    5. Community people will get our **PWD token, swag and more prizes** each month based on there activities. It ensure both filecoin network and PaperWithCode more engaged over time.


# Stack

PaperWithData comes with the **API as a service model**, who can use oue api to get datas and push data for approval. Internal APIs that only works for community peoples to vote and validate the datas.

Our current daily pipeline on run to grab different papers/datasets/models from various places that also validate by our community and contracts. Currently we using **vote_and_approve.sol, paperwithdata.sol, pwd.sol ( erc20 )**, yet to add more contracts. 

<div align="center">

  <a href="https://i.postimg.cc/SKndb1vS/fvm-api.png"><img src="https://i.postimg.cc/SKndb1vS/fvm-api.png" alt="Add-a-heading" border="0" width="1200" height="500"></a>
</div>

1. APIs - FASTAPI (Python)

2. Webapp ( Alpha ) - Streamlit on https://huggingface.co/ 

3. Storage - IPFS ( Lighthouse , NFT storage, web3 storage )

# Sample Screenshot -

<a href="https://i.postimg.cc/gYgPKwpm/fvm-1.png?dl=1"><img src="https://i.postimg.cc/gYgPKwpm/fvm-1.png?dl=1" alt="Add-a-heading" border="0" width="1000" height="500"></a>

<a href="https://i.postimg.cc/ZRVRmms2/fvm-7.png"><img src="https://i.postimg.cc/ZRVRmms2/fvm-7.png" alt="Add-a-heading" border="0" width="1000" height="500"></a>

<a href="https://i.postimg.cc/D2y9m2XD/fvm-2.png?dl=1"><img src="https://i.postimg.cc/D2y9m2XD/fvm-2.png?dl=1" alt="Add-a-heading" border="0" width="1000" height="500"></a>

<a href="https://i.postimg.cc/1SYQnNMK/fvm-3.png?dl=1"><img src="https://i.postimg.cc/1SYQnNMK/fvm-3.png?dl=1" alt="Add-a-heading" border="0" width="1000" height="500"></a>

<a href="https://i.postimg.cc/Z46tMsmf/fvm-4.png?dl=1"><img src="https://i.postimg.cc/Z46tMsmf/fvm-4.png?dl=1" alt="Add-a-heading" border="0" width="1000" height="500"></a>

<a href="https://i.postimg.cc/9VRjGFnH/fvm-5.png?dl=1"><img src="https://i.postimg.cc/9VRjGFnH/fvm-5.png?dl=1" alt="Add-a-heading" border="0" width="1000" height="500"></a>

<a href="https://i.postimg.cc/4XzfpNnx/fvm-6.png?dl=1"><img src="https://i.postimg.cc/4XzfpNnx/fvm-6.png?dl=1" alt="Add-a-heading" border="0" width="1000" height="500"></a>







    

