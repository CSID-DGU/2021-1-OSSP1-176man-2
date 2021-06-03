from flask import Flask, render_template, get_flashed_messages, request, jsonify
from naverPapago import translate

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def index():
    return jsonify()

@app.route('/' , methods=['GET', 'POST'])
def index1():
    if request.method == "GET":
        return render_template('show3.html')
    elif request.method == "POST":
        data = request.form
        trans = translate_en2ko(data["body"])
        return render_template("show3.html", name=trans, origin=data["body"])

if __name__ == '__main__':
    app.run(debug=True)
