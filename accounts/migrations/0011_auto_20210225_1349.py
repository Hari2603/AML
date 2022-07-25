# Generated by Django 3.1.5 on 2021-02-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210225_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finreq',
            name='address',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='city',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='contactnumber',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='firstname',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='grossincome',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='lastname',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='middlename',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='finreq',
            name='occupation',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='Companyname',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='Contactnumber',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='Email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='address',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='brand',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='city',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='fueltype',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='modelname',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='price',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='sellnewcar',
            name='variant',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
