# Generated by Django 4.2.1 on 2023-06-03 03:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options_remove_users_user_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Фотография пользователя'),
        ),
    ]