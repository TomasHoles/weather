from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Funkce pro získání dat z API
def get_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    data = get_weather_data()
    hourly_data = data['hourly']
    
    # Extrakce potřebných dat pro grafy
    times = hourly_data['time']
    temperatures = hourly_data['temperature_2m']
    humidity = hourly_data['relative_humidity_2m']
    wind_speed = hourly_data['wind_speed_10m']
    
    # Souřadnice města (pro příklad jsem použil konkrétní souřadnice)
    latitude = 43.9391
    longitude = 17.9024
    
    # Posíláme data a souřadnice do šablony
    return render_template(
        'index.html',
        times=times,
        temperatures=temperatures,
        humidity=humidity,
        wind_speed=wind_speed,
        latitude=latitude,
        longitude=longitude
    )

if __name__ == '__main__':
    app.run(debug=True)