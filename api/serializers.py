from meetings.models import Meeting
from rest_framework import serializers


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['code','title','time','address']


    