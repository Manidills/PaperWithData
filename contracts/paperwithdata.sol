
// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

contract DataStore {
struct Dataset {
string name;
string ipfshash;
uint voterCount;
}

struct Model {
    string name;
    string ipfshash;
    uint voterCount;
}

struct Paper {
    string name;
    string ipfshash;
    uint voterCount;
}

mapping(string => Dataset) datasets;
mapping(string => Model) models;
mapping(string => Paper) papers;

function storeDataset(string memory _name, string memory _ipfshash) public {
    require(datasets[_name].voterCount > 1, "Voter count not met.");
    datasets[_name] = Dataset(_name, _ipfshash, 0);
}

function storeModel(string memory _name, string memory _ipfshash) public {
    require(models[_name].voterCount > 1, "Voter count not met.");
    models[_name] = Model(_name, _ipfshash, 0);
}

function storePaper(string memory _name, string memory _ipfshash) public {
    require(papers[_name].voterCount > 1, "Voter count not met.");
    papers[_name] = Paper(_name, _ipfshash, 0);
}

function retrieveDataset(string memory _name) public view returns (string memory, string memory) {
    return (datasets[_name].name, datasets[_name].ipfshash);
}

function retrieveModel(string memory _name) public view returns (string memory, string memory) {
    return (models[_name].name, models[_name].ipfshash);
}

function retrievePaper(string memory _name) public view returns (string memory, string memory) {
    return (papers[_name].name, papers[_name].ipfshash);
}

function voteDataset(string memory _name) public {
    datasets[_name].voterCount++;
}

function voteModel(string memory _name) public {
    models[_name].voterCount++;
}

function votePaper(string memory _name) public {
    papers[_name].voterCount++;
}
}