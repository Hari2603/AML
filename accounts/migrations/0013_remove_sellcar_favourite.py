# Generated by Django 3.1.5 on 2021-03-02 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_sellcar_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellcar',
            name='favourite',
        ),
    ]
