# Generated by Django 3.1.2 on 2020-11-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryApp', '0002_auto_20201125_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='content',
            field=models.TextField(),
        ),
    ]
