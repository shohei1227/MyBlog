from django.conf import settings
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField

# Create your models here.

## Category model
class Category(models.Model):
    name = models.CharField("Category", max_length=20)

    def __str__(self):
        return self.name

## Tag model
'''
class Tag(models.Model):
    name = models.CharField("Tag", max_length=20)

    def __str__(self):
        return self.name
'''





class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.PROTECT
    )
    #tag = models.ManyToManyField(Tag, verbose_name='Tag')

    title = models.CharField(max_length=30)
    text = MDTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




