from rest_framework import serializers
from agriculture.models import Plot


class PlotSerializer(serializers.ModelSerializer):
    
    def create(self,validated_data):
            farmer = self.context['request_farmer_id']
            validated_data['farmer'] = farmer
            plot = Plot.objects.create(**validated_data)
            return plot
    
    class Meta:
        model = Plot
        fields = [
            'name',
            'culture',
            'season'
        ]