from django.shortcuts import render
from pathlib import Path
import joblib
from django.http import HttpResponse, JsonResponse
from .services import process_data


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Lazy-load the model to avoid crashes during management commands (collectstatic, migrate)
_model = None

def _get_model():
    global _model
    if _model is None:
        model_path = BASE_DIR / "trained_models" / "xgboost.pkl"
        _model = joblib.load(model_path)
    return _model


# Create your views here.
def home(request):
    return render(request, 'home.html')


def predict(request):
    print("Predict view called")
    if request.method == "POST":
        model = _get_model()
        df = process_data(request)
        result = model.predict(df)[0]
        print(result)
        return JsonResponse({"result": result})
    return render(request, 'predict.html')


def insights(request):
    return render(request, 'insights.html')


def about(request):
    return render(request, 'about.html')


def aqi_meter(request):
    return render(request, 'aqi_meter.html')
