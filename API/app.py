from flask import Flask, jsonify, request

from .DAODatabase import DAO

app = Flask(__name__)
dao = DAO()


@app.route('/user/data', methods=['GET'])
def getUserData():
    userData = dao.getUserData()
    return jsonify(userData)


@app.route('/user/add', methods=['POST'])
def insertUserData():
    userData = request.get_json()
    siteName = userData["sitename"]
    userName = userData["username"]
    password = userData["password"]
    result = dao.saveUserData(siteName, userName, password)
    return jsonify(result)


@app.route('/user/data/pass/', methods=['GET'])
def getUserPassword():
    id = request.args["id"]
    result = dao.getUserPassword(id)
    return jsonify(result)


@app.route('/user/data/name/', methods=['GET'])
def getUserName():
    id = request.args["id"]
    result = dao.getUserName(id)
    return jsonify(result)


@app.route('/user/data/name/', methods=['PUT'])
def updateUsername():
    userDetails = request.get_json()
    id = userDetails['ID']
    username = userDetails['username']
    result = dao.updateUsername(id, username)
    return jsonify(result)


@app.route('/user/data/pass/', methods=['PUT'])
def updateUserPassword():
    userDetails = request.get_json()
    id = userDetails['id']
    password = userDetails['password']
    result = dao.updateUserPassword(id, password)
    return jsonify(result)


@app.route('/user/data/delpass/<id>', methods=['DELETE'])
def deletePassword(id):
    result = dao.deleteOnePassword(id)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)
