import json

def overwriteLastOne( data ):
    #get reads from arduino
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'w') as outfile:
        json.dump(data, outfile)

def readAll():
    result = {}
    with open('historial.json', 'r') as json_file:
        data = json.load(json_file)
        for row in data['arduino']:
            result[ row['id'] ] = ('ph: ' + row['ph'] + ' Temp: ' + row['temp'] + ' Fecha: '+ row['date'] )
    return result

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

def read():
    with open('/home/GonzaloBernard/mysite/lastRead.json', 'r') as json_file:
        data = json.load(json_file)
        for row in data['arduino']:
            return(row['ph'])