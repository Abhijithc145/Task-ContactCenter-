from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

import uuid

# Create your models here.


class Organizations(models.Model)   :
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True,null = True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)
    deleted_by = models.CharField(max_length = 100,null = True)

    
class Department(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    organization = models.ForeignKey(Organizations,on_delete=models.CASCADE)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)


