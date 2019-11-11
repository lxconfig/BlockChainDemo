/*
 * @Author: your name
 * @Date: 2019-11-11 13:15:25
 * @LastEditTime: 2019-11-11 13:15:25
 * @LastEditors: your name
 * @Description: In User Settings Edit
 * @FilePath: /firstTruffleDemo/home/lixuan/code/Js_Workspace/Filter.js
 */


var arr = [1,3,4,5,2,6,7,9,5,10]
var r = arr.filter(function(x) {
    return x % 2 == 0;
});
console.log(r);


// 对数组去重
var s = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];
var q = s.filter(function(element, index, self) {
    return self.indexOf(element) === index;  // indexOf总是返回元素第一次出现的位置
});

console.log(q);

var num = 24;
var yz = []
for (var i=1; i<=num; i++) {
    if (num % i === 0) {
        yz.push(i);
    }
}
if (yz.length == 2) {
    console.log(num + '是素数');
} else {
    console.log(num + "不是素数");
}


return arr.filter(function(x) {
    var num = []
    for (var i=1; i<=x; i++) {
        if (x % i == 0) {
            num.push(i);
        }
    }
    if (num.length == 2) {
        return true;
    } else {
        return false;
    }
});