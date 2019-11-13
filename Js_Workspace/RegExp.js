/*
 * @Author: lixuan
 * @Date: 2019-11-13 11:07:18
 * @LastEditTime: 2019-11-13 14:52:34
 * @Description: RegExpression
*/

'use strict';

// 创建正则表达式
var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');
// console.log(re1, re2);

// 用正则表达式匹配字符串
var Reg_1 = /^\d{3}\-\d{3,8}$/;
var result1 = Reg_1.test("020-1245135");
console.log(result1);

// 用正则表达式切分字符串
var Reg_2 = /[\s\,]+/;
console.log("a b  c".split(" "));
console.log("a b,   c".split(Reg_2));

// 分组
var Reg_3 = /^(\d{3})\-(\d{3,8})$/;
console.log(Reg_3.exec("024-325184"));

// 贪婪匹配
var Reg_4 = /^(\d+?)(0*)$/;
console.log(Reg_4.exec("123024003000"));

// 全局搜索
var Reg_5 = /\w+Script/g;  // g 全局匹配
console.log(Reg_5.exec("JavaScript, VBScript, JScript and ECMAScript"));
console.log(Reg_5.exec("JavaScript, VBScript, JScript and ECMAScript"));

console.log(Reg_5.lastIndex);

var Reg_6 = /\w+Script/i;  // i 忽略大小写
console.log(Reg_6.exec("Javascript, VBscript, JScript and ECMAScript"));

var Reg_7 = /\w+Script/m;  // m 多行匹配
console.log(Reg_7.exec("Javascript, VBscript, JScript and ECMAScript"));

// 验证正确格式的邮箱
var reg = /^\w+\.?\w+\@\w+\.\w+$/;
console.log(reg.test('test@gmail.com'));

// 提取邮箱
var regg = /^<(\w+\s?\w+)>\s?(\w+\@\w+\.\w+)$/;
console.log(regg.exec('<Tom Paris> tom@voyager.org'));
var r = regg.exec('<Tom Paris> tom@voyager.org');
if (r === null || r.toString() !== ['<Tom Paris> tom@voyager.org', 'Tom Paris', 'tom@voyager.org'].toString()) {
    console.log('测试失败!');
}
else {
    console.log('测试成功!');
}