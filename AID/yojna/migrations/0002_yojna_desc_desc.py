# Generated by Django 2.0.3 on 2018-04-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yojna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yojna_desc',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
