from django.contrib.auth.models import User
from rest_framework import serializers
from trainapp.models import Schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password',)


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('train',
                  'departure_station',
                  'arrival_station',
                  'departure_time',
                  'arrival_time',
                  'duration'
                  )
