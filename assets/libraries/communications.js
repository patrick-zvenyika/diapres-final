//This script will handle all HTTP REQUESTS
// Created By Ryan Ben (Closed Source Script)

let serverURL = window.location.origin;

function POST_REQUEST(url,data,callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }
    xmlhttp.open("POST", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}


function UPDATE_REQUEST(url, data, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }

    xmlhttp.open("UPDATE", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}


function PUT_REQUEST(url, data, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }

    xmlhttp.open("PUT", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}


function GET_REQUEST(url, data, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }

    xmlhttp.open("GET", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}

function PATCH_REQUEST(url, data, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }

    xmlhttp.open("PATCH", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}

function DELETE_REQUEST(url, data, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }

    xmlhttp.open("DELETE", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}

function GET_REQUEST(url, data, callback) {
    data = null
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xmlhttp.response);
        }
    }

    xmlhttp.open("GET", serverURL + url)
    xmlhttp.setRequestHeader('Content-Type', 'application/json');
    xmlhttp.send(JSON.stringify(data));

}