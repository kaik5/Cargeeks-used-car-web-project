# Generated by Django 3.2.9 on 2021-11-10 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20211110_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='passengers',
        ),
    ]
