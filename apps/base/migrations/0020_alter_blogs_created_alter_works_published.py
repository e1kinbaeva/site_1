# Generated by Django 5.0.6 on 2024-06-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_blogs_created_alter_works_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='works',
            name='published',
            field=models.DateField(auto_now_add=True, verbose_name='Опубликовано'),
        ),
    ]
