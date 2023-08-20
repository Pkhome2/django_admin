from django.db import models
from django.contrib import admin


class Advertisement(models.Model):

    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    auction = models.BooleanField('Запрос скидки', help_text='Отметьте, если скдидки возможны')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    class Meta:
        db_table = 'advertisements'

    @admin.display(description="Дата созадния")
    def created_date(self):
        from django.utils import timezone, html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return html.format_html("<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", created_time)
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone, html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return html.format_html("<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", updated_time)
        return self.updated_at.strftime("%d.%m.%y в %H:%M:%S")