# Generated by Django 5.0.2 on 2024-04-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]