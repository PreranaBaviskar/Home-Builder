# Generated by Django 3.0 on 2020-03-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='text',
            field=models.TextField(default='now', max_length=200),
        ),
        migrations.AddField(
            model_name='info',
            name='title',
            field=models.TextField(default='here', max_length=200),
        ),
    ]