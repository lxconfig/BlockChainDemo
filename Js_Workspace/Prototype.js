/*
 * @Author: lixuan
 * @Date: 2019-11-14 10:53:29
 * @LastEditTime: 2019-11-14 11:05:45
 * @Description: 通过原型来实现面向对象编程
*/

'use strict';
// __proto__方法
var Student = {
    name: "robot",
    age: 1,
    run: function () {
        console.log(this.name + "is running...");
    }
};

var xiaoming = {
    name: "小明"
};

xiaoming.__proto__ = Student;

console.log(xiaoming.name);
console.log(xiaoming.age);
xiaoming.run();

// Obeject.create()方法
var Bird = {
    name: "bird",
    weight: '100g',
    fly: function() {
        console.log(this.name + "is flying...");
    }
};
function createBird(name) {
    var New_obj = Object.create(Bird);
    // console.log(New_obj.name);
    New_obj.name = name;
    return New_obj;
}

var xiaoniao = createBird("小鸟");
console.log(xiaoniao.name);
console.log(xiaoniao.weight);
xiaoniao.fly();
console.log(xiaoniao.__proto__ === Bird);
