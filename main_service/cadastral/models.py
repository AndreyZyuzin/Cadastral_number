from django.db import models


class Query(models.Model):
    """Модель запроса."""
    cadastral_number = models.CharField(
        max_length=20,
        verbose_name='Кадастровый Номеры',
        help_text='Кадастровой номер. В виде АА:ВВ:CCCCСCC:КК',
    )
    latitude = models.FloatField(verbose_name='Широта',
                                 help_text='Значение широты',)
    longitude = models.FloatField(verbose_name='Долгота',
                                  help_text='Значение долготы',)
    time_came = models.DateTimeField(verbose_name='In Time',
                                     help_text='Время присланного запроса',)
    time_went = models.DateTimeField(null=True, blank=True,
                                     verbose_name='Out Time',
                                     help_text='Время отправленного запроса',)
    result_response = models.BooleanField(null=True, blank=True,
                                          verbose_name='Ответ',
                                          help_text='Ответ внешнего сервера',)

    class Meta:
        ordering = ['-time_came']
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.cadastral_number
