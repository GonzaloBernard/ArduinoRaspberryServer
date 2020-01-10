from flask import Flask, json, render_template
import arduinoJson
app = Flask(__name__)

#ph = arduinoJson.phRead()
#temp = arduinoJson.tempRead()
#date = arduinoJson.dateRead()
@app.route('/home')
def render():
    #return 'hola'
    #return arduinoJson.phRead()
    return render_template( 'home.html', ph=arduinoJson.phRead(), temp = arduinoJson.tempRead(), date = arduinoJson.dateRead())

@app.route('/index')
def renderr():
    return 'Hola'

if __name__ == '__main__':
    app.run()#host='0.0.0.0', debug=True, port=5000)