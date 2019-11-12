/*
 * @Author: lixuan
 * @Date: 2019-11-12 16:28:52
 * @LastEditTime: 2019-11-12 16:57:15
 * @Description: Generator
 */

'use strict';

// function* fib(max) {
//     var a = 0
//     var b = 1
//     var n = 0;
//     while (n < max) {
//         yield a;
//         [a, b] = [b, a+b];
//         n++;
//     }
//     return;
// }
// var g = fib(5);
// console.log(fib(5));
// console.log(g.next());


// for( var i of fib(5)) {
//     console.log(i);
// }

function* next_id() {
    while (true) {
        yield x;
    }
}

var x, pass=true, g=next_id();
for (x=1; x<3; x++) {
    if (g.next().value !== x) {
        pass = false;
        console.log('failed');
        break;
    }
}
if (pass) {
    console.log("pass");
}