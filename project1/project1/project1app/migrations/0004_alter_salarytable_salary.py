# Generated by Django 4.1.7 on 2023-03-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0003_salarytable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarytable',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
