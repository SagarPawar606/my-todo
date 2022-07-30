from turtle import title
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={'slug': self.slug})

    class Meta:
       ordering = ('-added', )
