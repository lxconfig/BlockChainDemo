/*
 * @Author: lixuan
 * @Date: 2019-11-12 14:17:07
 * @LastEditTime: 2019-11-12 14:19:57
 * @Description: MapAndReduce.js
 */
// 高阶函数

'use strict';

// var arr = [1, 2, 3];
// console.log(arr.map(String));


// var a = [1, 2, 3];

// function pow(x) {
//     return x + x;
// }
// console.log(a.map(pow));

// var b = [1, 3, 4, 5];

// function sum(x, y) {
//     return x + y;
// }

// function Muti(x, y) {
//     return x * y;
// }

// console.log(b.reduce(Muti));

// 字符串变为数字
var strings = "13579";
var arr = strings.split("");
console.log(arr);
var xx = arr.map(function (x) {
    return x * 1;
});
console.log(xx.reduce(function (x, y) {
    return x*10 + y;
}));

// 首字母大写，其余字母小写
let names = ['adam', 'LISA', 'barT'];
console.log(names.map(function (x) {
    var y = x[0].toUpperCase();
    var z = (x.substring(1, x.length)).toLowerCase();
    return y+z;
}));