from django.db import models
from datetime import date

class News(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор')
    title = models.TextField(verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name='Изображение')
    visible = models.BooleanField(default=True, verbose_name='Отобразить')
    posted_at = models.DateField(default=date.today, verbose_name='Дата публикации')

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
    
    def __str__(self):
        return self.title
