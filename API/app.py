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
    siteName = userData["site name"]
    userName = userData["username"]
    password = userData["password"]
    result = dao.saveUserData(siteName, userName, password)
    return jsonify(result)


@app.route('/user/data/pass/<id>', methods=['GET'])
def getUserPassword(ID):
    result = dao.getUserPassword(ID)
    return jsonify(result)


@app.route('/user/data/name/<id>', methods=['GET'])
def getUserName(ID):
    result = dao.getUserName(ID)
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
    id = userDetails['ID']
    password = userDetails['password']
    result = dao.updateUserPassword(id, password)
    return jsonify(result)


@app.route('/user/data/del_pass/<id>', methods=['DELETE'])
def deletePassword(ID):
    result = dao.deleteOnePassword(ID)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)
