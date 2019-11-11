/*
 * @Author: lixuan
 * @Date: 2019-11-11 13:37:00
 * @LastEditTime: 2019-11-11 13:41:12
 * @Description: FindAndFindIndex.js
 */

 var arr = ["Python", "Js", "JAVA", "solidity"];
 var s = arr.find(function(x) {
     /**
      * @description: 返回满足条件的指定元素
      * @param {type} 
      * @return: 
      */
     return x.toLowerCase() === x;
 });
console.log(s);

var y = arr.findIndex(function(x) {
    /**
     * @description: 返回满足条件元素的索引值
     * @param {type} 
     * @return: 
     */
    return x.toUpperCase() === x;
});
console.log(y);
