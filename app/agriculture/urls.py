from django.urls import path,include

from agriculture.views import PlotAPIView,PlotDetailAPIView


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('plot/', PlotAPIView.as_view(), name='plots_list'),
    path('plot/<int:pk>',PlotDetailAPIView.as_view(),name='plot_detail')
    
]