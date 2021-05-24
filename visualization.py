from flask import Flask, render_template, get_flashed_messages, request, jsonify

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def index():
    return jsonify()

@app.route('/' , methods=['GET'])
def index1():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)
