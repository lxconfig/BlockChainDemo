/*
 * @Author: lixuan
 * @Date: 2019-11-14 14:18:05
 * @LastEditTime: 2019-11-14 14:44:35
 * @Description: 用构造函数来创建对象
*/

'use strict';

function Student(name) {
    this.name = name;
    // Student.prototype.hello = function () {
    //     console.log("hello, " + this.name + "!");  // xiaoming  xiaohong  共享hello方法
    // }
    this.hello = function () {
        console.log("hello, " + this.name + "!");
    }
}

var xiaoming = new Student('小明');
var xiaohong = new Student('小红');
console.log(xiaoming.name);
xiaoming.hello();
console.log(xiaoming.__proto__);  // Student {}
console.log(xiaoming.constructor);  // [Function: Student]

console.log(Student.prototype);  // Student {}
console.log(xiaoming.hello === xiaohong.hello);