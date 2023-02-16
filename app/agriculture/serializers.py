from rest_framework import serializers
from agriculture.models import Plot


class PlotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plot
        fields = [
            'name',
            'culture',
            'season'
        ]
        
        # def create(self, request, validated_data):
        #     user = self.context['request_user_id']
        #     validated_data['farmer'] = user
        #     event_type = Plot.objects.create(**validated_data)
        #     return event_type