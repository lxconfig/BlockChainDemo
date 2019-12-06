'use strict';

// keys/allKeys
// keys 返回对象的所有key，不包括继承的
// allKeys 返回包括继承的所有key
function Student(name, age) {
    this.name = name;
    this.age = age;
};
Student.prototype.school = 'No.1 Middle School';
var xiaoming = new Student('小明', 12);
console.log(_.keys(xiaoming));
console.log(_.allKeys(xiaoming));

// values 返回对象的所有的value，不包括继承的
console.log(_.values(xiaoming));

// invert
// 键变为值，值变为键
console.log(_.invert(xiaoming));

// extend / extendOwn
// extend 把多个对象的key-value合并到第一个对象中
// 重复的key会被覆盖
var a = {name: 'xx', age: 34, gender: 'n'};  // a改变
console.log(_.extend(a, xiaoming, {tel: 123, skill: 'study'}));

// clone
// 复制（浅赋值）一个对象
// 修改copied，也会修改xiaoming
var copied = _.clone(xiaoming);
console.log(copied);