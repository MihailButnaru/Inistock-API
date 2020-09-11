from django.db import models


class PersonModel(models.Model):
    """Person model
    Represents the information of the person
    """

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=50)
