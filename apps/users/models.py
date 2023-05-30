from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(
        max_length=255,
        verbose_name="ID Пользователя"
    )
    user_name = models.CharField(
        max_length=255,
        verbose_name="Имя Пользователя"
    )
    user_target = models.TextField(
        verbose_name="Цель пользователя"
    )
    user_image = models.ImageField(
        upload_to="user_image/",
        verbose_name="Фотография пользователя"
    )
    user_gender = models.CharField(
        max_length=255,
        verbose_name="Пол пользователя"
    )
    user_age = models.IntegerField(
        verbose_name="Возраст пользователя"
    )
    
    def __str__(self):
        return f"Имя: {self.user_name} - Возраст: {self.user_age}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"