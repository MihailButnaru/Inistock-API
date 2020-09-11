"""Tests to test the functionality of the serializer"""
from unittest import TestCase

from inistock.serializers import (
    ShareSerializer,
    InputShareSerializer,
    OutputShareSerializer,
)


class TestShareSerializer(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "company": "Tesla",
            "symbol": "TSLA",
            "shares": "10",
            "type": "sell",
            "date": "2020-01-01",
            "price": 1417.0,
            "amount": 5000.0,
            "currency": "GB",
            "note": "great investment",
        }

    def test_it_can_serialize(self):
        inst = ShareSerializer(data=self.input_data)

        inst.is_valid(raise_exception=True)

        self.assertSetEqual(set(inst.validated_data), set(self.input_data))

    def test_it_can_serialize_invalid_choice(self):
        input_data = self.input_data
        input_data["type"] = "test"

        inst = ShareSerializer(data=input_data)

        inst.is_valid()

        self.assertEqual(str(inst.errors["type"][0]), '"test" is not a valid choice.')

    def test_it_can_serialize_input_data(self):
        input_data = {}
        input_data["share"] = self.input_data

        inst = InputShareSerializer(data=input_data)
        inst.is_valid(raise_exception=True)

        self.assertSetEqual(set(inst.validated_data), set(input_data))

    def test_it_can_serialize_output_data(self):
        inst = OutputShareSerializer(data=self.input_data)
        inst.is_valid(raise_exception=True)

        self.assertSetEqual(set(inst.validated_data), set(self.input_data))
