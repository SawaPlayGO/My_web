from django.db import models
from django.contrib import admin

class Marmelad_order(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    auction = models.BooleanField('Торг')
    price = models.DecimalField('Цена за 1 кг', max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Marmelad_order'

    def __str__(self):
        return f'{self.title} {self.description} {self.auction} {self.price} {self.created_at} {self.update_at}'
    
    @admin.display(description= 'Дата создания')
    def created_date(self):
        from django.utils import timezone, html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return html.format_html(
                '<span style="color:green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        
        self.created_at.strftime('%d.%m.%y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone, html
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return html.format_html(
                '<span style="color:blue; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.update_at.strftime('%d.%m.%y в %H:%M:%S')
