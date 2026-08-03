from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("predict/", views.predict, name="predict"),
    path("insights/", views.insights, name="insights"),
    path("aqi-meter/", views.aqi_meter, name="aqi_meter"),
]

# Print all registered routes on startup
BASE = "http://127.0.0.1:8000"
print("\n" + "=" * 50)
print("  AirIntel - Registered Routes")
print("=" * 50)
for pattern in urlpatterns:
    name = pattern.name or "unnamed"
    url = f"{BASE}/{pattern.pattern}" if pattern.pattern else f"{BASE}/"
    print(f"  {name:<12} →  {url}")
print("=" * 50 + "\n")
