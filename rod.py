from flask import Flask, jsonify
import requests
import csv
from io import StringIO

# You can use Requests to talk to external packages 

app = Flask(__name__)

url = "https://github.com/CSSEGISandData/COVID-19/blob/e59694b8ef62e55aeb2d9f376cc3933bf013d3f8/csse_covid_19_data/csse_covid_19_daily_reports/10-06-2020.csv"
countries = ["Ghana", "Togo", "Nigeria", "Benin"]
covid_cases = []

@app.route("/api/")
def cases():
    resp = requests.get(url)

    data = resp.content.decode("ascii", "ignore")

    csv_data = StringIO(data)

    reader = csv.reader(csv_data)

    for row in reader:
        if row[0] =="FIPS":
            continue
        if row[3] in countries:
            covid_cases.append(
                {
                    "Country": row[3],
                    "Confirmed Cases": row[7],
                    "Death": row[8],
                    "Recoveries": row[9],
                    "Active Cases": row[10],
                }
            )
   
    

    return jsonify({"Covid 19 Cases": covid_cases})               
            
        
# @app.route("/greet/<name>")
# def greet(name):
#     return "Hi " + name

# @app.route("/hi")
# def hi():
#     return "Hello World"

# Always run your code in the terminal before going to the web

if __name__ == "__main__":
     app.run(port=8000, debug=True)
