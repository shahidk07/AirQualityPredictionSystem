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

    import pandas as pd
    
    # print(model.predict(sample))
    return render(request,'home.html')
            
    
def predict(request):
    if(request.method=="POST"):
        df=process_data(request)
    return render(request,'predict.html')
















