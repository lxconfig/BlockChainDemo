/*
 * @Author: lixuan
 * @Date: 2019-11-12 16:06:33
 * @LastEditTime: 2019-11-13 11:08:24
 * @Description: ArrowFunction.js
 */

'use strict';

var arr = [12,34,5,6,8];
//  var sum = function() {
//      return arr.reduce(function (x, y) {
//          return x + y;
//      })
//  }
var sum = () => arr.reduce((x, y) => x + y)
 
console.log(sum());