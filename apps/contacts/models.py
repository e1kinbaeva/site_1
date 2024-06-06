from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        max_length = 255,
        verbose_name = 'Email'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    message = models.TextField(
        verbose_name = 'Сообщение'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Journal(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    text = models.TextField(
        verbose_name = 'Текст'
    )
    type = models.CharField(
        max_length = 255,
        verbose_name = 'Тип'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журнал'

class Expert(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название эксперта'
    )
    text = models.CharField(
        max_length = 255,
        verbose_name = 'Текст'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Эксперт'
        verbose_name_plural = 'Эксперты'