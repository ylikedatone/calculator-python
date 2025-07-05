import sys
sys.stdout.reconfigure(line_buffering=True)
from flask import Flask, request, render_template, jsonify
import psycopg2

#i am using psycopg2-binary which doesn't include the pool module
#so have to create this def as a workaround
def get_db_connection():
    return psycopg2.connect(
        dbname="app_database",
        user="calculator",
        password="calculator",
        #docker resolves container names as hostnames -> flask will find postgres container
        host="calculator_db",
        port="5432"
    )



app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello", flush=True)
    return render_template("index.html")

###need to pass numbers as query parameters in URL

@app.route('/calculate')
def addition():
    print("Route /calculate was hit!")
    #extract the numbers from the URL
    num_1_str = request.args.get('num_1', default=None)
    num_2_str = request.args.get('num_2', default=None)
    #this is manually validating num_1_str to make sure it's a number
    try:
        num_1 = float(num_1_str) if num_1_str else None
        num_2 = float(num_2_str) if num_2_str else None
        operation = "addition"
        result = num_1+num_2
        if result is not None:
            conn = get_db_connection()
            cur = conn.cursor()
            #extract the data from json and parse into postgres table
            cur.execute("INSERT INTO calculations (num_1, operation, num_2, result) VALUES (%s, %s, %s, %s)", (num_1, operation, num_2, result))
            conn.commit() #save changes
            cur.close() #close cursor
            conn.close() #close the connection

        results_json = jsonify({"num_1": num_1, "operation": "addition", "num_2": num_2, "result": result})
        return results_json
        
    except ValueError:
        return jsonify({"error": "Invalid input! Please enter numbers only."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
