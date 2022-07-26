# Generated by Django 3.1.5 on 2021-02-16 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_financer_companyname'),
    ]

    operations = [
        migrations.CreateModel(
            name='finreq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='Hari', max_length=250)),
                ('middlename', models.CharField(default='Hari', max_length=250)),
                ('lasttname', models.CharField(default='Hari', max_length=250)),
                ('contactnumber', models.CharField(default='9999999999', max_length=10)),
                ('email', models.EmailField(default='abc@xyz.com', max_length=50)),
                ('dateofb', models.DateField(default=datetime.date.today)),
                ('maritalstatus', models.CharField(choices=[('MA', 'MARRIED'), ('UM', 'UNMARRIED')], default='UM', max_length=2)),
                ('address', models.TextField(default='home address', max_length=250)),
                ('city', models.CharField(default='New Delhi', max_length=25)),
                ('occupation', models.CharField(default='IT Job', max_length=25)),
                ('grossincome', models.CharField(default='150000', max_length=10)),
                ('aadharcard', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pancard', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('bankstatement', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('passportsizephoto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('ITreturn', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
