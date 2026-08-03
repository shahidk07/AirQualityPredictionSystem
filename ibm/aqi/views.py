from django.shortcuts import render
from pathlib import Path
import joblib
from django.http import HttpResponse
from .services import process_data


BASE_DIR=Path(__file__).resolve().parent.parent.parent
model_path=BASE_DIR/"trained_models"/"random_forest.pkl"
model=joblib.load(model_path)

# Create your views here.
def home(request):

    
    return render(request,'home.html')
            
    
from django.http import JsonResponse

def predict(request):
    print("Predict view called")
    if request.method == "POST":
        df = process_data(request)
        result = model.predict(df)[0]
        print(result)
        return JsonResponse({"result": result})
    return render(request, 'predict.html')

def insights(request):
    return render(request,'insights.html')

def about(request):
    return render(request,'about.html')

def aqi_meter(request):
    return render(request,'aqi_meter.html')













