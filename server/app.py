from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
 
@app.route("/entity", methods=['POST', 'GET'])
def hello():
    data = request.get_json(force=True)
    print(data)
    text = data['text']
    response = {"message":"Hello!", "text":text}
    return jsonify(response)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
