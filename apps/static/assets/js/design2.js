'use strict'

function setPage(ppa,customized) {
    if (document.getElementById("op_type_0").checked) {
        ppa.style.display = "block";
        customized.style.display = "none";
    }
    if (document.getElementById("op_type_1").checked) {
        ppa.style.display = "none";
        customized.style.display = "block";
    }
}

window.addEventListener('load',()=>{
    var ppa = document.getElementById("ppa");
    var customized = document.getElementById("On-Site Generation");
    var op_type = document.getElementById("op_type");
    setPage(ppa,customized);
    op_type.addEventListener("change", ()=>{
        setPage(ppa,customized);
    });
});