# Generated by Django 3.0.1 on 2020-08-30 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweets',
            options={'ordering': ['-id']},
        ),
    ]
