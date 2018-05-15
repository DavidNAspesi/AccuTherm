
from flask import Flask, request, render_template
import random
app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

@app.route("/")
def lab_temp():
    import sys
    temperature = random.uniform(71, 73)
    if temperature is not None:
        return render_template("lab_temp1.html",temp=temperature)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
