# Generated by Django 3.1.3 on 2020-11-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamain',
            name='stock_int',
            field=models.IntegerField(null=True),
        ),
    ]
