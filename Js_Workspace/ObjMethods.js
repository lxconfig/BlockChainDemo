'use strict';
// 对象中绑定函数，称为方法
// var xiaoming = {
//     name: "小明",
//     birth: 1990,
//     age: function () {
//         var y = new Date().getFullYear();
//         return y - this.birth;
//     }
// };

// console.log(xiaoming.age);   // [Function: age]
// console.log(xiaoming.age());  // 29


function getAge(z) {
    var y = new Date().getFullYear();
    return y - this.birth - z;
}

var xiaoming = {
    name: "小明",
    birth: 1990,
    age: getAge
};

console.log(xiaoming.age(3)); // 29
console.log(getAge.apply(xiaoming, [3]));   // NaN

// 先用that获取到对象
// var xiaoming = {
//     name: "小明",
//     birth: 1990,
//     age: function () {
//         var that = this;
//         function getAgeFromBirth() {
//             var y = new Date().getFullYear();
//             return y - that.birth;
//         }
//         return getAgeFromBirth();
//     }
// };

// console.log(xiaoming.age());
// console.log(xiaoming.age);