from django.core.exceptions import ObjectDoesNotExist

from inistock.exceptions.api_exceptions import PersonNotFound, ShareNotFound
from inistock.models.person_model import PersonModel
from inistock.models.share_model import ShareModel


class PersonServiceManagement:
    @staticmethod
    def create_object(data: dict) -> PersonModel:
        """Creates a person object in the database
        Args:
            data (dict): person information
        Returns:
            created person (PersonModel)
        """
        person_object = PersonModel(**data)
        person_object.save()
        return person_object

    @staticmethod
    def update_object(*, data: dict, person_id: int) -> PersonModel:
        """Updates a person object if the person id is provided
        Args:
            data (dict): person information
            person_id (int): unique identifier of the person object
        Returns:
            updated person
        """
        try:
            PersonModel.objects.filter(person_id=person_id).update(**data)
        except ObjectDoesNotExist:
            raise PersonNotFound(detail=f"Person with id {person_id} does not exist")

        updated_person = PersonModel.objects.get(person_id=person_id)

        return updated_person

    @staticmethod
    def retrieve_object(person_id: int) -> PersonModel:
        """Retrieves the person object based on the person id provided
        Args:
            person_id (int): unique identifier of the person object
        Returns:
            person
        """
        try:
            person = PersonModel.objects.get(person_id=person_id)
        except ObjectDoesNotExist:
            raise PersonNotFound(detail=f"Person with id {person_id} does not exist")
        return person


class ShareServiceManagement:
    @staticmethod
    def create_object(data: dict, person_id: int) -> ShareModel:
        """Creates a share object
        Args:
            data (dict): information about the share
            person_id (int): unique identifier of the person object
        Returns:
            (ShareModel): created share
        """
        person = PersonServiceManagement.retrieve_object(person_id=person_id)

        share = ShareModel.objects.create(person=person, **data)
        return share

    @staticmethod
    def update_object(*, data: dict, person_id: int, share_id: int) -> ShareModel:
        """Updates a share object of the person
        Args:
            data (dict): information about the share
            person_id (int): unique identifier of the person object
            share_id (int): unique identifier of the share object
        Returns:
            (ShareModel): updated share
        """
        person = PersonServiceManagement.retrieve_object(person_id=person_id)

        try:
            ShareModel.objects.filter(share_id=share_id).update(person=person, **data)
        except ObjectDoesNotExist:
            raise ShareNotFound(detail=f"Share with id {share_id} does not exist")

        updated_share = ShareModel.objects.get(share_id=share_id)

        return updated_share

    @staticmethod
    def delete_object(*, share_id: int, person_id: int) -> ShareModel:
        """Deleted share object
        Args:
            share_id (int): unique identifier of the share object
            person_id (int): unique identifier of the share object
        Returns:
            (ShareModel): share object
        """
        person = PersonServiceManagement.retrieve_object(person_id=person_id)

        try:
            share = ShareModel.objects.filter(share_id=share_id).get(person=person)
        except ObjectDoesNotExist:
            raise ShareNotFound(detail=f"Share with id {share_id} does not exist")

        share.delete()

        return share

    @staticmethod
    def retrieve_object(*, share_id: int, person_id: int) -> ShareModel:
        """Retrieves share object
        Args:
            share_id (int): unique identifier of the share object
            person_id (int): unique identifier of the person object
        Returns:
            (ShareModel): share object
        """
        person = PersonServiceManagement.retrieve_object(person_id=person_id)

        try:
            share = ShareModel.objects.filter(share_id=share_id).get(person=person)
        except ObjectDoesNotExist:
            raise ShareNotFound(detail=f"Share with id {share_id} does not exist")

        return share

    @staticmethod
    def retrieve_objects(person_id: int) -> ShareModel:
        """Retrieves all the shares of the person
        Args:
            person_id (int): unique identifier of the person object
        Returns:
            (ShareModel): share objects
        """
        person = PersonServiceManagement.retrieve_object(person_id=person_id)

        shares = ShareModel.objects.filter(person=person)

        return shares
