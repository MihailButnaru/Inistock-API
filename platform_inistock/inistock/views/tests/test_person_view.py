"""Tests to test the functionality of the person viewset"""
from unittest import TestCase
from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APIRequestFactory

from inistock.views.person_view import PersonViewSet
from inistock.views.tests.mock_data import (
    mock_input_data_person,
    mock_output_data_person,
)


class TestPersonViewSet(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.format = "json"

        self.input_data = mock_input_data_person()
        self.output_data = mock_output_data_person()
        self.person_id = self.output_data["person_id"]

    def _request_create_person(self, *, input_data: dict):
        request = self.factory.post(
            path="/v1/person", data=input_data, format=self.format
        )

        response = PersonViewSet.as_view(actions={"post": "create"})(request)

        return response

    def _request_update_person(self, *, input_data: dict):
        request = self.factory.patch(
            path=f"/v1/person/{self.person_id}", data=input_data, format=self.format
        )

        response = PersonViewSet.as_view(actions={"patch": "update"})(
            request, self.person_id
        )

        return response

    @patch("inistock.views.person_view.PersonServiceManagement")
    def test_create_person(self, mock_person_service_management):
        mock_person_service_management.create_object.return_value = self.output_data

        response = self._request_create_person(input_data=self.input_data)

        mock_person_service_management.assert_not_called()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.output_data)

    def test_create_person_invalid_input_data(self):
        input_data = self.input_data
        del input_data["person"]

        response = self._request_create_person(input_data=input_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("inistock.views.person_view.PersonServiceManagement")
    def test_update_person(self, mock_person_service_management):
        mock_person_service_management.update_object.return_value = self.output_data

        response = self._request_update_person(input_data=self.input_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.output_data)

    def test_update_person_invalid_input_data(self):
        input_data = self.input_data
        del input_data["person"]

        response = self._request_update_person(input_data=input_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("inistock.views.person_view.PersonServiceManagement")
    def test_retrieve_person(self, mock_person_service_management):
        mock_person_service_management.retrieve_object.return_value = self.output_data

        request = self.factory.get(
            path=f"/v1/person/{self.person_id}", format=self.format
        )

        response = PersonViewSet.as_view(actions={"get": "retrieve"})(
            request, self.person_id
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.output_data)
