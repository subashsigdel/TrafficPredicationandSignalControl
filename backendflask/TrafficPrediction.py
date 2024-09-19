import joblib
import pandas as pd
from datetime import datetime

# Load the saved model
RForest_clf = joblib.load('/content/drive/MyDrive/TrafficPrediction/Trafficprediction_model.pkl')

url = 'https://drive.google.com/file/d/1yREHIcwc7eMEaHmx-5RF9bYDRIQxoXmt/view?usp=drive_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

new_data_df = pd.read_csv(path)
new_data_df.head()
# Predict the traffic situation
predicted_traffic = RForest_clf.predict(new_data_df)

# Convert prediction to category
traffic_mapping = {0: 'Low', 1: 'Normal', 2: 'Heavy', 3: 'High'}
predicted_traffic_category = traffic_mapping[predicted_traffic[0]]
# Get the current date and time
now = datetime.now()
date = now.day
day_of_week = now.weekday()  # Monday is 0, Sunday is 6
hour = now.hour
minute = now.minute
am_pm = 'PM' if hour >= 12 else 'AM'  # 1 for PM, 0 for AM

# Convert 24-hour time to 12-hour format
if hour > 12:
    hour -= 12


# Create the formatted time string with AM/PM
time_str = f"{hour:02d}:{minute:02d} {am_pm}"

# Prepare the output data (time and prediction)
output_data = {
    'Time': time_str,
    'Predicted Traffic Situation': predicted_traffic_category
}

# Convert the data to a DataFrame for saving
output_df = pd.DataFrame([output_data])

# Save to CSV in the desired format (without header, append mode)
output_df.to_csv('/content/drive/MyDrive/TrafficPrediction/PredictedTraffic.csv', mode='a', header=False, index=False)

print(f"Predicted Traffic Situation: {predicted_traffic_category} at {time_str}")
print("Prediction saved successfully to 'predicted_traffic.csv'.")
