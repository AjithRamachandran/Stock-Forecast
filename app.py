import json

from flask import Flask, render_template
from markupsafe import Markup
from plotly.offline import plot
from plotly.graph_objs import Scatter
from datetime import date

from utils import get_data
from utils import predict
from utils.common import get_param
from utils.common import create_table
from utils.common import export_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    global today, initial_date
    data = json.load(open('assets/date.json'))
    today = date.today()
    today = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    initial_date = data.get('date')
    if(initial_date != today):
        initial_date = today
        get_data.create_data()
        export_data(initial_date)
    return render_template('index.html')


@app.route('/ms')
def predict_ms():
    csv = 'assets/Microsoft.csv'
    prediction = predict.predict_ms()
    X, Y = get_param(csv)
    table = create_table(csv)
    my_plot_div = plot([Scatter(x=X, y=Y)], output_type='div')
    return render_template('prediction.html', title='Microsoft', prediction=prediction, graph=Markup(my_plot_div), table=table)


@app.route('/intel')
def predict_intel():
    csv = 'assets/Intel.csv'
    prediction = predict.predict_intel()
    X, Y = get_param(csv)
    table = create_table(csv)
    my_plot_div = plot([Scatter(x=X, y=Y)], output_type='div')
    return render_template('prediction.html', title='Intel', prediction=prediction, graph=Markup(my_plot_div), table=table)


@app.route('/apple')
def predict_apple():
    csv = 'assets/Apple.csv'
    prediction = predict.predict_apple()
    X, Y = get_param(csv)
    table = create_table(csv)
    my_plot_div = plot([Scatter(x=X, y=Y)], output_type='div')
    return render_template('prediction.html', title='Apple', prediction=prediction, graph=Markup(my_plot_div), table=table)


if __name__ == '__main__':
    app.run()
