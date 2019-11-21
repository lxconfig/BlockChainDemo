'use strict'
var App = {

    web3Provider: null,
    Voting: null,

    init: function () {
        return App.initWeb3();
    },

    initWeb3: function () {
        // 初始化web3
        if (typeof web3 !== "undefined") {
            App.web3Provider = web3.currentProvider;
            web3 = new Web3(App.web3Provider);
        } else {
            App.web3Provider = new Web3.providers.HttpProvider("http://127.0.0.1:7545");
            web3 = new Web3(App.web3Provider);
        }
        return App.initContract();
    },

    initContract: function () {
        // 初始化合约
        // 通过 truffle compile 得到的json文件
        $.getJSON('Voting.json', function (data) {  // 通过回调拿到json的内容
            App.Voting = TruffleContract(data);  // 得到TruffleContract的对象
            App.Voting.setProvider(App.web3Provider);
            return App.initData();
        });
        $("#vote").on("click", App.voteForCandidate);
    },

    initData: function () {
        let candidates = {"Rama": "candidate-1", "Nick": "candidate-2", "Jose": "candidate-3"};
        let candidateNames = Object.keys(candidates);
        for (var i=0; i<candidateNames.length; i++) {
            let name = candidateNames[i];
            // 通过deployed()拿到合约对象
            App.Voting.deployed().then(function(contractInstance) {
                return contractInstance.totalVotesFor(name);
            }).then(function(v) {
                console.log(v);
                $("#" + candidates[name]).html(v.toString());
            }).catch(function(err) {
                console.log(err.message);
            });
        }
    },

    voteForCandidate: function () {
        let candidateName = $("#candidate").val();
        App.Voting.deployed().then(function(contractInstance) {
            return contractInstance.voteForCandidate(candidateName);
        }).then(function(v) {
            App.initData();
        }).catch(function(err) {
            console.log(err.message);
        });
    }
};


$(function () {
    $(window).load(function () {
        App.init();
    });
});