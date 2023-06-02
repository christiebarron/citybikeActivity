import requests
from flask import Flask, jsonify

url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"

app = Flask(__name__)

#first route
@app.route("/")
def index():
    return render_template("index.html")


# API route
@app.route("/api")
def api():

    #first step is getting data. this can be from nosQL connection, csv, SQL connection, etc. 
        #GOAL IS GET DATA
    response = requests.get(url)

    if response.status_code == 200: #if request is made correctly
        #parse the json data into python dictionary format??
        data = response.json()

    #jsonify the data
        return jsonify(data)
    
    else:
        return jsonify({
            "error" : "failed to get data!"
        })

#if name is main, run app
if __name__ == "__main__":
    app.run()


