/*
 * @Author: lixuan
 * @Date: 2019-11-21 15:07:12
 * @LastEditTime: 2019-11-21 15:23:56
 * @Description: 判断上传的文件类型
 */
'use strict';
function CheckUploadForm() {
    var form = document.getElementById("test-file-upload");
    var file_name = form.value;
    if (!file_name || !file_name.endsWith(".jpg") || !file_name.endsWith(".gif")) {
        alert("Can't read upload file");
        return false;
    }
    var p1 = document.getElementById("p1");
    var n = document.createElement("p");
    n.id = "pp";
    n.innerText = file_name;
    p1.appendChild(n);
}
