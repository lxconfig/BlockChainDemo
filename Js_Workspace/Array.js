/*
 * @Author: lixuan
 * @Date: 2019-12-03 15:14:37
 * @LastEditTime: 2019-12-09 17:27:45
 * @Description: underscore 中的 Array 相关方法
 */
'use strict';
// first/last
// first取第一个元素
// last取最后一个元素
var arr = [2,4,6,8,5,1];
var r1 = _.first(arr);
var r2 = _.last(arr);
console.log(r1, r2);

// flatten
// 把传入的一维或N维数组变成一维数组
var r3 = _.flatten([1, [3], [1, [23]], [7]]);
console.log(r3);

// zip/unzip/object
// zip把两个或多个元素按索引合并成新数组
// unzip是zip的反过程
// object类似zip,但返回的是Object对象
var names = ['bob', 'lisa', 'bart'];
var scores = ['94', '24', '34'];
var r4 = _.zip(names, scores);
var r5 = _.object(names, scores);
console.log(r4, r5);

// range
// 快速生成一个序列
var r6 = _.range(1, 10);
console.log(r6);

// uniq
// 去重
var arr = ['Apple', 'orange', 'banana', 'ORANGE', 'apple', 'PEAR'];
var result = _.uniq(arr);
console.log(result);