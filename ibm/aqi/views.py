from django.shortcuts import render
from pathlib import Path
import joblib
from django.http import HttpResponse



BASE_DIR=Path(__file__).resolve().parent.parent.parent
model_path=BASE_DIR/"trained_models"/"random_forest.pkl"
model=joblib.load(model_path)

# Create your views here.
def home(request):

    import pandas as pd

    sample = pd.DataFrame([{
    "Unnamed: 0": 0,
    "Month": 6,
    "Is_Weekend": 0,
    "Humidity_Percent": 65,
    "Dew_Point_C": 20,
    "Wind_Speed_10m_kmh": 12,
    "Precipitation_mm": 0,
    "Pressure_MSL_hPa": 1013,
    "Surface_Pressure_hPa": 1008,
    "Solar_Radiation_Wm2": 650,
    "Cloud_Cover_Percent": 35,
    "Sunshine_Seconds": 28000,
    "PM2_5_ugm3": 48,
    "PM10_ugm3": 75,
    "PM_Ratio": 0.64,
    "CO_ugm3": 800,
    "NO2_ugm3": 28,
    "SO2_ugm3": 10,
    "O3_ugm3": 42,
    "Dust_ugm3": 60,
    "AOD": 0.45,
    "Festival_Period": 0,
    "Crop_Burning_Season": 0,

    "City_Ahmedabad": 0,
    "City_Aizawl": 0,
    "City_Bengaluru": 0,
    "City_Bhopal": 0,
    "City_Bhubaneswar": 0,
    "City_Chandigarh": 0,
    "City_Chennai": 0,
    "City_Dehradun": 0,
    "City_Delhi": 1,
    "City_Gangtok": 0,
    "City_Gurugram": 0,
    "City_Guwahati": 0,
    "City_Hyderabad": 0,
    "City_Imphal": 0,
    "City_Itanagar": 0,
    "City_Jaipur": 0,
    "City_Kohima": 0,
    "City_Kolkata": 0,
    "City_Lucknow": 0,
    "City_Mumbai": 0,
    "City_Panaji": 0,
    "City_Patna": 0,
    "City_Raipur": 0,
    "City_Ranchi": 0,
    "City_Shillong": 0,
    "City_Shimla": 0,
    "City_Thiruvananthapuram": 0,
    "City_Visakhapatnam": 0,
}])
    print(model.predict(sample))
    return HttpResponse("Prediction completed. Check the terminal.")