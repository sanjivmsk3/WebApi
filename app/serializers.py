from rest_framework import serializers
from app.models import *

class PositiveNo(serializers.Serializer):
    field1 = serializers.IntegerField()
    class Meta:
        fields = ['field1']



class SlotBooking(serializers.Serializer):
    field1 = serializers.IntegerField()
    field2 = serializers.IntegerField()
    class Meta:
        fields = ['field1','field2']




class SlotBook(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    class Meta:
        fields = ['x','y']