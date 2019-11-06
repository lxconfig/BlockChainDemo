'use strict';
function area_of_circle(r, pi){
    if (arguments.length === 1) {
        return (r * r * 3.14);
    } else {
        return (r * r * pi);
    }
}

console.log(area_of_circle(2, 3.1415));


function max(a, b) {
    if (a < b) {
        return b;
    } else {
        return a;
    }
}