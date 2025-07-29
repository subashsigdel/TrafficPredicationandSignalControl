# app.py
from flask import Flask, render_template,request, redirect, url_for,jsonify
import csv
import gdown
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
       
        if authenticate_user(email, password):
           
            return redirect(url_for('liveanalysis'))
        else:
           
            return redirect(url_for('index')) 
    
    return render_template('index.html')

def authenticate_user(email, password):
    correct_email = 'test@example.com'
    correct_password = 'password123'
    
    return email == correct_email and password == correct_password

@app.route('/liveanalysis')
def liveanalysis():
    
    csv_file = 'predictdata.csv'  
    data = []

   
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return render_template('Analysis.html',data=data)

@app.route('/livetraffic')
def livetraffic():


    
    file_id = '1gLoHkAkiMvsXbKZciV_6ynquo_lAydjk'

    # Use gdown to download the file
    gdown.download(f"https://drive.google.com/uc?id={file_id}", 'predictdata.csv', quiet=False)

    # # Read the CSV file into pandas DataFrame
    # new_data_df = pd.read_csv('data.csv')


    csv_file = 'predictdata.csv' 
    last_row = None

    # Read the CSV file and fetch the last row
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            last_row = row  
           
        traffic_prediction = last_row[2].strip().lower()

        # Set different intervals for green light based on the traffic prediction
        if traffic_prediction == "high":
            green_duration = 5000  # Green light for 5 seconds when high
        else:
            green_duration = 3000  # Default green light for 3 seconds

         # Pass the last row to the HTML template
    return render_template('livetraffic.html', last_row=last_row,green_duration=green_duration)

def display_chart():
    csv_file = 'predicted_traffic.csv'  
    times = []
    days = []
    traffic_situations = []

    
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            times.append(row[0])  
            days.append(row[1])  
            traffic_situations.append(row[2]) 

    
    return render_template('Analysis.html', times=times, days=days, traffic_situations=traffic_situations)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
