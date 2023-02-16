from django.shortcuts import render
from rest_framework import generics

from agriculture.serializers import PlotSerializer
from agriculture.models import Plot


class PlotView(generics.ListCreateAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Plot.objects.filter(
            farmer__user_name=self.request.user.id
        )
        return queryset
    
    # def get_serializer_context(self):
    #     context = super(Plot, self).get_serializer_context()
    #     context.update({"request_user_id": self.request.user.id})
    #     print(context)
    #     return context
    
class PlotView(generics.ListCreateAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Plot.objects.filter(
            farmer__user_name=self.request.user.id
        )
        return queryset