# Generated by Django 5.0.6 on 2024-06-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_about_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='facebook',
        ),
        migrations.AddField(
            model_name='settings',
            name='telegram',
            field=models.URLField(default=1, verbose_name='Телеграм'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='whatsapp_phone',
            field=models.CharField(max_length=255, verbose_name='Ватсап номер'),
        ),
    ]
