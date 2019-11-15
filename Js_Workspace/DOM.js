/*
 * @Author: lixuan
 * @Date: 2019-11-15 14:45:32
 * @LastEditTime: 2019-11-15 16:07:11
 * @Description: 操作DOM
*/

var p = document.getElementById('p-id');
// p.innerHTML = "ABC";  // 可以修改这个节点里面的文本内容
// p.innerHTML = "abc <span style='color: red'>RED</span>";  // 修改节点的内部结构，新增加一个<span>

// 会对字符串进行HTML编码，保证无法设置HTML标签，不返回隐藏元素
// p.innerText = "a<span style='color:red'>RED</span>";

// 会对字符串进行HTML编码，保证无法设置HTML标签，返回有所有文本
// p.textContent = "s<span style='color:red'>RED</span>";

// 修改设置CSS
p.style.color = "#ff0000";
p.style.fontSize = '20px';
p.style.paddingTop = '2em';

var d = document.getElementById('container');
var js = document.getElementById("js");
d.appendChild(js);  // 将已经存在的节点扩展到某个节点下（先从原位置删除，再插入到新位置）

// 重新创建一个节点插入到新的位置
var n = document.createElement("h1");
n.id = "n";
n.innerText = "test h1";
d.appendChild(n);


// 插入到指定位置（找到后一个元素位置）
var nn = document.createElement("input");
nn.id = "input_nn";
nn.innerText = "输入框";
d.insertBefore(nn, js);

// 按字符串顺序重新排列DOM节点

// <!-- HTML结构 -->
// <ol id="test-list">
//     <li class="lang">Scheme</li>
//     <li class="lang">JavaScript</li>
//     <li class="lang">Python</li>
//     <li class="lang">Ruby</li>
//     <li class="lang">Haskell</li>
// </ol>
// var ol = document.getElementById("test-list");
// var arrs = [];
// for (var i=0; i<ol.children.length; i++){
//     arrs.push(ol.children[i].innerText);
// }
// arrs.sort();
// for (var j=0; j<arrs.length; j++){
//     ol.children[j].innerText = arrs[j];
// }


// 删除DOM节点(用父节点删)
var inp = document.getElementById("input_nn");
d.removeChild(inp);