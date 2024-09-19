import pandas as pd
from datetime import datetime
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('/content/drive/MyDrive/Trafficdetectionruns/detect/train/weights/best.pt')

# Run the detection on the video
results = model.predict(source='/content/drive/MyDrive/Trafficdetectionruns/predict/trafficvideo.avi', conf=0.25, save=True)

# Class names as per YOLOv8 model (you may need to adjust these based on your training)
vehicle_classes = {'bike': 0, 'bus': 1, 'car': 2, 'green-light': 3,'motorbike':4,'red-light':5,'truck':6,'yello-light':7}  # Example class IDs for car, bike, etc.
vehicle_count = {'bike': 0, 'bus': 0, 'car': 0, 'green-light': 0,'motorbike':0,'red-light':0,'truck':0,'yello-light':0}


# Count vehicles from the results
for result in results:
    for box in result.boxes:
        cls_id = int(box.cls)
        for vehicle, cls in vehicle_classes.items():
            if cls_id == cls:
                vehicle_count[vehicle] += 1

# Get the current date and time
now = datetime.now()
date = now.day
day_of_week = now.weekday()  # Monday is 0, Sunday is 6
hour = now.hour
print(hour)
minute = now.minute
am_pm = 1 if hour >= 12 else 0  # 1 for PM, 0 for AM

# Convert 24-hour time to 12-hour format
if hour > 12:
    hour -= 12

# Prepare the data in the specified format
new_data = {
    'Date': date,
    'Day of the week': day_of_week,
    'CarCount': vehicle_count['car'],
    'BikeCount': vehicle_count['bike'],
    'BusCount': vehicle_count['bus'],
    'TruckCount': vehicle_count['truck'],
    'Total': sum(vehicle_count.values()),
    'hour': hour,
    'minute': minute,
    'AM/PM': am_pm
}

# Convert the data to a pandas DataFrame
df = pd.DataFrame([new_data])

# Save the data to a CSV file
df.to_csv('/content/drive/MyDrive/Trafficdetectionruns/Vehicle_counts.csv', index=False)

print("Vehicle counts with time and date saved to CSV:")
print(df)
