import pandas as pd


def process_data(request):
    city_list = [
        "Ahmedabad",
        "Aizawl",
        "Bengaluru",
        "Bhopal",
        "Bhubaneswar",
        "Chandigarh",
        "Chennai",
        "Dehradun",
        "Delhi",
        "Gangtok",
        "Gurugram",
        "Guwahati",
        "Hyderabad",
        "Imphal",
        "Itanagar",
        "Jaipur",
        "Kohima",
        "Kolkata",
        "Lucknow",
        "Mumbai",
        "Panaji",
        "Patna",
        "Raipur",
        "Ranchi",
        "Shillong",
        "Shimla",
        "Thiruvananthapuram",
        "Visakhapatnam",
    ]

    features = {}

    for c in city_list:
        features[f"City_{c}"] = 0

    city = request.POST.get("city")
    features[f"City_{city}"] = 1

    data = {
        "Month": int(request.POST.get("month")),
        "Is_Weekend": int(request.POST.get("is_weekend")),
        # Weather Parameters
        "Humidity_Percent": float(request.POST.get("humidity")),
        "Dew_Point_C": float(request.POST.get("dew_point")),
        "Wind_Speed_10m_kmh": float(request.POST.get("wind_speed")),
        "Precipitation_mm": float(request.POST.get("precipitation")),
        "Pressure_MSL_hPa": float(request.POST.get("pressure_msl")),
        "Surface_Pressure_hPa": float(request.POST.get("surface_pressure")),
        "Solar_Radiation_Wm2": float(request.POST.get("solar_radiation")),
        "Cloud_Cover_Percent": float(request.POST.get("cloud_cover")),
        "Sunshine_Seconds": float(request.POST.get("sunshine")),
        # Pollutants
        "PM2_5_ugm3": float(request.POST.get("pm25")),
        "PM10_ugm3": float(request.POST.get("pm10")),
        "PM_Ratio": float(request.POST.get("pm_ratio")),
        "CO_ugm3": float(request.POST.get("co")),
        "NO2_ugm3": float(request.POST.get("no2")),
        "SO2_ugm3": float(request.POST.get("so2")),
        "O3_ugm3": float(request.POST.get("o3")),
        "Dust_ugm3": float(request.POST.get("dust")),
        "AOD": float(request.POST.get("aod")),
        # Seasonal Factors
        "Festival_Period": int(request.POST.get("festival_period")),
        "Crop_Burning_Season": int(request.POST.get("crop_burning")),
    }

    data.update(features)
    df = pd.DataFrame([data])

    return df
