import email
from email.policy import default
from operator import mod
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

import uuid

# Create your models here.sss


class Organization(models.Model)   :
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True,null = False)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)
    deleted_by = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return self.id

    
class Department(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Agent_Model(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    email = models.EmailField(max_length = 254,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    department_data = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Bot_Model(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    organization_data = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Channel_Model(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    Bot_data = models.ForeignKey(Bot_Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Conversations_Model(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    Bot_data = models.ForeignKey(Bot_Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

