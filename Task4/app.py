import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template

app = Flask(__name__)

# Create the static and templates directories if they don't exist
os.makedirs('static', exist_ok=True)
os.makedirs('templates', exist_ok=True)


@app.route('/')
def home():
    """
    This route performs the data analysis, generates visualizations,
    and serves the main webpage.
    """
    # --- 1. Data Generation and Loading (Simulating a real dataset) ---
    # We create a sample DataFrame to simulate the accident data.
    # In a real-world scenario, you would load this from a CSV or database.
    data = {
        'time_of_day': ['Morning', 'Evening', 'Afternoon', 'Night', 'Afternoon', 'Morning', 'Night', 'Morning', 'Evening'],
        'weather_conditions': ['Clear', 'Rain', 'Cloudy', 'Clear', 'Clear', 'Rain', 'Fog', 'Snow', 'Cloudy'],
        'road_conditions': ['Dry', 'Wet', 'Dry', 'Dry', 'Icy', 'Wet', 'Wet', 'Icy', 'Dry']
    }
    df = pd.DataFrame(data)

    # --- 2. Data Analysis ---
    # Analyze contributing factors
    time_of_day_counts = df['time_of_day'].value_counts()
    weather_counts = df['weather_conditions'].value_counts()
    road_counts = df['road_conditions'].value_counts()

    # --- 3. Visualization Generation ---
    # We will generate three visualizations and save them to the static folder.
    # This allows us to serve them on the webpage.
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Plot 1: Accidents by Time of Day
    plt.figure(figsize=(8, 6))
    sns.barplot(x=time_of_day_counts.index, y=time_of_day_counts.values, palette="viridis")
    plt.title('Accidents by Time of Day')
    plt.xlabel('Time of Day')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('static/accidents_by_time.png')
    plt.close()

    # Plot 2: Accidents by Weather Conditions
    plt.figure(figsize=(8, 6))
    sns.barplot(x=weather_counts.index, y=weather_counts.values, palette="rocket")
    plt.title('Accidents by Weather Conditions')
    plt.xlabel('Weather Conditions')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('static/accidents_by_weather.png')
    plt.close()

    # Plot 3: Accidents by Road Conditions
    plt.figure(figsize=(8, 6))
    sns.barplot(x=road_counts.index, y=road_counts.values, palette="mako")
    plt.title('Accidents by Road Conditions')
    plt.xlabel('Road Conditions')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('static/accidents_by_road.png')
    plt.close()

    # --- 4. Render Template ---
    # Pass the paths to the generated images to the HTML template
    return render_template(
        'index.html',
        time_image_path='static/accidents_by_time.png',
        weather_image_path='static/accidents_by_weather.png',
        road_image_path='static/accidents_by_road.png'
    )

if __name__ == '__main__':
    # Start the Flask development server.
    app.run(debug=True)
