from django.urls import path
from .views import heatmap, home

urlpatterns = [
    path('', home, name='home'),  # Just use 'home' instead of 'home.views'
    path ('heatmap/', heatmap, name='heatmap'),  # Include the heatmap view
]
