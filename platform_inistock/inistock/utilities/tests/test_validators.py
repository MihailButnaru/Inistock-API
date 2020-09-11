"""Tests to test the functionality of the validators"""
from unittest import TestCase
from unittest.mock import MagicMock

from inistock.exceptions.api_exceptions import PersonIDNotValid
from inistock.utilities.validators import get_person_id


class TestValidators(TestCase):
    def test_get_person_id(self):
        request = MagicMock()
        request.headers = {"PERSON-ID": 1}

        person_id = get_person_id(request=request)

        self.assertEqual(person_id, 1)

    def test_get_person_id_not_present(self):
        request = MagicMock()
        request.headers = {"Content-Type": "application/json"}
        request.method = "POST"

        with self.assertRaises(PersonIDNotValid) as ex:
            get_person_id(request=request)

        self.assertEqual(
            str(ex.exception),
            f"[PERSON-ID] header is missing while doing a POST request",
        )
