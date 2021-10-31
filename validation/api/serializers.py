from rest_framework import serializers
from .models import Student


def start_with_a(value):
    if value[0].lower() != "a":
        raise serializers.ValidationError("Name must be start with A")
    return value


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_a])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validation
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError("Seat full")
        return value
    # object level validation

    def validate(self, attrs):
        if attrs.get('city').lower() != "narowal":
            raise serializers.ValidationError("City must be Narowal")
        return attrs
