/*
 * @Author: lixuan
 * @Date: 2019-11-18 08:32:09
 * @LastEditTime: 2019-11-18 08:45:57
 * @Description: 
*/
function checkRegisterForm() {
    var name = document.getElementById("username");
    var pwd_1 = document.getElementById("password");
    var pwd_2 = document.getElementById("password-2");
    var re_name = /^\w{3,10}$/;
    var re_pwd = /^\w{6,20}$/;
    if (!re_name.test(name.value)) {
        alert("用户名必须是3-10位英文字母或数字");
        return false;
    } else if (!re_pwd.test(pwd_1.value)) {
        alert("口令必须是6-20位");
        return false;
    } else if (pwd_1 != pwd_2) {
        alert("两次输入口令必须一致");
        return false;
    } else {
        return true;
    }
}
