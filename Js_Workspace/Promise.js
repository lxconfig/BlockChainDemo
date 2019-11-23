/*
 * @Author: lixuan
 * @Date: 2019-11-22 15:20:53
 * @LastEditTime: 2019-11-22 17:01:53
 * @Description: promise
*/
'use strict';
// function callback() {
//     console.log("done");
// }
// console.log("before callback");
// setTimeout(callback, 2000);
// console.log("after setTimeout()");

function test(resolve, reject) {
    var timeOut = Math.random() * 2;
    console.log('set timeout to: ' + timeOut + ' seconds.');
    setTimeout(function () {
        if (timeOut < 1) {
            console.log('call resolve()...');
            resolve('200 OK');
        }
        else {
            console.log('call reject()...');
            reject('timeout in ' + timeOut + ' seconds.');
        }
    }, timeOut * 1000);
}

var p1 = new Promise(test).then(function (result) {
    console.log('成功：' + result);
}).catch(function (reason) {
    console.log('失败：' + reason);
});

// console.log(typeof p1);