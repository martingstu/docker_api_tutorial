from flask import Flask, jsonify, request, abort
import json
import os
app = Flask(__name__)

USERNAME = "Martin"

@app.route('/', methods=['GET'])
def home():
    #Return simple string for home page
    return 'R&I 6'

@app.route('/posts', methods=['GET'], defaults={'postid': None})
@app.route('/posts/<int:postid>', methods=['GET'])
def query_posts(postid):
    filename = os.path.join(app.static_folder, 'posts.json')
    with open(filename) as f:
        records = json.load(f)
    if postid:
        for post in records:
            if post['id'] == postid:
                return jsonify(post)
        abort(404)
    else:
        return jsonify(records)


## ADD COMMENTS AND USERS METHODS HERE
@app.route('/comments', methods=['GET'], defaults={'postid': None})
@app.route('/posts/<int:postid>/comments', methods=['GET'])
@app.route('/comments/<int:commentid>', methods=['GET'])
@app.route('/posts/<int:postid>/comments/<int:commentid>', methods=['GET'])
# @app.route('/posts/<postid>/comments/<commentid>', methods=['GET'])
def query_comments(postid, commentid):
    filename = os.path.join(app.static_folder, 'comments.json')
    with open(filename) as f:
        records = json.load(f)
    if postid:
        if commentid:
            for comment in records:
                if comment['postId'] == postid and comment['id'] == commentid:
        else:
            resp = []
            for comment in records:
                if comment['postId'] == postid:
                    resp.append(comment)
            return jsonify(resp)
    else:
        return jsonify(records)


@app.route('/users', methods=['GET'], defaults={'userid': None})
@app.route('/users/<int:userid>', methods=['GET'])
def query_users(userid):
    filename = os.path.join(app.static_folder, 'users.json')
    with open(filename) as f:
        records = json.load(f)
    if userid:
        for user in records:
            if user['id'] == userid:
                return jsonify(user)
        abort(404)
    else:
        return jsonify(records)

if __name__ == '__main__':
    #Run app on port 5000 in debug mode. Host is specified as Flask needs you to give a host for apps that would
    #need to be externally visible - in this case, from outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)