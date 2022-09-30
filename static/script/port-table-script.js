
// --------- table-sort-search-json -----------

var table_full = document.getElementById('port-table');
var table_body = document.getElementById('port-table-body');
var search_input = document.getElementById('port-search');
let tableColumns = document.getElementsByClassName('table-column');
var def_tableData = tableToJson(table_full);
var tableData = def_tableData;

var carretDefaultClassName = 'fa-solid fa-arrows-up-down';
var caretUpClassName = 'fa-solid fa-arrow-up-wide-short';
var caretDownClassName = 'fa-solid fa-arrow-down-short-wide';

function tableToJson(table) {
  var data = [];

  // first row needs to be headers
  var headers = [];
  for (var i = 0; i < table.rows[0].cells.length; i++) {
    headers[i] = table.rows[0].cells[i].innerText.replace(/ /gi, '').toLowerCase();
  }

  // go through cells
  for (var i = 1; i < table.rows.length; i++) {

    var tableRow = table.rows[i];
    var rowData = {};

    for (var j = 0; j < tableRow.cells.length; j++) {

      rowData[headers[j]] = tableRow.cells[j].innerHTML;

    }

    data.push(rowData);
  }

  return data;
}

const sort_by = (field, reverse, primer) => {

  const key = primer ?
    function (x) {
      return primer(x[field]);
    } :
    function (x) {
      return x[field];
    };

  reverse = !reverse ? 1 : -1;

  return function (a, b) {
    return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
  };
};


function clearArrow() {
  let carets = document.getElementsByClassName('caret');
  for (let caret of carets) {
    caret.className = `caret ${carretDefaultClassName} `; //  
  }
}

function toggleArrow(event) {
  let element = event.target;
  let caret, field, reverse;
  if (element.tagName === 'SPAN') {
    caret = element.getElementsByClassName('caret')[0];
    field = element.innerText.replace(/ /gi, '').toLowerCase()
  }
  else {
    caret = element;
    field = element.parentElement.innerText.replace(/ /gi, '').toLowerCase()
  }


  let iconClassName = caret.className;
  clearArrow();
  if (iconClassName.includes(caretUpClassName)) {
    caret.className = `caret ${caretDownClassName}`;
    reverse = false;
  } else {
    reverse = true;
    caret.className = `caret ${caretUpClassName}`;
  }
  tableData.sort(sort_by(field, reverse));

  populateTable();
}


function populateTable() {
  table_body.innerHTML = '';

  for (let data of tableData) {
    let row = table_body.insertRow(-1);
    
    let pid = row.insertCell(0);
    pid.outerHTML = "<th>" + data.pid + "</th>";

    let name = row.insertCell(1);
    name.innerHTML = data.portname;

    let temperature = row.insertCell(2);
    temperature.innerHTML = data.temperature;

    let latitude = row.insertCell(3);
    latitude.innerHTML = data.latitude;

    let longitude = row.insertCell(4);
    longitude.innerHTML = data.longitude;

    let date = row.insertCell(5);
    date.innerHTML = data.date;
  


    // let action = row.insertCell(5);
    // action.innerHTML = data.action;
  }

  filterTable();
}


function filterTable() {
  let filter = search_input.value.toUpperCase();
  rows = table_body.getElementsByTagName("tr");
  let flag = false;

  for (let row of rows) {
    let cells = row.getElementsByTagName("td");
    for (let cell of cells) {
      if (cell.textContent.toUpperCase().indexOf(filter) > -1) {
        if (filter) {
          cell.style.backgroundColor = 'yellow';
        } else {
          cell.style.backgroundColor = '';
        }

        flag = true;
      } else {
        cell.style.backgroundColor = '';
      }
    }

    if (flag) {
      row.style.display = "";
    } else {
      row.style.display = "none";
    }

    flag = false;
  }
}

for (let column of tableColumns) {
  column.addEventListener('click', function (event) {
    toggleArrow(event);
  });
}

search_input.addEventListener('keyup', function (event) {
  filterTable();
});


$(document).ready(function(){
	setTimeout(function(){ clearArrow(); });
});

$(document).ready(function () {
  $('#port-table tfoot th').each(function () {
      var title = $(this).text();
      $(this).html('<input type="text" placeholder="Search ' + title + '" />');
  });

});