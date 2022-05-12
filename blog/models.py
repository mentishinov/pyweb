from django.db import models


class Note(models.Model):
    title = models.CharField(max_length = 100)
    message = models.TextField(max_length = 500)
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)





from django.db import models

# Create your models here.
