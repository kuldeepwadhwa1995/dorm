# Generated by Django 3.1.3 on 2020-11-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
