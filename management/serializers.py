from rest_framework import serializers
from booking.models import Booking
from restaurants.models import Restaurant
from .models import Manager, Employee


class RestaurantSerializer(serializers.ModelSerializer):
    class RestaurantSerializer(serializers.ModelSerializer):
        class Meta:
            model = Restaurant
            fields = [
                'id', 'author', 'restaurant_name', 'picture', 'description',
                'service_fee', 'booking_count_total', 'booking_count_day_by_day',
                'address', 'phone', 'email', 'category', 'created_at', 'updated_at'
            ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'author', 'restaurants', 'room', 'number_of_people',
            'meals', 'contact_number', 'contact_username', 'comment',
            'occasion', 'status', 'paying_status', 'booked_time', 'planed_time'
        ]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
