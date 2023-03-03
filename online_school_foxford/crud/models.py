from django.db import models


class Speakers(models.Model):
    name = models.CharField('ФИО преподавателя', max_length=50)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.name


class SpeakersWebinars(models.Model):
    speaker_id = models.ForeignKey('Speakers', on_delete=models.CASCADE)
    webinar_id = models.ForeignKey('Webinars', on_delete=models.CASCADE)
    date = models.DateTimeField('Начало вебинара')
    time = models.TimeField('Длительность вебинара')

    class Meta:
        verbose_name = 'Дополнительная инофрмация про вебинар'
        verbose_name_plural = 'Дополнительная инофрмация про вебинары'

    def __str__(self):
        return f'вебинар "{self.webinar_id}" будет вести {self.speaker_id}'


class Webinars(models.Model):
    created = 'Создан'
    going = 'Сейчас идет'
    cancelled = 'Отменен'
    completed = 'Завершен'
    status_webinar = [
        (created, 'Создан'),
        (going, 'Сейчас идет'),
        (cancelled, 'Отменен'),
        (completed, 'Завершен'),
    ]

    title_webinar = models.CharField('Название вебинара', max_length=50)
    status = models.CharField('Статус вебинара', max_length=20, choices=status_webinar)
    course_id = models.ForeignKey('Courses', on_delete=models.CASCADE)
    description = models.TextField('О вебинаре')

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'

    def __str__(self):
        return self.title_webinar

    def get_absolute_url(self):
        return f'/crud/webinars/{self.id}'


class Courses(models.Model):
    title_course = models.CharField('Название курса', max_length=50)
    description = models.TextField('О курсе')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title_course

    def get_absolute_url(self):
        return f'/crud/courses/{self.id}'


class SpeakersCoursesBid(models.Model):
    speaker_id = models.ForeignKey('Speakers', on_delete=models.CASCADE)
    courses_id = models.ForeignKey('Courses', on_delete=models.CASCADE)
    bid = models.IntegerField('Ставка преподавателя за час')

    class Meta:
        verbose_name = 'Ставка преподавателя'
        verbose_name_plural = 'Ставки преподавателей'

    def __str__(self):
        return f'{self.speaker_id} по курсу {self.courses_id}'
