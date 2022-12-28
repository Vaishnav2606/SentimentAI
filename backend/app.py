from flask import Flask, request, jsonify,redirect, url_for
import sys
import model.index as p



app = Flask(__name__)

@app.route('/ping', methods = ['GET','POST'])
def ping():
    if request.method == 'GET':
        return jsonify({"success": True, "message": "this is the create endpoint"}), 201
    
@app.route('/predict', methods = ['POST','GET'])    
def predict():    
    print(type(request.json))

    text = request.json
    text = text['data']

    prediction = p.predRun(text)

    return jsonify({'data':prediction}), 201

if __name__ == '__main__':
    app.run()
