function Request(url, method, form, table) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            if (request.status === 200 || request.status === 201 || request.status === 204) {
                var response = JSON.parse(request.response);
                (table) ? AppendToTable(table, response) : console.log(response);
            } else {}
        }
    };
    request.open(method, url);
    if (form) {
        var data = formDataToJSON(form);
        request.setRequestHeader("Content-Type", "application/json");
        request.send(data);
    }else{
        request.send();
    }
}

function AppendToTable(table, data){
    if (data instanceof Array) {
        data.forEach(function (item) {
            var tr = tableRow(item);
            table.appendChild(tr);
        });
    }else {
        var tr = tableRow(data);
        table.prepend(tr);
    }
}

function tableRow(item){
    var keys = Object.keys(item);
    var tr = document.createElement('tr');
    keys.forEach(function (key) {
        var td = document.createElement('td');
        var txt = document.createTextNode(item[key]);
        td.appendChild(txt);
        tr.appendChild(td);
    });
    return tr;
}

function formDataToJSON(formElement) {
    var formData = new FormData(formElement), convertedJSON = {};
    formData.forEach(function(value, key) {
        convertedJSON[key] = value;
    });
    return JSON.stringify(convertedJSON);
}

document.getElementById('form').addEventListener('submit', function (e) {
    document.getElementById('submit').disabled = true;
});