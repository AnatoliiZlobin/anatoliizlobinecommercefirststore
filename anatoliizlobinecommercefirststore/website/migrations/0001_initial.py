# Generated by Django 3.1.3 on 2020-11-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('number', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('price', models.FloatField(max_length=10)),
                ('stock_bool', models.BooleanField(default=False)),
                ('stock_int', models.IntegerField()),
            ],
        ),
    ]
