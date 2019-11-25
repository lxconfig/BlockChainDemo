/*
 * @Author: lixuan
 * @Date: 2019-11-25 14:47:50
 * @LastEditTime: 2019-11-25 15:35:32
 * @Description: 
 */
'use strict';

var json = {
    name: $("input[name=name]")[0].value,
    email: $("input[name=email]")[0].value,
    password: $("input[name=password]")[0].value,
    gender: $("input[name=gender]:checked")[0].value,
    city: $("select[name=city]>option:selected")[0].value,
}

if (typeof (json) === 'string') {
    console.log(json);
} else {
    console.log('json变量不是string!');
}

var obj = {};
// 限定状态:input 可获取：<input>，<textarea>，<select>和<button> 元素
var name = $('#test-form :input,#test-form :radio');
name.filter(function () {
    return this.type !== 'submit'
}).map(function () {
    if (this.type !== 'radio' || this.checked) {
        obj[this.name] = this.value;
    }
});
json = JSON.stringify(obj, null, " ");