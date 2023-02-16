from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from agriculture.serializers import PlotSerializer
from agriculture.models import Plot


class PlotAPIView(generics.ListCreateAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Plot.objects.filter(
            farmer__user_name=self.request.user.id
        )
        return queryset
    
    def get_serializer_context(self):
        context = super(PlotAPIView, self).get_serializer_context()
        context.update({"request_farmer_id": self.request.user.farmer})
        print(context)
        return context
    
class PlotDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Plot.objects.filter(
            farmer__user_name=self.request.user.id
        )
        return queryset