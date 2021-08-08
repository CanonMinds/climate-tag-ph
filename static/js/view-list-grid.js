/*********************************
        List-Grid Views
*********************************/
var elements = document.querySelectorAll(".lg-info");
var items = document.querySelectorAll(".lg-item");

$(".lg-label").hide();

function gridView() {
    $("#list.btn-toggle").removeClass("active");
    $("#grid.btn-toggle").addClass("active");
    $(".lg-container").removeClass("list").addClass("grid");

    // $(".lg-label").show();

    $("#listHeader").hide();
    $(".lg-info.lg-listonly").hide();

    // sorting columns into rows
    $(".lg-item").removeClass("list").addClass("grid");
}

function listView() {
    $("#list.btn-toggle").addClass("active");
    $("#grid.btn-toggle").removeClass("active");
    $(".lg-container").removeClass("grid").addClass("list");

    // $(".lg-label").hide();

    $("#listHeader").show();
    $(".lg-info.lg-listonly").show();

    // resetting columns
    $(".lg-item").removeClass("grid").addClass("list");
}

// Filtering

// Parsing filter variables in URL
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value.replace(/\+/g," ").replace(/%28/g,"(").replace(/%29/g,")");
    });
    return vars;
}

// Get filter variables in URL
function getUrlParam(parameter, defaultvalue){
    var urlparameter = defaultvalue;
    if(window.location.href.indexOf(parameter) > -1){
        urlparameter = getUrlVars()[parameter];
        }
    return urlparameter;
}

