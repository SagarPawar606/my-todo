# Generated by Django 4.0.6 on 2022-07-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-added',)},
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
