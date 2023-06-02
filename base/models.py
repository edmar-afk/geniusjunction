from django.db import models
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


now = timezone.now()

class Files(models.Model):
    files = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'word', 'excel'])],)
    date = models.DateField(default=now)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    type = models.CharField(max_length=200)