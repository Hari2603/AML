# Generated by Django 3.1.5 on 2021-02-16 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210216_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='finreq',
            name='user_id',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='financer_id', to='accounts.financer'),
            preserve_default=False,
        ),
    ]
