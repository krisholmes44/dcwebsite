# Generated by Django 3.2.5 on 2021-12-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmas', '0004_bookstores_dc_facts_entertainment'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_facts',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
