/*
 * @Author: lixuan
 * @Date: 2019-11-11 16:11:18
 * @LastEditTime: 2019-11-11 16:11:19
 * @Description: 
 */
'use strict'
var App = {

    web3Provider: null,
    contracts: {},

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
        $.getJSON('InfoContract.json', function (data) {  // 通过回调拿到json的内容
            App.contracts.InfoContract = TruffleContract(data);  // 得到TruffleContract的对象
            App.contracts.InfoContract.setProvider(App.web3Provider);
            App.getInfo();
        });
        App.bindEvents();
    },

    getInfo: function () {
        App.contracts.InfoContract.deployed().then(function (instance) {
            //通过TruffleContract对象的deployed()得到合约的实例对象instace
            return instance.getInfo.call();
        }).then(function (result) {
            // 在then()中拿到上一个return的返回值
            $("#loader").hide();
            $("#info").html(result[0] + "(" + result[1] + "years old)");
            console.log(result);
        }).catch(function (err) {
            console.error(err);
        });
    },

    bindEvents: function () {
        $("#button").click(function () {
            var name = $('#name').val();
            var age = $('#age').val();
            $("#loader").show();
            App.contracts.InfoContract.deployed().then(function (instance) {
                return instance.setInfo.sendTransaction(name, age, {from: web3.eth.defaultAccount});
            }).then(function (result) {
                return App.getInfo();
            }).catch(function (err) {
                console.error(err);
            });
        });
    }
};


$(function () {
    $(window).load(function () {
        App.init();
    });
});