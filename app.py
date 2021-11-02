from flask import Flask, jsonify, request
import json
import os
app = Flask(__name__)

USERNAME = "<INSERT YOUR NAME HERE>"

@app.route('/', methods=['GET'])
def home():
    #Return simple string for home page
    return 'R&I 6'

@app.route('/posts', methods=['GET'], defaults={'postid': None})
@app.route('/posts/<postid>', methods=['GET'])
def query_posts(postid):
    filename = os.path.join(app.static_folder, 'posts.json')
    with open(filename) as f:
        records = json.load(f)
    if postid:
        "Insert your code here"
    else:
        "Insert your code here"

## ADD COMMENTS AND USERS METHODS HERE

if __name__ == '__main__':
    #Run app on port 5000 in debug mode. Host is specified as Flask needs you to give a host for apps that would
    #need to be externally visible - in this case, from outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)