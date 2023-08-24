from django.db import models
from django_resized.forms import ResizedImageField
# Create your models here.
class Users(models.Model):
    user_id = models.CharField(
        max_length=255,
        verbose_name="Id Пользователя"
    )
    user_name = models.CharField(
        max_length=255,
        verbose_name="Имя Пользователя"
    )
    user_image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Фотография пользователя",
        blank = True, null = True
    )
    
    def __str__(self):
        return f"Имя: {self.user_name} - Айди: {self.user_id}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"