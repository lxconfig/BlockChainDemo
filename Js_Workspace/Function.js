/*
 * @Author: lixuan
 * @Date: 2019-12-06 10:12:14
 * @LastEditTime: 2019-12-06 10:28:06
 * @Description: underscore 中的 Function 相关方法
*/

'use strict';

// memoize
// 把某个函数的结果缓存
var factorial = _.memoize(function (n) {
    console.log('start calculate ' + n + '!...');
    var s = 1, i = n;
    while (i > 1) {
        s = s * i;
        i--;
    }
    console.log(n + '! = ' + s);
    return s;
});
factorial(10);
factorial(10);  // 控制台不会再输出

// once
// 保证某函数仅调用一次
var register = _.once(function () {
    alert('register ok');
});
// register();
// register();
// register();

// delay
// 类似setTimeout
var l = _.delay(function (n) {
    console.log(n);
}, 1000, '100');
console.log(l);