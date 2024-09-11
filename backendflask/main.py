# app.py
from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Process login (e.g., authenticate user, check password, etc.)
        if authenticate_user(email, password):
            # Redirect to the livetraffic page upon successful login
            return redirect(url_for('liveanalysis'))
        else:
            # Redirect back to index or handle failure
            return redirect(url_for('index'))  # Customize if needed
    
    return render_template('index.html')

def authenticate_user(email, password):
    # Hardcoded credentials for testing purposes
    correct_email = 'test@example.com'
    correct_password = 'password123'
    
    return email == correct_email and password == correct_password

@app.route('/liveanalysis')
def liveanalysis():
    return render_template('Analysis.html')

@app.route('/livetraffic')
def livetraffic():
    return render_template('livetraffic.html')



if __name__ == '__main__':
    app.run(debug=True)
