'use strict';

// map/filter
var obj = {
    name: 'bob',
    school: 'No.1 middle school',
    address: 'xueyuan road'
};
var upper = _.map(obj, function (key, value) {
    return key + '=' + value;  // 返回Array类型
});

var low = _.mapObject(obj, function (key, value) {
    return key + '=' + value;  // 返回Object类型
});

console.log(JSON.stringify(upper));
console.log(JSON.stringify(low));

// every/some
// 当所有元素都满足条件时，every返回true
// 当有至少一个元素满足条件时，some返回true
var r1 = _.every(obj, function (key, value) {
    return key === key.toLowerCase() && value === value.toLowerCase();
});
var r2 = _.some(obj, function (key, value) {
    return key === key.toLowerCase() || value === value.toLowerCase();
});
console.log('every key-value are lowercase: ' + r1 + '\nsome key-value are lowercase: ' + r2);

// max/min
// 只作用于value，忽略key
var r3 = _.max({
    a: 1,
    b: 3,
    c: -13
});
console.log(r3);

// groupBy
// 按照用户传入的key进行分组
var scores = [23,57,43,76,23,5,3,52,46,245,87,54];
var groups = _.groupBy(scores, function (x) {
    if (x < 60) {
        return 'C';
    } else if (x < 80) {
        return "B";
    } else {
        return "A";
    }
});
console.log(groups);

// shuffle/sample
// shuffle随机打乱集合中的元素
// sample随机选择几个元素，默认一个
var r4 = _.shuffle(obj);
console.log(r4);
var r5 = _.sample(obj, 2);
console.log(r5);