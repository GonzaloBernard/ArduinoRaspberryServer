from flask import Flask, render_template, request, redirect, url_for
import arduinoJson
import pytz
import datetime
app = Flask(__name__)

@app.route('/update')
def update():
    ph = request.args.get('ph', default = -1, type = float)
    temp = request.args.get('temp', default = -1, type = float)
    hum = request.args.get('hum' , default = -1, type = float)

    # Obtencion de la hora en Argentina
    tz = pytz.timezone('America/Argentina/Buenos_Aires')
    ct = datetime.datetime.now(tz=tz)
    fecha = ct.strftime("%H:%M %d/%m/%Y")

    arduinoJson.overwriteLastOne( {"arduino": [{"date": fecha, "ph": ph, "temp": temp, "hum": hum}]} )

#    arduinoJson.addHistorial( {"date": fecha, "ph": ph, "temp": temp, "hum": hum} )
    return redirect (url_for('renderLastRead'))

#    return arduinoJson.addHistorial( {"date": fecha, "ph": ph, "temp": temp, "hum": hum} )

@app.route('/')
def renderLastRead():
    return render_template( 'home.html', ph= arduinoJson.phRead(), temp = arduinoJson.tempRead(), date = arduinoJson.dateRead(), hum = arduinoJson.humRead())

@app.route('/historial')
def renderHistorial():
    return arduinoJson.getHistorialHTML()

if __name__ == '__main__':
    app.run()