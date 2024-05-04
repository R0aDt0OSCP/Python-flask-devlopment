from flask import Flask,render_template,request, redirect, url_for,jsonify

career=[{'id':'1',
       'name':'Data Analyst',
       'salary':'12000',
        'location':'Bangalore'
      },
     {'id':'2',
        'name':'Software Engineer',
        'salary':'15000',
         'location':'Bangalore'
       }]


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/jobs")

def jobs():
    return render_template("jobs.html",job=career)

@app.route("/api/jobs")

def json_list():
    return jsonify(career)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port='5000', debug=True)