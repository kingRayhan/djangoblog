from django.db import models
from froala_editor.widgets import FroalaEditor
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=250, unique=True)
    excerpt = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnail/%y/%m/%d", blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    # Relational Field
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
