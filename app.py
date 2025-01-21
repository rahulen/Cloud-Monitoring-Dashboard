import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 90 or mem_percent > 90:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')