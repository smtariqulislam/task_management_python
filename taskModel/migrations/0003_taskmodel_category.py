# Generated by Django 5.1.3 on 2025-01-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskCategory', '0002_remove_taskcategory_taskmodel'),
        ('taskModel', '0002_rename_name_taskmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(to='taskCategory.taskcategory'),
        ),
    ]
