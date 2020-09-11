"""Tests to test the functionality of the serializer"""
from unittest import TestCase

from inistock.serializers import (
    PersonSerializer,
    InputPersonSerializer,
    OutputPersonSerializer,
)


class TestPersonSerializer(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "first_name": "Test",
            "last_name": "Smith",
            "date_of_birth": "2020-01-01",
            "email": "testsmith@hotmail.com",
        }

    def test_it_can_serialize(self):
        inst = PersonSerializer(data=self.input_data)
        inst.is_valid(raise_exception=True)

        self.assertSetEqual(set(inst.validated_data), set(self.input_data))

    def test_it_can_serialize_input_data(self):
        input_data = {}
        input_data["person"] = self.input_data

        inst = InputPersonSerializer(data=input_data)
        inst.is_valid(raise_exception=True)

        self.assertSetEqual(
            set(inst.validated_data["person"]), set(input_data["person"])
        )

    def test_it_can_serialize_output_data(self):
        output_data = self.input_data

        inst = OutputPersonSerializer(data=output_data)
        inst.is_valid(raise_exception=True)

        self.assertSetEqual(set(inst.validated_data), set(output_data))
