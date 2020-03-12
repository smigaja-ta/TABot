from flask import request
from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>The temperature is 91.2 F</h1>"

@app.route("/errorhelp/", methods=["GET", "POST"])
def errorhelp():
    print(request.form['text'])
    time.sleep(1.3)    
    url = "https://lmgtfy.com/?q=" + "Python%20" + request.form['text']
    response = {
        "blocks": [
                  {"type": "section",
                   "text": {
                           "type": "mrkdwn",
                           "text": f"Hello {request.form['user_name']}! As always, I am glad to help! :smile:"
                           }
                  }, 
                  {"type":"section",
                   "text":{
                          "type": "mrkdwn",
                          "text": f"<{url}|Here is a link to the information you need to fix this problem!>"
                          }
                  }
                  ]
         ,
         "response_type": "in_channel" 
} 
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
