from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_tag_limit(value):
    tags = value.split(',')
    if len(tags) > 5:
        raise ValidationError('You can only enter up to 5 tags.')

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    images = models.ImageField(upload_to='images')
    tags = models.CharField(
        max_length=255,  # Assuming tags are separated by commas
        validators=[validate_tag_limit],
        help_text="Enter up to 5 tags separated by commas."
    )
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
# Create your models here.
