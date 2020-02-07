import json

def overwriteLastOne( data ):
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'w') as outfile:
        json.dump(data, outfile)
    return True

def addHistorial( data ):
    with open('/home/GonzaloBernard/mysite/historial.json', 'r') as json_file:
        historialDict = json.load(json_file)

    lista = list(historialDict.items())
#    lista.append(data)

    with open('/home/GonzaloBernard/mysite/historial.json', 'w') as outfile:
        json.dump(lista, outfile)
    return str(lista)

def phRead():
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'r') as json_file:
        data = json.load(json_file)
        for row in data['arduino']:
            return(row['ph'])

def tempRead():
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'r') as json_file:
        data = json.load(json_file)
        for row in data['arduino']:
            return(row['temp'])

def dateRead():
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'r') as json_file:
        data = json.load(json_file)
        for row in data['arduino']:
            return(row['date'])

def humRead():
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'r') as json_file:
        data = json.load(json_file)
        for row in data['arduino']:
            return(row['hum'])

def getHistorialHTML():
    result  = '<!DOCTYPE html>  <html lang="en">    <head>  <title>Historial de mediciones  </title>  </head>'
    result += '<body>   <table style="margin-left:auto;margin-right:auto;font-size:30px">'
    result += '<!-- Table headers --><th><tr style="color: green; ">'
    result += '<td align=center>pH</td> <td align=center>Temperatura</td> <td align=center>Humedad</td> <td align=center>Fecha</td>'
    result += '</tr></th>'
    with open('/home/GonzaloBernard/mysite/historial.json', 'r') as json_file:
        data = json.load(json_file)
    i = 1
    for row in data['arduino']:
        result += ('<tr> <td align=center>'+ row['ph'] +'</td> <td align=center>' + row['temp'] + '</td> <td align=center>' + row['hum'] + '</td> <td align=center>' + row['date'] + '</td></tr>')
        i+=1
        if  i > 24:
            result += '</table></body></html>'
            return result
    result += '</table></body></html>'
    return result