
from flask import Flask, request, render_template
import grove_hightemperature_sensor as grovepi
import sys
app = Flask(__name__)
app.debug = False

@app.route("/")
def lab_temp():
    probe_temperature_pin = 14

    sensor = grovepi.HighTemperatureSensor(probe_temperature_pin)
    
    while True:

        temperature = sensor.getProbeTemperature()
        if temperature is not None:
            return render_template("lab_temp1.html",temp=temperature)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
