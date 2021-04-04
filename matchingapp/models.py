# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=500)
    gender = models.CharField(max_length=5)


class DogMatch(models.Model):
    dog_like_sender = models.ForeignKey(
        Dog, related_name="dog_like_sender+", on_delete=models.CASCADE, null=True
    )
    dog_like_receiver = models.ForeignKey(
        Dog, related_name="dog_like_receiver+", on_delete=models.CASCADE, null=True
    )
