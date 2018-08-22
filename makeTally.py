#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    choices = []
    
    for i in fs.keys():
        choices += [fs.getvalue(i)]
    
    top = """<!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link rel="stylesheet" href="style.css" type="text/css">

        <title>Your Tally Counter</title>
    </head>

    <body>
        <div class="space-sm"></div>
        <div class="container">
    """
    
    bottom = """
        </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        <script src="script.js"></script>
    </body>
    </html>"""
    
    toAdd = ''
    btntypes = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'lighht', 'dark']
    on = -1
    for i in choices:
        if (i == "Next") {
            continue;
        }
        on += 1
        on %= 8
        btn = btntypes[on]
        toAdd += '<div class="row"><div class="col"><button type="button" class="btn btn-' + btn + '" onclick="buttonClick("' + i + '")>' + i + '</button>&nbsp;&nbsp;&nbsp;&nbsp;<label id="' + i + '">0</label><div class="space-sm"></div>\n\n\n'
    print top
    print toAdd
    print bottom

go()
    
    
    
    
    
    
    
    
    
    
    
    
    
    