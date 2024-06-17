from flask import Flask, render_template, request
import pandas as pd
from model import model

# Createing Flask application instance
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    # Render the home page when root URL is accessed
    return render_template('home.html')

@app.route('/start')
def start():
    # Render the index page when the /start URL is accessed
    return render_template('index.html')

def result_statement(date, time, traffic_volume):
    # Define thresholds for traffic volume categories
    very_low_threshold = 666
    low_threshold = 667
    moderate_threshold = 668
    high_threshold = 669

    # Classify traffic volume based on defined thresholds
    if traffic_volume < very_low_threshold:
        traffic_condition = "VERY LOW"
    elif traffic_volume < low_threshold:
        traffic_condition = "LOW"
    elif traffic_volume < moderate_threshold:
        traffic_condition = "MODERATE"
    elif traffic_volume < high_threshold:
        traffic_condition = "HIGH"
    else:
        traffic_condition = "VERY HIGH"

    # Createing result statement
    statement = (
        f"On {date}\n"
        f"At {time}\n"
        f"The Traffic Condition Was {traffic_condition}\n"
        f"With {int(traffic_volume)} Vehicles."
    )
    return statement

# Dictionary to store form data
d = {}

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Get form data and convert it to appropriate format
    d['is_holiday'] = request.form['isholiday']
    if d['is_holiday'] == 'yes':
        d['is_holiday'] = int(1)
    else:
        d['is_holiday'] = int(0)
    d['temperature'] = int(request.form['temperature'])
    d['weekday'] = int(0)
    D = request.form['date']
    d['hour'] = int(request.form['time'][:2])
    d['month_day'] = int(D[8:])
    d['year'] = int(D[:4])
    d['month'] = int(D[5:7])
    d['x0'] = request.form.get('x0')
    d['x1'] = request.form.get('x1')
   
    # Define possible values for x0 and x1
    xoval = {'x0_Clear', 'x0_Clouds', 'x0_Drizzle', 'x0_Fog', 'x0_Haze',
             'x0_Mist', 'x0_Rain', 'x0_Smoke', 'x0_Snow', 'x0_Thunderstorm'}
    x1val = {'x1_Sky is Clear',
             'x1_broken clouds',
             'x1_drizzle',
             'x1_few clouds',
             'x1_fog',
             'x1_haze',
             'x1_heavy intensity drizzle',
             'x1_heavy intensity rain',
             'x1_heavy snow',
             'x1_light intensity drizzle',
             'x1_light intensity shower rain',
             'x1_light rain',
             'x1_light rain and snow',
             'x1_light shower snow',
             'x1_light snow',
             'x1_mist',
             'x1_moderate rain',
             'x1_overcast clouds',
             'x1_proximity shower rain',
             'x1_proximity thunderstorm',
             'x1_proximity thunderstorm with drizzle',
             'x1_proximity thunderstorm with rain',
             'x1_scattered clouds',
             'x1_shower drizzle',
             'x1_sky is clear',
             'x1_sleet',
             'x1_smoke',
             'x1_snow',
             'x1_thunderstorm',
             'x1_thunderstorm with heavy rain',
             'x1_thunderstorm with light drizzle',
             'x1_thunderstorm with light rain',
             'x1_thunderstorm with rain',
             'x1_very heavy rain'
             }
    
    # Initialize dictionaries for x0 and x1 with zero values
    x0 = {}
    x1 = {}
    for i in xoval:
        x0[i] = 0
    for i in x1val:
        x1[i] = 0
    x0[d['x0']] = 1
    x1[d['x1']] = 1
    
    # Create the input feature list for model
    final = []
    final.append(d['is_holiday'])
    final.append(d['temperature'])
    final.append(d['weekday'])
    final.append(d['hour'])
    final.append(d['month_day'])
    final.append(d['year'])
    final.append(d['month'])

    # Get the date and time from the form
    date = request.form['date']
    time = request.form['time']

    # Predict the traffic volume using model
    output = model.predict([final])
     
    # Render the output page with prediction result
    return render_template('output.html', statement=result_statement(date, time, output))

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
