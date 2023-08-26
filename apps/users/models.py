from django.db import models
# from django_resized.forms import ResizedImageField

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
    user_image = models.ImageField(
        upload_to='image_users/',
        verbose_name="Фотография пользователя",
    )
    user_level = models.CharField(
        max_length=244,
        verbose_name= "Уровень студента"
    )
    
    def __str__(self):
        return f"Имя: {self.user_name} - Айди: {self.user_id}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"