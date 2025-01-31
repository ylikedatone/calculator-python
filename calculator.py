from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

###need to pass numbers as query parameters in URL

@app.route('/calculate')
def addition():
    #extract the numbers from the URL
    num_1_str = request.args.get('num_1', default=None)
    num_2_str = request.args.get('num_2', default=None)
    try:
        num_1 = float(num_1_str) if num_1_str is not None else 0
        num_2 = float(num_2_str) if num_2_str is not None else 0
        result = num_1+num_2
        return jsonify({"num_1": num_1, "num_2": num_2, "result": result})
    except ValueError:
        return jsonify({"error": "Invalid input! Please enter numbers only."})
    

if __name__ == '__main__':
    app.run(debug=True)
