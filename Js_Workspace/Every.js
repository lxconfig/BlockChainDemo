/*
 * @Author: lixuan
 * @Date: 2019-11-11 13:33:16
 * @LastEditTime: 2019-11-11 13:34:43
 * @Description: Every.js
 */
'use strict';
 var arr = ['Apple', "orange", "Pear"];
 var s = arr.every(function(x) {
     return x.length > 0;
 });

 console.log(s);
