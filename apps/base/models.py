from django.db import models

# Create your models here.

class Settings(models.Model):
    address = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    whatsapp_phone = models.CharField(
        max_length = 255,
        verbose_name = 'Ватсап номер'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    instagram = models.URLField(
        verbose_name = 'Инстаграм'
    )
    telegram = models.URLField(
        verbose_name = 'Телеграм'
    )
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'



class About(models.Model):
    image = models.ImageField(
        upload_to = 'about/',
        verbose_name = 'Фото'
    )
    fullname = models.CharField(
        max_length = 255,
        verbose_name = 'ФИО'
    )
    phrase = models.TextField(
        verbose_name='фраза'
    )
    def __str__(self):
        return self.fullname
    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


class Rewards(models.Model):
    title = models.CharField(
    max_length = 255,
    verbose_name = 'Название награды'
    )
    year = models.IntegerField(
        verbose_name="Год получения"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'

class Positions(models.Model):
    title = models.CharField(
    max_length = 255,
    verbose_name = 'Название должности'
    )
    full_info = models.TextField(
        verbose_name = "Название обр.уч. и дата"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
class Education(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название профессии"
    )
    description = models.TextField(
        verbose_name="Место обучение и год"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("Образование")
        verbose_name_plural = ("Образование")

class Works(models.Model):
    image = models.ImageField(
        upload_to= "works/",
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название работы"
    )
    published = models.DateField(
        verbose_name="Опубликовано"
    )
    description = models.TextField(
        verbose_name="Описание работы"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

class Experience(models.Model):
    data = models.CharField(
        max_length=255,
        verbose_name="Дата"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.data
    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

class Research(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Иследования'
        verbose_name_plural = 'Иследования'
    
class Interests(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Интересы'
        verbose_name_plural = 'Интересы'

class Blogs(models.Model):
    image = models.ImageField(
        upload_to= "blogs/",
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    created = models.DateField(
        verbose_name="Дата создания"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Последний блог'
        verbose_name_plural = 'Последние блоги'