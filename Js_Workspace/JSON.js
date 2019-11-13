/*
 * @Author: lixuan
 * @Date: 2019-11-13 15:24:48
 * @LastEditTime: 2019-11-13 15:44:46
 * @Description: JSON
*/

'use strict';
// 序列化
var xiaoming = {
    name: "小王吧",
    age: 35,
    gender: "男",
    favorite: ["Sing", "Dancing", "Rap", "Basketball"],
    skills: ["Coding", "Programing", "Playing"],
    hight: "172cm",
    weight: "90Kg"
};
// console.log(JSON.stringify(xiaoming, ["name", "skills", "favorite"], ' '));

function convert(key, value) {
    if (typeof value === 'string') {
        return value.toUpperCase();
    }
    return value;
}

// console.log(JSON.stringify(xiaoming, convert, ' '));


var xiaohei = {
    name: "小王吧",
    age: 35,
    gender: "男",
    favorite: ["Sing", "Dancing", "Rap", "Basketball"],
    skills: ["Coding", "Programing", "Playing"],
    hight: "172cm",
    weight: "90Kg",
    toJSON: function () {
        return {
            'Name': this.name,
            "Age": this.age
        };
    }
};
var serialized = JSON.stringify(xiaohei, null, " ")
// console.log(serialized);


// 反序列化
// console.log(JSON.parse(serialized));
