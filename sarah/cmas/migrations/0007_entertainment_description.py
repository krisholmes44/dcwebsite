# Generated by Django 3.2.5 on 2021-12-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmas', '0006_auto_20211227_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainment',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]