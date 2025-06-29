
from flask import Flask, render_template, request
from tracker_logic import predict_period, save_to_csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        name = request.form['name']
        last_period = request.form['last_period']
        cycle_length = int(request.form['cycle_length'])
        period_length = int(request.form['period_length'])

        result = predict_period(last_period, cycle_length, period_length)

        if isinstance(result, dict):  # Only save if valid
            save_to_csv(name, last_period, cycle_length, period_length, result)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
