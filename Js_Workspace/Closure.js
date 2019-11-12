/*
 * @Author: lixuan
 * @Date: 2019-11-12 14:22:38
 * @LastEditTime: 2019-11-12 15:40:26
 * @Description: Closure.js  闭包
 */


 function lazy_sum(arr) {
     let a = 2;
     var sum = function () {
         return arr.reduce(function(x, y) {
            return x + y + a; 
         });
     }
     return sum;
 }

 var ff = lazy_sum([1,3,4]);
 console.log(ff);  // ff是一个函数对象
 console.log(ff());  // 调用函数对象ff


 function count() {
    var arr = [];
    for (let i=1; i<=3; i++) {
        arr.push(function () {
            return i * i;
        });
    }
    return arr;
}

var results = count();
var f1 = results[0];
var f2 = results[1];
var f3 = results[2];
console.log(f1());
console.log(f2());
console.log(f3());


var name = "The Window";

var object = {
　　name : "My Object",

　　getNameFunc : function(){
       var that = this;
　　　　return function(){
　　　　　　return that.name;
　　　　};
　　}
};

console.log(object.getNameFunc()());