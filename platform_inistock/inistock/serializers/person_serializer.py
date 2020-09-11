from rest_framework import serializers

from inistock.models import PersonModel


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = ["first_name", "last_name", "date_of_birth", "email"]


class InputPersonSerializer(serializers.Serializer):
    person = PersonSerializer(many=False, required=True)


class OutputPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = ["person_id", "first_name", "last_name", "date_of_birth", "email"]
