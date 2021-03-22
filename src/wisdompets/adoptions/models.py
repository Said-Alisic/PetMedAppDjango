from django.db import models

# Create model by defining a class that
# inherits the django.db.models Model class
class Pet(models.Model):
    # Create fields of model
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')] # Constant choices
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    # Choices means there will be some
    # choices to choose from
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # Tells django what the string representation
    # should be for this model
    def __str__(self):
        return self.name
