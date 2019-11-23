/*
 * @Author: lixuan
 * @Date: 2019-11-23 10:10:46
 * @LastEditTime: 2019-11-23 13:07:58
 * @Description: Synchronous and Asynchronous
*/
'use strict';

// callback  function

// function a() {
//     console.log("a function is running...");
// }

// function b(callback) {
// 	setTimeout(function () {
//         // b函数执行
//         console.log("b function is running...");
// 		callback();  // a函数执行
// 	}, 2000);
// }
// b(a);

// Promise
// var p = new Promise(function (resolve, reject) {
//     setTimeout(function() {
//         console.log("success");
//         resolve("xxxxxxx");
//     }, 2000);
// });

// 通常用函数包装一个Promise对象 (调用resolve的情况)

function runAsync() {
    var pro = new Promise(function (resolve, reject) {
        setTimeout(function() {
            console.log("runAsync");
            resolve("xxxxxxx");
        }, 2000);
    });
    return pro;  // 需要返回Promise对象
}

function runAsync2() {
    var asy = new Promise(function (resolve, reject) {
        setTimeout(function() {
            console.log("runAsync2");
            resolve("yyyyyyyyy");
        }, 1000);
    });
    return asy;
}
// runAsync().then(function(data) {
//     console.log(data);
//     return runAsync2();
// }).then(function (data) {
//     console.log(data);
// })
// Promise.all([runAsync(), runAsync2()]).then(function (data) {
//     console.log(data);
// })

Promise.race([runAsync(), runAsync2()]).then(function (data) {
    console.log(data);
})

// (调用reject的情况)

// function math() {
//     var ma = new Promise(function (resolve, reject) {
//         setTimeout(function() {
//             var num = Math.random() * 2;
//             if (num < 1) {
//                 console.log("num=" + num);
//                 resolve("success!");
//             } else {
//                 console.log("num=" + num);
//                 reject("failed!");
//             }
//         }, 2000);
//     });
//     return ma;
// }
// math().then(function (data) {
//     console.log("resolve, " + data);
//     console.log(ssss);
// }).catch(function (data) {
//     console.log("reject, " + data);
// })