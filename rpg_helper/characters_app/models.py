from django.db import models
from django.utils import timezone
# Create your models here.


class Character(models.Model):

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40, null=True, blank=True)
    middle_name = models.CharField(max_length=40, null=True, blank=True)
    surname = models.CharField(max_length=40, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    alive = models.BinaryField()
    race = models.CharField(null=True, max_length=50, blank = True)
    main_story = models.TextField(null=True, blank = True)
    notes = models.TextField(null=True, blank=True)
    #TODO: add a campain model and campain variable to that model! OR stay with just relational db
    #campain = models.ForeignKey()
    created_date = models.DateTimeField(default=timezone.now)
    #TODO: add proffession. It will be a field from campain modelor separated model.


