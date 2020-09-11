"""Tests to test the functionality of the share viewset"""
from unittest import TestCase
from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APIRequestFactory

from inistock.views.share_view import ShareViewSet
from inistock.views.tests.mock_data import (
    mock_input_data_share,
    mock_output_data_share,
    mock_output_data_shares,
)


class TestShareViewSet(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.format = "json"

        self.input_data = mock_input_data_share()
        self.output_data = mock_output_data_share()
        self.output_data_shares = mock_output_data_shares()
        self.share_id = self.output_data["share_id"]

        self.headers = {"PERSON-ID": 1}

    def _request_create_share(self, *, input_data: dict, headers: dict):
        request = self.factory.post(
            path="/v1/share", data=input_data, format=self.format
        )
        request.headers = headers

        response = ShareViewSet.as_view(actions={"post": "create"})(request)

        return response

    def _request_update_share(self, *, input_data: dict, headers: dict):
        request = self.factory.patch(
            path=f"/v1/share/{self.share_id}", data=input_data, format=self.format
        )
        request.headers = headers

        response = ShareViewSet.as_view(actions={"patch": "update"})(
            request, self.share_id
        )

        return response

    def _request_retrieve_share(self, headers: dict):
        request = self.factory.get(
            path=f"/v1/share/{self.share_id}", format=self.format
        )
        request.headers = headers

        response = ShareViewSet.as_view(actions={"get": "retrieve"})(
            request, self.share_id
        )

        return response

    def _request_delete_share(self, headers: dict):
        request = self.factory.delete(
            path=f"/v1/share/{self.share_id}", format=self.format
        )
        request.headers = headers

        response = ShareViewSet.as_view(actions={"delete": "delete"})(
            request, self.share_id
        )

        return response

    def _request_retrieve_shares(self, headers: dict):
        request = self.factory.get(path="/v1/share", format=self.format)
        request.headers = headers

        response = ShareViewSet.as_view(actions={"get": "list"})(request)

        return response

    @patch("inistock.views.share_view.ShareServiceManagement")
    def test_create_share(self, mock_share_service_management):
        mock_share_service_management.create_object.return_value = self.output_data

        response = self._request_create_share(
            input_data=self.input_data, headers=self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.output_data)

    def test_create_share_without_header(self):
        response = self._request_create_share(input_data=self.input_data, headers={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["message"]),
            "[PERSON-ID] header is missing while doing a POST request",
        )

    def test_create_share_invalid_input_data(self):
        input_data = self.input_data
        del input_data["share"]

        response = self._request_create_share(
            input_data=input_data, headers=self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("inistock.views.share_view.ShareServiceManagement")
    def test_update_share(self, mock_share_service_management):
        mock_share_service_management.update_object.return_value = self.output_data

        response = self._request_update_share(
            input_data=self.input_data, headers=self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.output_data)

    def test_update_share_without_header(self):
        response = self._request_update_share(input_data=self.input_data, headers={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["message"]),
            "[PERSON-ID] header is missing while doing a PATCH request",
        )

    def test_update_share_invalid_input_data(self):
        input_data = self.input_data
        del input_data["share"]

        response = self._request_update_share(
            input_data=self.input_data, headers=self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("inistock.views.share_view.ShareServiceManagement")
    def test_retrieve_share(self, mock_share_service_management):
        mock_share_service_management.retrieve_object.return_value = self.output_data

        response = self._request_retrieve_share(headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.output_data)

    def test_retrieve_share_without_header(self):
        response = self._request_retrieve_share(headers={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["message"]),
            "[PERSON-ID] header is missing while doing a GET request",
        )

    @patch("inistock.views.share_view.ShareServiceManagement")
    def test_delete_share(self, mock_share_service_management):
        mock_share_service_management.delete_object.return_value = self.output_data

        response = self._request_delete_share(headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.output_data)

    def test_delete_share_without_header(self):
        response = self._request_delete_share(headers={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["message"]),
            "[PERSON-ID] header is missing while doing a DELETE request",
        )

    @patch("inistock.views.share_view.ShareServiceManagement")
    def test_retrieve_shares(self, mock_share_service_management):
        mock_share_service_management.retrieve_objects.return_value = (
            self.output_data_shares
        )

        response = self._request_retrieve_shares(headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.output_data_shares)

    def test_retrieve_shares_without_header(self):
        response = self._request_retrieve_shares(headers={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["message"]),
            "[PERSON-ID] header is missing while doing a GET request",
        )
