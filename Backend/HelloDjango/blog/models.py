from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """Категория"""
    title = models.CharField('Заголовок категории', max_length=255, db_index=True)
    description = models.TextField('Описание', max_length=300, help_text='До 300 символов')
    order = models.PositiveIntegerField('Порядковый номер', null=True, blank=True)
    slug = models.SlugField('Slug', unique=True,
                            help_text='Только маленькие латинские буквы, без пробелов и спецсимволов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']


class Post(models.Model):
    """Пост"""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Категория', related_name='posts')
    title = models.CharField('Заголовок поста', max_length=255, db_index=True)
    description = models.TextField('Краткое описание', max_length=200, help_text='Необходимо для СЕО')
    image = ThumbnailerImageField('Изображение', upload_to='blog/', resize_source={'size': (700, 700), 'crop': 'scale'})
    body = RichTextUploadingField('Контент поста')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True,
                                             help_text='Необходим для сортировки')
    slug = models.SlugField('Slug', unique=True, db_index=True,
                            help_text='Только маленькие латинские буквы, без пробелов и спецсимволов')
    public = models.BooleanField('Опубликовать', default=False)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date', 'order']


class Comment(models.Model):
    """Комметарии к постам"""
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пост',
                             related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Ответ на сообщение', related_name='child')
    name = models.CharField('Имя', max_length=255, db_index=True)
    comment = models.TextField('Комментарий')
    public = models.BooleanField('Опуликовать', default=False)
    date = models.DateTimeField('Создан', auto_now_add=True)
    update = models.DateTimeField('Обновлен', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']




