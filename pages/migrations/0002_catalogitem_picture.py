# Generated by Django 2.0.7 on 2018-07-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
