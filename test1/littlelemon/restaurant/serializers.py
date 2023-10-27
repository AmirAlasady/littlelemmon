from .models import Menu, Booking
from rest_framework import serializers



class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title','price','inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'