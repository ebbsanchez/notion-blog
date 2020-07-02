from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class Filter(TimeStampedModel):
    name = models.CharField(max_length=200)
    # demo = models.FileField(
        # upload_to='./videos/', null=True, verbose_name="")

    demo = models.CharField(max_length=400)
    link = models.CharField(max_length=100)
    avatar = models.CharField(max_length=400)
    # slug = models.SlugField(unique=True)

    def __str__(self):
    	return self.name
