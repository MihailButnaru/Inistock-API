"""This module represents the view of the person resource"""

from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from inistock.models import PersonServiceManagement
from inistock.serializers import InputPersonSerializer, OutputPersonSerializer


class PersonViewSet(ViewSet):
    """PersonViewset provides to create, retrieve and patch"""

    def create(self, request: WSGIRequest):
        """create a person object
        Args:
            request (WSGIRequest): request data
        Returns:
            (OutputPersonSerializer): created person
        """
        serializer = InputPersonSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        person = PersonServiceManagement.create_object(
            data=serializer.validated_data["person"]
        )

        return Response(
            status=status.HTTP_201_CREATED, data=OutputPersonSerializer(person).data
        )

    def update(self, request: WSGIRequest, person_id: int):
        """Updates the person based on the id provided
        Args:
            person_id (int): unique identifier of the person object
            request (WSGIRequest): request data
        Returns:
            (OutputPersonSerializer): updated person
        """
        serializer = InputPersonSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        updated_person = PersonServiceManagement.update_object(
            data=serializer.validated_data["person"], person_id=person_id
        )

        return Response(
            status=status.HTTP_200_OK, data=OutputPersonSerializer(updated_person).data
        )

    def retrieve(self, request: WSGIRequest, person_id: int):
        """Retrieves a person based on the id provided
        Args:
            person_id (int): unique identifier of the person object
        Returns:
            (OutputPersonSerializer): person
        """
        retrieve_person = PersonServiceManagement.retrieve_object(person_id=person_id)

        return Response(
            status=status.HTTP_200_OK, data=OutputPersonSerializer(retrieve_person).data
        )
