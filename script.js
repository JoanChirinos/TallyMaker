//var doc = document.getElementById('inputArea');

//

function checkNumberOfChoices() {
    var num = document.getElementById('numberOfChoices').value;
    if (num == "") {
        return;
    }
    var x = parseInt(num);
    document.getElementById('numberOfChoices').value = Math.abs(Math.floor(x));
}

function enteredChoices() {
    var doc = document.getElementById('inputArea');
    var num = parseInt(document.getElementById('numberOfChoices').value);
    doc.innerHTML = "Loading...";
    if (num < 1) {
        num = 1;
    }
    var toPlaceInInputArea = '<form action="makeTally.py" method="GET" target="_blank">'
    for (var i = 0; i < num; i++) {
        toPlaceInInputArea += '<div class="row"><div class="col"><div class="form-group"><label for="choice' + (i + 1) + '"> Choice ' + (i + 1) + '</label><input type="text" id="choice' + (i + 1) + '" class="form-control" name="choice' + (i + 1) + '"></div></div></div>';
    }
    toPlaceInInputArea += '<div class="row"><div class="col"><input type="submit" class="btn btn-success" name="Next" value="Next"></div></div></form>';
    console.log(toPlaceInInputArea);
    doc.innerHTML = toPlaceInInputArea;
}

function buttonClick(i) {
    console.log(i);
    var num = parseInt(document.getElementById(i).innerHTML);
    document.getElementById(i).value = (num + 1);
}
