# Generated by Django 4.2.1 on 2023-06-02 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_age',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_gender',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_target',
        ),
    ]