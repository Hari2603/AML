# Generated by Django 3.1.5 on 2021-02-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210215_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financer',
            name='Address',
            field=models.CharField(default='Enter Address Here', max_length=200),
        ),
    ]
