from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=20, default='Не дали название')
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Webinar'
        verbose_name_plural = 'Webinars'
