from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_reporter = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="categoryCreatedBy")
    modifie_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  null=True, blank=True, related_name="categorymodifie_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modifie_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name, str(self.id)


class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateField()
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="postCreatedBy")
    modifie_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name="postmodifie_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modifie_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)



