'use strict'

function setPage(op_type, ppa, customized) {
    var display = op_type.options[op_type.selectedIndex].text;
    if (display=="PPA") {
        ppa.style.display = "block";
        customized.style.display = "none";
    }
    else {
        ppa.style.display = "none";
        customized.style.display = "block";
    }
}

window.addEventListener('load',()=>{
    var ppa = document.getElementById("ppa");
    var customized = document.getElementById("customized");
    var op_type = document.getElementById("op_type");
    setPage(op_type, ppa, customized);
    op_type.addEventListener("change",()=>{
        setPage(op_type, ppa, customized);
    });
});