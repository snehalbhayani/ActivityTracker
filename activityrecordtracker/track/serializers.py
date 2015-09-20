from rest_framework import serializers
from track.models import Activity,Feature


class FeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feature

    def __str__(self):
        return 'Serializer for Feature. '+str(self.feature_name)


class ActivitySerializer(serializers.ModelSerializer):
    
    def __str__(self):
        return 'Serializer for Activity . '
    class Meta:
	model=Activity


