# Generated by Django 3.1.2 on 2020-12-02 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaryApp', '0004_auto_20201125_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memory',
            options={'ordering': ['-date']},
        ),
    ]
