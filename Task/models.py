from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Tag(models.Model):
    tag_title = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_title

class Task(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        print('get absolute url : ', reverse("task-detail", kwargs={'slug': self.slug}))
        return reverse("task-detail", kwargs={'slug': self.slug})

    class Meta:
       ordering = ('-added', )
