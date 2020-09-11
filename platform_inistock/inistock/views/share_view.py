"""This module represents the view of the share resource"""

from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from inistock.models import ShareServiceManagement
from inistock.serializers import InputShareSerializer, OutputShareSerializer
from inistock.utilities import get_person_id


class ShareViewSet(ViewSet):
    """
    This viewset provides actions: to create, get a list, patch and retrieve
    the shares
    """

    def create(self, request: WSGIRequest):
        """Create a share object
        Args:
            request (WSGIRequest): request data
        Returns:
            (OutputShareSerializer): created share
        """
        person_id = get_person_id(request=request)

        serializer = InputShareSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        share = ShareServiceManagement.create_object(
            data=serializer.validated_data["share"], person_id=person_id
        )

        return Response(
            status=status.HTTP_201_CREATED, data=OutputShareSerializer(share).data
        )

    def update(self, request: WSGIRequest, share_id: int):
        """Updates a share object
        Args:
            request (WSGIRequest): request data
            share_id (int): unique identifier of the share object
        Returns:
            (OutputShareSerializer): updated share
        """
        person_id = get_person_id(request=request)

        serializer = InputShareSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        updated_share = ShareServiceManagement.update_object(
            data=serializer.validated_data["share"],
            share_id=share_id,
            person_id=person_id,
        )

        return Response(
            status=status.HTTP_200_OK, data=OutputShareSerializer(updated_share).data
        )

    def delete(self, request: WSGIRequest, share_id: int):
        """Deletes share object
        Args:
            request (WSGIRequest): request data
            share_id (int): unique identifier of the share object
        Returns:
            (OutputShareSerializer): deleted object
        """
        person_id = get_person_id(request=request)

        deleted_share = ShareServiceManagement.delete_object(
            share_id=share_id, person_id=person_id
        )

        return Response(
            status=status.HTTP_200_OK, data=OutputShareSerializer(deleted_share).data
        )

    def retrieve(self, request: WSGIRequest, share_id: int):
        """Retrieves a share object
        Args:
            request (WSGIRequest): request data
            share_id (int): unique identifier of the share object
        Returns:
            (OutputShareSerializer): retrieved share object
        """
        person_id = get_person_id(request=request)

        retrieved_share = ShareServiceManagement.retrieve_object(
            share_id=share_id, person_id=person_id
        )

        return Response(
            status=status.HTTP_200_OK, data=OutputShareSerializer(retrieved_share).data
        )

    def list(self, request: WSGIRequest):
        """Returns the list of shares objects
        Args:
            request (WSGIRequest): request data
        Returns:
            (OutputShareSerializer): retrieves a list of shares

        """
        person_id = get_person_id(request=request)

        list_shares = ShareServiceManagement.retrieve_objects(person_id=person_id)

        return Response(
            status=status.HTTP_200_OK,
            data=OutputShareSerializer(list_shares, many=True).data,
        )
