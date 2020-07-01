from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class Filters(TimeStampedModel):
    name = models.CharField(max_length=200)
    demo = models.FileField(
        upload_to='./videos/', null=True, verbose_name="")

    link = models.CharField(max_length=100)
    avatar = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
