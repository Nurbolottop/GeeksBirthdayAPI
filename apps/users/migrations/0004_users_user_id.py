# Generated by Django 4.2.1 on 2023-06-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_id',
            field=models.CharField(default=1, max_length=255, verbose_name='Id Пользователя'),
            preserve_default=False,
        ),
    ]
