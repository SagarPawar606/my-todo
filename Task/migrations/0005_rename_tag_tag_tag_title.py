# Generated by Django 4.0.6 on 2022-12-02 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_tag_task_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='tag_title',
        ),
    ]
