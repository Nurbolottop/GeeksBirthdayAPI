from django.db import models
# from django_resized.forms import ResizedImageField

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(
        max_length=255,
        verbose_name="Пол Пользователя"
    )
    def __str__(self):
        return f" {self.gender}"
    
    class Meta:
        verbose_name = "1) Добавить уровни"
        verbose_name_plural = "1) Добавить уровни"

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
    user_level = models.ForeignKey(
        Gender,
        on_delete = models.CASCADE,
        related_name = "level",
        verbose_name = "Выберите уровень"
    )
    
    def __str__(self):
        return f" Имя: {self.user_name} - Айди: {self.user_id}"
    
    class Meta:
        verbose_name = "2) Пользователь"
        verbose_name_plural = "2) Пользователи"