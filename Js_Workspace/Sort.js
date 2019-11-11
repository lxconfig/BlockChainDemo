/*
 * @Author: lixuan
 * @Date: 2019-11-11 13:22:22
 * @LastEditTime: 2019-11-11 13:28:38
 * @Description: Sort.js
 */
'use strict';

var arr = [2,3,1,6,4,0,9,5];
arr.sort(function(x, y) {
    if (x > y) {
        return 1;
    } else if (x < y) {
        return -1;
    }
    return 0;
});

console.log(arr);