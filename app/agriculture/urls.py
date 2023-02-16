from django.urls import path,include

from agriculture.views import PlotView


urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('plot/', PlotView.as_view())
    
]